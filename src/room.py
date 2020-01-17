# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.room_inventory = []
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
    def get_room_in_direction(self, direction):
        if direction == 'n':
            return self.n_to
        elif direction == 'e':
            return self.e_to
        elif direction =='s':
            return self.s_to
        elif direction == 'w':
            return self.w_to
        else:
            return None
    def get_room_items(self):
        if self.room_inventory != []:
            print('You see a')
            for item in self.room_inventory:
                print(item.name)
        else:
            print("There's nothing here")
    # def __str__(self):
    #     return f"You are in the {self.name} room. It is {self.desc}"