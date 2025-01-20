from room import Room
from character import Enemy, Character

kitchen = Room()
kitchen.set_name("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom = Room()
ballroom.set_name("ballroom")
ballroom.set_description("A vast room with a shiny wooden floor")

dining_hall = Room()
dining_hall.set_name("dining hall")
dining_hall.set_description("A large room with ornate golden decorations")


kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)


current_room = kitchen
while True:
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ")

    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
    elif command == "talk":
        if inhabitant:
            inhabitant.talk()
        else:
            print("You are in the room alone.")
    elif command == "fight":
        if inhabitant:
            print("What will you fight with?")
            fight_with = input()
            
            fight_result = inhabitant.fight(fight_with)
            if fight_result == False:
                print("Game Over")
                break
        else:
            print("There is no one in the room to fight.")