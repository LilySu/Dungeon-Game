from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username', 'password')


# The reason we’re making two different serializers for the model is 
# because we’ll be using the UserSerializerWithToken for handling 
# signups. When a user signs up, we want the response from the server 
# to include both their relevant user data (in this case, just
#  the username), as well as the token, which will be stored in 
# the browser for further authentication. But we don’t need the token
#  every time we request a user’s data — just when signing up. 
# Thus, separate serializers.
# That’s the ‘why’, but let’s take a closer look at the code for the 
# ‘how’. Both serializers inherit 
# from rest_framework.serializers.ModelSerializer, which provides us 
# with a handy shortcut for customizing the serializers according to
#  the model data they’ll be working with (otherwise we’d need to 
# spell out every field by hand). In the internal Meta class, we 
# indicate which model each serializer will be representing, and 
# which fields from that model we want the serializer to include.
# But the User class doesn’t have an internal ‘token’ field, so 
# for that we do need to define our own custom field. We define
#  the token variable to be a custom method, then add a get_token() 
# method which handles the manual creation of a new token. It does 
# this using the default settings for payload and encoding handling 
# provided by the JWT package (the payload is the data being tokenized, 
# in this case the user). Finally, we added the custom ‘token’ field 
# to the fields variable in our Meta internal class.
# We also need to make sure the serializer recognizes and stores
#  the submitted password, but doesn’t include it in the returned JSON. 
# So we add the ‘password’ field to fields, but above that also specify
#  that the password should be write only. Then, we override the 
# serializer’s create() method, which determines how the object being 
# serialized gets saved to the database. We do this primarily so that 
# we can call the set_password() method on the user instance, which 
# is how the password gets properly hashed.

