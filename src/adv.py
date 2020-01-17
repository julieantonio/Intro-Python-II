from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

cat = Item('cat', 'A chokin cat named Maceo')
bow = Item('bow', 'A bow fashioned from yew wood')
arrows = Item('arrows', 'A quiver of arrows with feathered ends')

room['foyer'].room_inventory.append(cat)
room['overlook'].room_inventory.append(bow)
room['overlook'].room_inventory.append(arrows)


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

directions = ['n', 'e', 's', 'w']

def adventure_game():
    name = 'mysterious adventurer'
    player = Player(name, room['outside'])
    print("Wow this is a game do you want to play it")

    user_input = int(input("Press [1] to start or [9] to exit "))

    if user_input == 1:
        name = input("What is your name? ")
        if name != '':
            player.name = name
        print(f"\n Welcome {player.name}. \n Move by entering [N]/[E]/[S]/[W] \n You are {player.current_room.name}. \n {player.current_room.desc}")
    elif user_input == 9:
        print('goodbye')
    while user_input == 1:
        choice = input("\n what will you do?")
        if choice.lower() in directions:
            player.travel(choice.lower())

        elif 'get' in choice:
            split_string = choice.split()
            # print(f'Got {split_string[1]}')
            player.get_item(split_string[1].lower())

        elif 'drop' in choice:
            split_string = choice.split()
            player.drop_item(split_string[1].lower())

        elif choice.lower() == 'inventory' or choice.lower() == 'backpack':
            if player.player_inventory != []:
                print('You look in your backpack and see:')
                for x in player.player_inventory:
                    print(f"{x.name} \n {x.desc}")

            else:
                print('Your backpack is empty')
            
        elif choice == 'win the game':
            print('ok, you win')
            break

        elif choice == '9':
            print('Goodbye')
            break

        else:
            print(choice)
            print("I don't recognize that command, please try again")
        
    else:
        print('Invalid input')

adventure_game()
            