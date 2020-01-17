# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.player_inventory = []

    def travel(self, directions):
        next_room = self.current_room.get_room_in_direction(directions)
        if next_room is not None:
            self.current_room = next_room
            print(f"*****{self.current_room.name}***** \n {self.current_room.desc} \n")
            self.current_room.get_room_items()
        else:
            print('You cannot move in that direction')

    def get_item(self, item_name):
        for item in self.current_room.room_inventory:
            if item.name == item_name:
                print(f'You put the {item.name} in your backpack')
                self.current_room.room_inventory.remove(item)
                return self.player_inventory.append(item)
        print("That item isn't here")

    def drop_item(self, item_name):
        for item in self.player_inventory:
            if item.name == item_name:
                print(f"You dropped the {item.name}")
                self.player_inventory.remove(item)
                return self.current_room.room_inventory.append(item)
            print("You don't have that item in your inventory")