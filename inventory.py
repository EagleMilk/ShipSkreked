from Room import Room


class Inventory():
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def drop(self, item):
        self.items.remove(item)

    def list(self):
        print ("You are carrying:")
        for item in self.items:
            print (item.get_name())

    def get(self, type):
        items_of_type = []
        for item in self.items:
            if isinstance(item, type):
                items_of_type.append(item)
        return items_of_type

    def process_command(self, command):
        result = []
        for item in self.items:
            if item.get_name() in command:
                result.append(item.process_command(command))
        return result


class Item():
    def __init__(self, name, description):
        self.name = name
        self.known_commands = {}
        self.itemsdescriptions = {name: description}

    def get_name(self):
        return self.name

    def process_command(self, command):
        for a_command in self.known_commands:
            if a_command in command:
                self.known_commands[a_command](command)


class Literature(Item):
    def __init__(self, name, contents="This item is blank"):
        Item.__init__(self, name)
        self.contents = contents

    def read(self):
        print self.contents

    def set_contents(self, contents):
        self.contents = contents


class Flashlight(Item):
    def __init__(self, name, battery_level=100, state='off'):
        Item.__init__(self, name)
        self.battery_level = battery_level
        self.state = state


    def turn_on(self):
        self.state = "On"

    def turn_off(self):
        self.state = "Off"

    def change_batteries(self):
        self.battery_level = 100

    def compute_usage(self):
        pass



class LightSource(Item):
    def __init__(self, name, on=False):
        self.on = on
        Item.__init__(self, name)
        self.known_commands["turn on"] = self.turn_on
        self.known_commands["turn off"] = self.turn_off

    @staticmethod
    def is_one_on(sources):
        if len(sources) > 0:
            for source in sources:
                if source.is_on():
                    return True
        return False

    def is_on(self):
        return self.on

    def turn_on(self, command):
        self.on = True
        print ("The " + self.name + " is on.")

    def turn_off(self, command):
        self.on = False
        print ("The " + self.name + " is off.")

class Wallet(Item):
    def __init__(self, name, description):
        Item.__init__(self, name, description)
        self.known_commands["inspect"] = self.inspect()

    def inspect(self):
        return self.itemsdescriptions[self.name]


class Flashlight(LightSource):
    def __init__(self, name="flashlight", battery_level=100, on=False):
        LightSource.__init__(self, name, on)
        self.battery_level = battery_level

    def change_batteries(self):
        self.battery_level=100

    def compute_usage(self):
        # Compute the time it's been on and then drain the battery an equal amount
        pass

class DarkRoom(Room):
    def enter_room(self, inventory):
        light_sources = inventory.get(LightSource)
        if LightSource.is_one_on(light_sources):
            Room.enter_room(self, inventory)
        else:
            print ("You were eaten by a grue.")
            print ("Game over.")
            exit()
