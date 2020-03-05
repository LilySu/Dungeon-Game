from django.contrib.auth.models import User
from adventure.models import Player, Room


Room.objects.all().delete()

r_outside = Room(x=1,y=1,title="Outside Cave Entrance",
               description="North of you, the cave mount beckons")

r_foyer = Room(x=1,y=2,title="Foyer", description="""Dim light filters in from the south. Dusty
passages run north and east.""")

r_overlook = Room(x=1,y=3,title="Grand Overlook", description="""A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")

r_narrow = Room(x=2, y=2,title="Narrow Passage", description="""The narrow passage bends here from west
to north. The smell of gold permeates the air.""")

r_treasure = Room(x=2,y=3,title="Treasure Chamber", description="""You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

# START

r_entry = Room(x=2,y=4,title="Entry", description="""You've found the long-lost entry! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_livingroom = Room(x=2,y=5,title="Living Room", description="""You've found the long-lost living room! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_closet = Room(x=2,y=6,title="Closet", description="""You've found the long-lost closet! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_secretroom = Room(x=2,y=7,title="Secret Room", description="""You've found the long-lost secret room! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_diningroom = Room(x=2,y=8,title="Dining Room", description="""You've found the long-lost dining room! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_hallway = Room(x=2,y=9,title="Hallway", description="""You've found the long-lost hallway! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_masterbedroom = Room(x=2,y=10,title="Master Bedroom", description="""You've found the long-lost master bedroom! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")
#7
r_masterbathroom = Room(x=2,y=11,title="Master Bathroom", description="""You've found the long-lost master bathroom! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_study = Room(x=2,y=12,title="Study", description="""You've found the long-lost study! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_walkincloset = Room(x=2,y=13,title= "Walk in Closet", description="""You've found the long-lost walk in closet! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_room11 = Room(x=2,y=14,title="Room 11", description="""You've found the long-lost room 11! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_room12 = Room(x=2,y=15,title="Room 12", description="""You've found the long-lost room 12! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_room13 = Room(x=2,y=16,title="Room 13", description="""You've found the long-lost room 13! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_room14 = Room(x=2,y=17,title="Room 14", description="""You've found the long-lost room 14! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_room15 = Room(x=2,y=18,title="Room 15", description="""You've found the long-lost room 15! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_room16 = Room(x=2,y=19,title="Room 16", description="""You've found the long-lost room 16! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_room17 = Room(x=2,y=20,title="Room 17", description="""You've found the long-lost room 17! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_room18 = Room(x=2,y=21,title="Room 18", description="""You've found the long-lost room 18! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_room19 = Room(x=2,y=22,title="Room 19", description="""You've found the long-lost room 19! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_room20 = Room(x=2,y=23,title="Room 20", description="""You've found the long-lost room 20! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_room21 = Room(x=2,y=24,title="Room 21", description="""You've found the long-lost room 21! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_room22 = Room(x=2,y=25,title="Room 22", description="""You've found the long-lost room 22! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_room23 = Room(x=2,y=26,title="Room 23", description="""You've found the long-lost room 23! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_room24 = Room(x=2,y=27,title="Room 24", description="""You've found the long-lost room 24! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")

r_room25 = Room(x=2,y=28,title="Room 25", description="""You've found the long-lost room 25! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the north.""")
# -------------------------------
r_room26 = Room(x=3,y=28,title="Room 26", description="""You've found the long-lost room 26! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room27 = Room(x=4,y=28,title="Room 27", description="""You've found the long-lost room 27! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room28 = Room(x=5,y=28,title="Room 28", description="""You've found the long-lost room 28! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room29 = Room(x=6,y=28,title="Room 29", description="""You've found the long-lost room 29! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room30 = Room(x=7,y=28,title="Room 30", description="""You've found the long-lost room 30! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room31 = Room(x=8,y=28,title="Room 31", description="""You've found the long-lost room 31! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room32 = Room(x=9,y=28,title="Room 32", description="""You've found the long-lost room 32! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room33 = Room(x=10,y=28,title="Room 33", description="""You've found the long-lost room 33! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room34 = Room(x=11,y=28,title="Room 34", description="""You've found the long-lost room 34! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room35 = Room(x=12,y=28,title="Room 35", description="""You've found the long-lost room 35! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room36 = Room(x=13,y=28,title="Room 36", description="""You've found the long-lost room 36! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room37 = Room(x=14,y=28,title="Room 37", description="""You've found the long-lost room 37! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room38 = Room(x=15,y=28,title="Room 38", description="""You've found the long-lost room 38! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room39 = Room(x=16,y=28,title="Room 39", description="""You've found the long-lost room 39! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room40 = Room(x=17,y=28,title="Room 40", description="""You've found the long-lost room 40! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room41 = Room(x=18,y=28,title="Room 41", description="""You've found the long-lost room 41! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room42 = Room(x=19,y=28,title="Room 42", description="""You've found the long-lost room 42! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room43 = Room(x=20,y=28,title="Room 43", description="""You've found the long-lost room 43! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room44 = Room(x=21,y=28,title="Room 44", description="""You've found the long-lost room 44! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room45 = Room(x=22,y=28,title="Room 45", description="""You've found the long-lost room 45! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room46 = Room(x=23,y=28,title="Room 46", description="""You've found the long-lost room 46! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room47 = Room(x=24,y=28,title="Room 47", description="""You've found the long-lost room 47! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room48 = Room(x=25,y=28,title="Room 48", description="""You've found the long-lost room 48! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room49 = Room(x=26,y=28,title="Room 49", description="""You've found the long-lost room 49! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")

r_room50 = Room(x=27,y=28,title="Room 50", description="""You've found the long-lost room 50! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the east.""")
#----------------------------------
r_room51 = Room(x=27,y=27,title="Room 51", description="""You've found the long-lost room 51! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room52 = Room(x=27,y=26,title="Room 52", description="""You've found the long-lost room 52! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room53 = Room(x=27,y=25,title="Room 53", description="""You've found the long-lost room 53! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room54 = Room(x=27,y=24,title="Room 54", description="""You've found the long-lost room 54! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room55 = Room(x=27,y=23,title="Room 55", description="""You've found the long-lost room 55! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room56 = Room(x=27,y=22,title="Room 56", description="""You've found the long-lost room 56! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room57 = Room(x=27,y=21,title="Room 57", description="""You've found the long-lost room 57! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room58 = Room(x=27,y=20,title="Room 58", description="""You've found the long-lost room 58! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room59 = Room(x=27,y=19,title="Room 59", description="""You've found the long-lost room 59! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room60 = Room(x=27,y=18,title="Room 60", description="""You've found the long-lost room 60! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room61 = Room(x=27,y=17,title="Room 61", description="""You've found the long-lost room 61! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room62 = Room(x=27,y=16,title="Room 62", description="""You've found the long-lost room 62! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room63 = Room(x=27,y=15,title="Room 63", description="""You've found the long-lost room 63! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room64 = Room(x=27,y=14,title="Room 64", description="""You've found the long-lost room 64! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room65 = Room(x=27,y=13,title="Room 65", description="""You've found the long-lost room 65! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room66 = Room(x=27,y=12,title="Room 66", description="""You've found the long-lost room 66! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room67 = Room(x=27,y=11,title="Room 67", description="""You've found the long-lost room 67! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room68 = Room(x=27,y=10,title="Room 68", description="""You've found the long-lost room 68! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room69 = Room(x=27,y=9,title="Room 69", description="""You've found the long-lost room 69! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room70 = Room(x=27,y=8,title="Room 70", description="""You've found the long-lost room 70! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room71 = Room(x=27,y=7,title="Room 71", description="""You've found the long-lost room 71! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room72 = Room(x=27,y=6,title="Room 72", description="""You've found the long-lost room 72! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room73 = Room(x=27,y=5,title="Room 73", description="""You've found the long-lost room 73! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room74 = Room(x=27,y=4,title="Room 74", description="""You've found the long-lost room 74! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

r_room75 = Room(x=27,y=3,title="Room 75", description="""You've found the long-lost room 75! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")

#----------------------------------------------------

r_room76 = Room(x=26,y=3,title="Room 76", description="""You've found the long-lost room 76! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room77 = Room(x=25,y=3,title="Room 77", description="""You've found the long-lost room 77! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room78 = Room(x=24,y=3,title="Room 78", description="""You've found the long-lost room 78! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room79 = Room(x=23,y=3,title="Room 79", description="""You've found the long-lost room 79! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room80 = Room(x=22,y=3,title="Room 80", description="""You've found the long-lost room 80! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room81 = Room(x=21,y=3,title="Room 81", description="""You've found the long-lost room 81! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room82 = Room(x=20,y=3,title="Room 82", description="""You've found the long-lost room 82! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room83 = Room(x=19,y=3,title="Room 83", description="""You've found the long-lost room 83! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room84 = Room(x=18,y=3,title="Room 84", description="""You've found the long-lost room 84! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room85 = Room(x=17,y=3,title="Room 85", description="""You've found the long-lost room 85! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room86 = Room(x=16,y=3,title="Room 86", description="""You've found the long-lost room 86! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room87 = Room(x=15,y=3,title="Room 87", description="""You've found the long-lost room 87! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room88 = Room(x=14,y=3,title="Room 88", description="""You've found the long-lost room 88! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room89 = Room(x=13,y=3,title="Room 89", description="""You've found the long-lost room 89! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room90 = Room(x=12,y=3,title="Room 90", description="""You've found the long-lost room 90! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room91 = Room(x=11,y=3,title="Room 91", description="""You've found the long-lost room 91! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room92 = Room(x=10,y=3,title="Room 92", description="""You've found the long-lost room 92! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room93 = Room(x=9,y=3,title="Room 93", description="""You've found the long-lost room 93! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room94 = Room(x=8,y=3,title="Room 94", description="""You've found the long-lost room 94! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room95 = Room(x=7,y=3,title="Room 95", description="""You've found the long-lost room 95! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room96 = Room(x=6,y=3,title="Room 96", description="""You've found the long-lost room 96! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room97 = Room(x=4,y=3,title="Room 97", description="""You've found the long-lost room 97! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")

r_room98 = Room(x=3,y=3,title="Room 98", description="""You've found the long-lost room 98! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the west.""")


r_outside.save()
r_foyer.save()
r_overlook.save()
r_narrow.save()
r_treasure.save()
r_entry.save()
r_livingroom.save()
r_closet.save()
r_secretroom.save()
r_diningroom.save()
r_hallway.save()
r_masterbedroom.save()
r_masterbathroom.save()
r_study.save()
r_walkincloset.save()
r_room11.save()
r_room12.save()
r_room13.save()
r_room14.save()
r_room15.save()
r_room16.save()
r_room17.save()
r_room18.save()
r_room19.save()
r_room20.save()
r_room21.save()
r_room22.save()
r_room23.save()
r_room24.save()
r_room25.save()
r_room26.save()
r_room27.save()
r_room28.save()
r_room29.save()
r_room30.save()
r_room31.save()
r_room32.save()
r_room33.save()
r_room34.save()
r_room35.save()
r_room36.save()
r_room37.save()
r_room38.save()
r_room39.save()
r_room40.save()
r_room41.save()
r_room42.save()
r_room43.save()
r_room44.save()
r_room45.save()
r_room46.save()
r_room47.save()
r_room48.save()
r_room49.save()
r_room50.save()
r_room51.save()
r_room52.save()
r_room53.save()
r_room54.save()
r_room55.save()
r_room56.save()
r_room57.save()
r_room58.save()
r_room59.save()
r_room60.save()
r_room61.save()
r_room62.save()
r_room63.save()
r_room64.save()
r_room65.save()
r_room66.save()
r_room67.save()
r_room68.save()
r_room69.save()
r_room70.save()
r_room71.save()
r_room72.save()
r_room73.save()
r_room74.save()
r_room75.save()
r_room76.save()
r_room77.save()
r_room78.save()
r_room79.save()
r_room80.save()
r_room81.save()
r_room82.save()
r_room83.save()
r_room84.save()
r_room85.save()
r_room86.save()
r_room87.save()
r_room88.save()
r_room89.save()
r_room90.save()
r_room91.save()
r_room92.save()
r_room93.save()
r_room94.save()
r_room95.save()
r_room96.save()
r_room97.save()
r_room98.save()












# Link rooms together
r_outside.connectRooms(r_foyer, "n")
r_foyer.connectRooms(r_outside, "s")

r_foyer.connectRooms(r_overlook, "n")
r_overlook.connectRooms(r_foyer, "s")

r_foyer.connectRooms(r_narrow, "e")
r_narrow.connectRooms(r_foyer, "w")

r_narrow.connectRooms(r_treasure, "n")
r_treasure.connectRooms(r_narrow, "s")

r_treasure.connectRooms(r_entry,"n")
r_entry.connectRooms(r_treasure,'s')

r_entry.connectRooms(r_livingroom,"n")
r_livingroom.connectRooms(r_entry,'s')

r_livingroom.connectRooms(r_closet,'n')
r_closet.connectRooms(r_livingroom, "s")

r_closet.connectRooms(r_secretroom, 'n')
r_secretroom.connectRooms(r_closet,'s')

r_secretroom.connectRooms(r_diningroom,'n')
r_diningroom.connectRooms(r_secretroom, 's')

r_diningroom.connectRooms(r_hallway,'n')
r_hallway.connectRooms(r_diningroom,'s')

r_hallway.connectRooms(r_masterbedroom, 'n')
r_masterbedroom.connectRooms(r_hallway,'s')

r_masterbedroom.connectRooms(r_masterbathroom,'n')
r_masterbathroom.connectRooms(r_masterbedroom, 's')

r_masterbathroom.connectRooms(r_study, 'n')
r_study.connectRooms(r_masterbathroom, 's')

r_study.connectRooms(r_walkincloset,'n')
r_walkincloset.connectRooms(r_study,'s')

r_walkincloset.connectRooms(r_room11,'n')
r_room11.connectRooms(r_walkincloset,'s')

r_room11.connectRooms(r_room12, 'n')
r_room12.connectRooms(r_room11,'s')

r_room12.connectRooms(r_room13, 'n')
r_room13.connectRooms(r_room12, 's')

r_room13.connectRooms(r_room14, 'n')
r_room14.connectRooms(r_room13,'s')

r_room14.connectRooms(r_room15, 'n')
r_room15.connectRooms(r_room14,'s')

r_room15.connectRooms(r_room16,'n')
r_room16.connectRooms(r_room15,'s')

r_room16.connectRooms(r_room17,'n')
r_room17.connectRooms(r_room16, 's')

r_room17.connectRooms(r_room18,'n')
r_room18.connectRooms(r_room17, 's')

r_room18.connectRooms(r_room19,'n')
r_room19.connectRooms(r_room18,'s')

r_room19.connectRooms(r_room20, 'n')
r_room20.connectRooms(r_room19, 's')

r_room20.connectRooms(r_room21,'n')
r_room21.connectRooms(r_room20, 's')

r_room21.connectRooms(r_room22,'n')
r_room22.connectRooms(r_room21,'s')

r_room22.connectRooms(r_room23,'n')
r_room23.connectRooms(r_room22,'s')

r_room23.connectRooms(r_room24,'n')
r_room24.connectRooms(r_room23,'s')

r_room24.connectRooms(r_room25,'n')
r_room25.connectRooms(r_room24,'s')

r_room25.connectRooms(r_room26,'e')
r_room26.connectRooms(r_room25,'w')

r_room26.connectRooms(r_room27,'e')
r_room27.connectRooms(r_room26,'w')

r_room27.connectRooms(r_room28,'e')
r_room28.connectRooms(r_room27,'w')

r_room28.connectRooms(r_room29,'e')
r_room29.connectRooms(r_room28,'w')

r_room29.connectRooms(r_room30,'e')
r_room30.connectRooms(r_room29,'w')

r_room30.connectRooms(r_room31,'e')
r_room31.connectRooms(r_room30,'w')

r_room31.connectRooms(r_room32,'e')
r_room32.connectRooms(r_room31,'w')

r_room32.connectRooms(r_room33,'e')
r_room33.connectRooms(r_room32,'w')

r_room33.connectRooms(r_room34,'e')
r_room34.connectRooms(r_room33,'w')

r_room34.connectRooms(r_room35,'e')
r_room35.connectRooms(r_room34,'w')

r_room35.connectRooms(r_room36,'e')
r_room36.connectRooms(r_room35,'w')

r_room36.connectRooms(r_room37,'e')
r_room37.connectRooms(r_room36,'w')

r_room37.connectRooms(r_room38,'e')
r_room38.connectRooms(r_room37,'w')

r_room38.connectRooms(r_room39,'e')
r_room39.connectRooms(r_room38,'w')

r_room39.connectRooms(r_room40,'e')
r_room40.connectRooms(r_room39,'w')

r_room40.connectRooms(r_room41,'e')
r_room41.connectRooms(r_room40,'w')

r_room41.connectRooms(r_room42,'e')
r_room42.connectRooms(r_room41,'w')

r_room42.connectRooms(r_room43,'e')
r_room43.connectRooms(r_room42,'w')

r_room43.connectRooms(r_room44,'e')
r_room44.connectRooms(r_room43,'w')

r_room44.connectRooms(r_room45,'e')
r_room45.connectRooms(r_room44,'w')

r_room45.connectRooms(r_room46,'e')
r_room46.connectRooms(r_room45,'w')

r_room46.connectRooms(r_room47,'e')
r_room47.connectRooms(r_room46,'w')

r_room47.connectRooms(r_room48,'e')
r_room48.connectRooms(r_room47,'w')

r_room48.connectRooms(r_room49,'e')
r_room49.connectRooms(r_room48,'w')

r_room49.connectRooms(r_room50,'e')
r_room50.connectRooms(r_room49,'w')

#south

r_room50.connectRooms(r_room51,'s')
r_room51.connectRooms(r_room50,'n')

r_room51.connectRooms(r_room52,'s')
r_room52.connectRooms(r_room51,'n')

r_room52.connectRooms(r_room53,'s')
r_room53.connectRooms(r_room52,'n')

r_room53.connectRooms(r_room54,'s')
r_room54.connectRooms(r_room53,'n')

r_room54.connectRooms(r_room55,'s')
r_room55.connectRooms(r_room54,'n')

r_room55.connectRooms(r_room56,'s')
r_room56.connectRooms(r_room55,'n')

r_room56.connectRooms(r_room57,'s')
r_room57.connectRooms(r_room56,'n')

r_room57.connectRooms(r_room58,'s')
r_room58.connectRooms(r_room57,'n')

r_room58.connectRooms(r_room59,'s')
r_room59.connectRooms(r_room58,'n')

r_room59.connectRooms(r_room60,'s')
r_room60.connectRooms(r_room59,'n')

r_room60.connectRooms(r_room61,'s')
r_room61.connectRooms(r_room60,'n')

r_room61.connectRooms(r_room62,'s')
r_room62.connectRooms(r_room61,'n')

r_room62.connectRooms(r_room63,'s')
r_room63.connectRooms(r_room62,'n')

r_room63.connectRooms(r_room64,'s')
r_room64.connectRooms(r_room63,'n')

r_room64.connectRooms(r_room65,'s')
r_room65.connectRooms(r_room64,'n')

r_room65.connectRooms(r_room66,'s')
r_room66.connectRooms(r_room65,'n')

r_room66.connectRooms(r_room67,'s')
r_room67.connectRooms(r_room66,'n')

r_room67.connectRooms(r_room68,'s')
r_room68.connectRooms(r_room67,'n')

r_room68.connectRooms(r_room69,'s')
r_room69.connectRooms(r_room68,'n')

r_room69.connectRooms(r_room70,'s')
r_room70.connectRooms(r_room69,'n')

r_room70.connectRooms(r_room71,'s')
r_room71.connectRooms(r_room70,'n')

r_room71.connectRooms(r_room72,'s')
r_room72.connectRooms(r_room71,'n')

r_room72.connectRooms(r_room73,'s')
r_room73.connectRooms(r_room72,'n')

r_room73.connectRooms(r_room74,'s')
r_room74.connectRooms(r_room73,'n')

r_room74.connectRooms(r_room75,'s')
r_room75.connectRooms(r_room74,'n')

#west
r_room75.connectRooms(r_room76,'w')
r_room76.connectRooms(r_room75,'e')

r_room76.connectRooms(r_room77,'w')
r_room77.connectRooms(r_room76,'e')

r_room77.connectRooms(r_room78,'w')
r_room78.connectRooms(r_room77,'e')

r_room78.connectRooms(r_room79,'w')
r_room79.connectRooms(r_room78,'e')

r_room79.connectRooms(r_room80,'w')
r_room80.connectRooms(r_room79,'e')

r_room80.connectRooms(r_room81,'w')
r_room81.connectRooms(r_room80,'e')

r_room81.connectRooms(r_room82,'w')
r_room82.connectRooms(r_room81,'e')

r_room82.connectRooms(r_room83,'w')
r_room83.connectRooms(r_room82,'e')

r_room83.connectRooms(r_room84,'w')
r_room84.connectRooms(r_room83,'e')

r_room84.connectRooms(r_room85,'w')
r_room85.connectRooms(r_room84,'e')

r_room85.connectRooms(r_room86,'w')
r_room86.connectRooms(r_room85,'e')

r_room86.connectRooms(r_room87,'w')
r_room87.connectRooms(r_room86,'e')

r_room87.connectRooms(r_room88,'w')
r_room88.connectRooms(r_room87,'e')

r_room88.connectRooms(r_room89,'w')
r_room89.connectRooms(r_room88,'e')

r_room89.connectRooms(r_room90,'w')
r_room90.connectRooms(r_room89,'e')

r_room90.connectRooms(r_room91,'w')
r_room91.connectRooms(r_room90,'e')

r_room91.connectRooms(r_room92,'w')
r_room92.connectRooms(r_room91,'e')

r_room92.connectRooms(r_room93,'w')
r_room93.connectRooms(r_room92,'e')

r_room93.connectRooms(r_room94,'w')
r_room94.connectRooms(r_room93,'e')

r_room94.connectRooms(r_room95,'w')
r_room95.connectRooms(r_room94,'e')

r_room95.connectRooms(r_room96,'w')
r_room96.connectRooms(r_room95,'e')

r_room96.connectRooms(r_room97,'w')
r_room97.connectRooms(r_room96,'e')

r_room97.connectRooms(r_room98,'w')
r_room98.connectRooms(r_room97,'e')

r_room98.connectRooms(r_treasure,'w')
r_treasure.connectRooms(r_room98,'e')


players=Player.objects.all()
for p in players:
  p.currentRoom=r_outside.id
  p.save()

