from room import Room
from character import Enemy, Character, Friend
from item import Item

#Created Kitchen as a room with a description 
kitchen = Room()
kitchen.set_name("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

#Created ballroom as a room with a description
ballroom = Room()
ballroom.set_name("ballroom")
ballroom.set_description("A vast room with a shiny wooden floor")

#created dining hall as a room with description
dining_hall = Room()
dining_hall.set_name("dining hall")
dining_hall.set_description("A large room with ornate golden decorations")

#Linked rooms to each other and which direction they are in comparison. 
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

#Created Dave as an enemy with conversation, description, weakness, bribe and which room he is in
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dave.set_favourite("brains")
dining_hall.set_character(dave)

#Created Jade as a friend including conversation, a potential gift item and which room she is in
jade = Friend("Jade", "A young woman in a flowing green ballgown")
jade.set_conversation("I am waiting for my dance partner to arrive, but there's a strange man in the ballroom.")
jade.set_gift_item("necklace")
kitchen.set_character(jade)

#Created Dr. Acular as an enemy with conversation, description, weakness, potential bribe item and which room he is in,. 
dr_acular = Enemy("Dr. Acular", "A tall, slender and very pale man with two very pointed teeth and a long black jacket. There's a red stain on the collar of his white shirt.")
dr_acular.set_conversation("Looks like dinner is served!")
dr_acular.set_weakness("stake")
dr_acular.set_favourite("blood")
ballroom.set_character(dr_acular)

#Create Key item and place in the Kitchen
key = Item()
key.set_name("Ballroom closet key")
key.set_description("an old rusty key. There is a tag hanging from it with faded writing which seems to say 'Ballroom closet'")
kitchen.set_item(key)

#Create 'Player' character
player = Character("Hero", "This is you, the player, the hero of this story.")



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
    elif command == "bribe":
        if inhabitant:
            print("How will you bribe them?")
            bribe_with = input()
            bribe_result = inhabitant.bribe(bribe_with)
            if bribe_result == False:
                print("Game Over")
                break
        else:
            print("There is no one to bribe in the room.")
    elif command == "gift":
        if Friend:
            print("What will you give?")
            give_item = input()
            give_result = inhabitant.gift(give_item)
    
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

    elif command == "look":
        if current_room.get_item():
            print("In the " + current_room.get_name() + " you see " + current_room.get_item().get_description() + ". It would seem that you have found the " + current_room.get_item().get_name() + ".")
            player.add_item(current_room.get_item().get_name())
            print("[GOT ITEM:] " + current_room.get_item().get_name() + " was added to your inventory.")
        else:
            print("There are no useful items in this room.")

    elif command == "inventory":
        if player.inventory:
            print(player.inventory)
        else:
            print("You currently have no items in your inventory.")