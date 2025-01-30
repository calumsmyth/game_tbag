class Room:
    def __init__(self):
        self.name = None
        self.description = None
        self.linked_room = {}
        self.character = None
        self.item = None
        
    def get_description(self):
        return self.description
    
    def set_description(self, room_description):
        self.description = room_description
        return self.description

    def describe(self):
        print(self.description)

    def get_name(self):
        return self.name

    def set_name(self, room_name):
        self.name = room_name
        return self.name

    def link_room(self, room_to_link, direction):
        self.linked_room[direction] = room_to_link

    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character
    
    def set_item(self, new_item):
        self.item = new_item

    def get_item(self):
        return self.item
    
    def set_objective(self, objective):
        self.objective = objective

    def get_objective(self):
        return self.objective


    def get_details(self):
        print(self.name)
        print("-------------------------")
        print(self.description)
        for direction in self.linked_room:
            room = self.linked_room[direction]
            print("The " + room.get_name() + " is " + direction)

    def move(self, direction):
        if direction in self.linked_room:
            return self.linked_room[direction]
        else:
            print("You can't go that way")
            return self
        
    def start(self):
        print("\n")
        print("[Welcome to the TBAG game! Your goal is to navigate the castle and help Jade find her dance partner.]")
        print("[Navigate through the castle by typing the direction in which the room you want to enter is in ('north', 'east', 'south', 'west'). Do not worry about case sensitivity, we've got you sorted!]")
        print("[Interact with characters and the rooms by using the following commands: 'talk', 'bribe', 'gift', 'fight', 'look' and 'inventory'].")
        print("\n")
        print("You have stumbled upon a grand castle that you have never seen before. The enormous metal door is open and inviting. You can hear jovial music coming from within.")
        print("[Will you enter? (yes/no)]")