from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from pusher import Pusher
from django.http import JsonResponse
from decouple import config
from django.contrib.auth.models import User
from .models import *
from rest_framework.decorators import api_view
import json
# from util.sample_generator import World
from util.lily_generator import World
from django.http import HttpResponse
from django.core import serializers
from django.core.serializers import serialize
# w = World()
# num_rooms = 100
# width = 10
# height = 10
# w.generate_rooms(width, height, num_rooms)
# w.print_rooms()

all_rooms = {}

with open('adventure/static/rooms.json') as f:
    all_rooms = json.load(f)    


@csrf_exempt
@api_view(['POST'])
def pusher_auth(request):
    print(request)
    auth = pusher.authenticate(
        channel=request.form['presence-main-channel'],
        socket_id=request.form['socket_id']
    )
    return json.dumps(auth)

# instantiate pusher
pusher = Pusher(app_id=config('PUSHER_APP_ID'), key=config('PUSHER_KEY'), secret=config('PUSHER_SECRET'), cluster=config('PUSHER_CLUSTER'))
@csrf_exempt
@api_view(["GET"])
# def initialize(request):
#     user = request.user
#     player = user.player
#     player_id = player.id
#     uuid = player.uuid
#     room = player.room()
#     exists_rooms = Room.objects.filter(exists=room.exists)#selecting a subset
#     exists_map = {
#     "room_exists": room.exists,
#     "rooms": [{
#         'id': i.id,
#         'x': i.x,
#         'y': i.y,
#         'n_to': i.n_to,
#         's_to': i.s_to,
#         'e_to': i.e_to,
#         'w_to': i.w_to,
#         } for i in exists_rooms]
#     }
#     players = room.playerNames(player_id)
#     return JsonResponse({'uuid': uuid, 'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players, 'exists_map': exists_map}, safe=True)

def initialize(request):
    user = request.user
    player = user.player
    player_id = player.id
    uuid = player.uuid
    room = player.room()
    players = room.playerNames(player_id)
    return JsonResponse({'uuid': uuid, 'name':player.user.username, 'title':room.title, 'description':room.description, 'players':players}, safe=True)

# @csrf_exempt
@api_view(["POST"])
def move(request):
    dirs={"n": "north", "s": "south", "e": "east", "w": "west"}
    reverse_dirs = {"n": "south", "s": "north", "e": "west", "w": "east"}
    player = request.user.player
    player_id = player.id
    player_uuid = player.uuid
    data = json.loads(request.body)
    direction = data['direction']
    room = player.room()
    nextRoomID = None
    if direction == "n":
        nextRoomID = room.n_to
    elif direction == "s":
        nextRoomID = room.s_to
    elif direction == "e":
        nextRoomID = room.e_to
    elif direction == "w":
        nextRoomID = room.w_to
    if nextRoomID is not None and nextRoomID > 0:
        nextRoom = Room.objects.get(id=nextRoomID)
        player.currentRoom=nextRoomID
        player.save()
        players = nextRoom.playerNames(player_id)
        currentPlayerUUIDs = room.playerUUIDs(player_id)
        nextPlayerUUIDs = nextRoom.playerUUIDs(player_id)
        for p_uuid in currentPlayerUUIDs:
            pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has walked {dirs[direction]}.'})
        for p_uuid in nextPlayerUUIDs:
            pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username} has entered from the {reverse_dirs[direction]}.'})
        return JsonResponse({'name':player.user.username, 'title':nextRoom.title, 'position':[nextRoom.x, nextRoom.y],  'description':nextRoom.description, 'players':players, 'error_msg':""}, safe=True)
    else:
        players = room.playerNames(player_id)

        return JsonResponse({'name':player.user.username, 'title':room.title, 'description':room.description,  'players':players, 'error_msg':"You cannot move that way."}, safe=True)
@csrf_exempt
@api_view(["POST"])
def say(request):
    # IMPLEMENT
    player = request.user.player
    player_id = player.id
    player_uuid = player.uuid
    room = player.room()
    message = json.loads(request.body)['message']
    currentRoomPlayerUUID = room.playerUUIDs(player_id)
    currentRoomPlayerUUID.append(player_uuid)
    for p_uuid in currentRoomPlayerUUID:
            pusher.trigger(f'p-channel-{p_uuid}', u'broadcast', {'message':f'{player.user.username}: {message}'})
    return JsonResponse({'data':message}, safe=True, status=200)
@csrf_exempt
@api_view(["GET"])
def getallrooms(request):
    print(request.body)
    get_rooms = Room.objects.all()

    rooms = {}

    for room in get_rooms.values():
        id = str(room['id'])
        xy = {"x": room['x'], "y": room['y']}
        title = {"title": room['title']}
        description = {"description": room['description']}
        connections = {'n': room['n_to'], 'e': room['e_to'], 'w': room['w_to'], 's': room['s_to']}
        connections = { k: v for k, v in connections.items() if v != 0}
        
        modified_room = [xy, connections, title, description, {"items": []}]
        rooms[id] = modified_room
        
    return JsonResponse({"rooms": rooms}, safe=True, status=200)


@csrf_exempt
@api_view(["GET"])
def getroom(request):
    print(request.body)
    room = Room.objects.get(id=json.loads(request.body)['id'])
    return JsonResponse({'id': room.id, 'n_to': room.n_to,'s_to': room.s_to, 'e_to': room.e_to, 'w_to': room.w_to, 'x': room.x, 'y': room.y}, safe=True,status=200)


@api_view(["GET"])
def make_grid(request):
    Room.objects.create(title = "A Generic Room", description = "This is a generic room.", n_to = 0, s_to = 0, e_to = 0, w_to = 0)
    data = serializers.serialize('json',Room.objects.get())
    return JsonResponse(data, safe=False)
    try:
        Room.objects.all().delete()
    except:
        pass
    map = World()
    map.generate_rooms(11, 11, 100)
    players=Player.objects.all()
    for p in players:
        p.currentRoom=1
        p.save()
    Room.objects.all()
    return JsonResponse({"rooms": list(Room.objects.values())})