from django.conf.urls import url
from . import api

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    url('getroom', api.getroom),
    url('getallrooms', api.getallrooms),
    url('make_grid', api.make_grid),
]