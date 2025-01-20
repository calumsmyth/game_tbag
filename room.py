class Room:
    def __init__(self):
        self.name = None
        self.description = None
        self.linked_room = {}
        self.character = None
        
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