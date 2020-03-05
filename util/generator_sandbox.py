import random

# n = 500
# xy = {"x": 4, "y": 8}
# direction = {"n": , "s": , "e": , "w": }
# title = {"title":"Room"+ str(n)}
# description = {"description": "There are exits to the east"}
# items = {"items":["powerpellet"]}
# roomlist = []
# roomlist.append(a)
# roomlist.append(b)
# ndict = {}

def create_room(grid_dimension):
    num_rooms = grid_dimension**2
    for i in range(num_rooms):

        x_value = i/grid_dimension
        y_value = i%grid_dimension
        xy = {"x": x_value, "y": y_value}

        if i > grid_dimension:
            n_to = i - grid_dimension
            s_to = i + grid_dimension
        else:
            n_to = 0
            s_to = 0
        if (i % grid_dimension != 0) or ((i-1) % grid_dimension !=0):
            e_to = i + 1
            w_to = i - 1
        else:
            e_to = 0
            w_to = 0
            
        direction = {"n" : n_to , "s": s_to, "e": e_to, "w": w_to}

        title = {"title":"Room"+ str(num_rooms)}
        description = {"description": "There are exits to the east"}
        items = {"items":["powerpellet"]}
                    
        roomlist = []
        roomlist.append(xy)
        roomlist.append(direction)
        roomlist.append(items)
        print({str(random.randrange(num_rooms)) : roomlist})

create_room(10)



    # def gen_fixture(self):

    #     grid_list = [item for sublist in self.grid for item in sublist]# grid turns into list

    #     list_before_json = []

    #     for i, room in enumerate(grid_list, start = 0):
    #         if room is None:
    #             break
    #         room_to_json = {}
    #         room_to_json["model"] = "adventure.room"
    #         room_to_json["pk"] = room.id
    #         room_to_json["fields"] = {
    #             "title": room.name,
    #             "description": room.description,
    #             "n_to": room.n_to,
    #             "s_to": room.s_to,
    #             "e_to": room.e_to,
    #             "w_to": room.w_to,
    #             "x": room.x,
    #             "y": room.y,
    #         }