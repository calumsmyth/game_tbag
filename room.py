class Room:
    def __init__(self):
        self.name = None
        self.description = None
        self.linked_room = {}
        
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