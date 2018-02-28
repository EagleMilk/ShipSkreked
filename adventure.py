from Room import Room
from inventory import Inventory

print '   _____ __                       __         __\n  / ___// /__________ _____  ____/ /__  ____/ /\n  \__ \/ __/ ' \
      '___/ __ `/ __ \/ __  / _ \/ __  / \n ___/ / /_/ /  / /_/ / / / / /_/ /  __/ /_/ /  \n/____/\__/_/   \__,' \
      '_/_/ /_/\__,_/\___/\__,_/   \n '


Beach = Room('Beach', "You find yourself awake on a beach - palm trees swaying in the wind, the ocean breeze upon your face, and white sand all around you.", 1)
dining = Room('dining room', 'you are in the dining room', 2)
hallway = Room('hallway', 'you are in the hallway', 3)
hallway2 = Room('upstairs hallway', "You are in the upstairs hallway", 4)
bedroom = Room('bedroom', 'you are in the bedroom', 5)
bedroom2 = Room('bedroom', 'You are in the bedroom', 6)
bedroom3 = Room('bedroom', 'You are in the bedroom', 7)
living = Room('living room', 'you are in the living room', 8)


inventory = Inventory()
current_room = Beach

while True:
    current_room.enter_room()
    command = raw_input("What do you want to do?\n")
    print
    if command == 'x':
        break

    result = current_room.process_command(command, inventory)
    if isinstance(result, Room):
        current_room = result
        result.enter_room()
        continue
    elif isinstance(result, str):
        print result
        continue
    else:
        print 'Stop that \n'

