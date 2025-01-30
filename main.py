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
ballroom.set_description("A vast room with a shiny wooden floor. There appears to be a wooden door in the corner which grabs your attention. Could it be worth a look?")

#created dining hall as a room with description
dining_hall = Room()
dining_hall.set_name("dining hall")
dining_hall.set_description("A large room with ornate golden decorations")

#Linked rooms to each other and which direction they are. 
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

#Created Dave as an enemy with conversation, description, weakness, bribe and which room he is in
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation('"Brrlgrh... rgrhl... brains..."')
dave.set_weakness("cheese")
dave.set_favourite("brains")
dining_hall.set_character(dave)

#Created Jade as a friend including conversation, a potential gift item and which room she is in
jade = Friend("Jade", "A young woman in a flowing green ballgown")
jade.set_conversation('"Tonight is not my night! I forgot my necklace at home, and now James, my dance partner, is nowhere to be found. He is always on time usually! I was stood in the ballroom, but a strange man walked in. I was so scared that I left in a rush. I did find a key on my way here though, not sure what it does."')
jade.set_gift_item("necklace")
kitchen.set_character(jade)


#Created Dr. Acular as an enemy with conversation, description, weakness, potential bribe item and which room he is in,. 
dr_acular = Enemy("Dr. Acular", "A tall, slender and very pale man with two very pointed teeth and a long black jacket. There's a red stain on the collar of his white shirt.")
dr_acular.set_conversation('"Looks like dinner is served!"')
dr_acular.set_weakness("stake")
dr_acular.set_favourite("blood")
ballroom.set_character(dr_acular)
ballroom.set_objective("closet door")

#Create Key item and place in the Kitchen
key = Item()
key.set_name("Ballroom closet key")
key.set_description("an old rusty key. There is a tag hanging from it with faded writing which seems to say 'Ballroom closet'")
jade.add_item(key)

#Create 'Player' character
player = Character("Hero", "This is you, the player, the hero of this story.")



current_room = kitchen

i = True
while i == True:
    start = Room()
    start.start()
    begin = input("> ").lower()
    if begin == ("yes"):
        i == False
        break
    else:
        print("Your nerves get the better of you and you decide not to explore any further. You turn around and walk home. You will forever wonder why the castle seemed so enticing. When you return at a later date, you find the castle has vanished completely.")
        print("[Game Over!]")
        exit()


while True:
        
    print("\n")
    print("[MOVE to a different room using: 'north', 'east', 'south' or 'west'] [INTERACT with 'talk', 'bribe', 'gift', 'fight', 'look' or 'inventory']")
    print("\n")
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    command = input("> ").lower()

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
            bribe_with = input().lower()
            bribe_result = inhabitant.bribe(bribe_with)
            if bribe_result == False:
                print("Game Over")
                break
        else:
            print("There is no one to bribe in the room.")
    elif command == "gift":
        if Friend:
            print("What will you give?")
            give_item = input().lower()
            give_result = inhabitant.gift(give_item)
            if inhabitant.inventory:
                inventory_item = ", ".join([item.get_name() for item in inhabitant.get_inventory()])
                print(inhabitant.get_name() + " holds out their hand. In it you see a " + inventory_item + ".")
                player.add_item(inventory_item)
                print("[GOT ITEM:] " + inventory_item + " was added to your inventory.")


    elif command == "fight":
        if inhabitant:
            print("What will you fight with?")
            fight_with = input().lower()
            fight_result = inhabitant.fight(fight_with)
            if fight_result == False:
                print("Game Over")
                break
        else:
            print("There is no one in the room to fight.")

    elif command == "inventory":
        if player.inventory:
            print(", ".join(player.inventory))
        else:
            print("You currently have no items in your inventory.")

    elif command == "look":
        if ballroom.get_objective:
            print("There is a very ornate looking wooden door in the corner. It seems as though it may be even older than the building itself.")
            if player.inventory:
                print("Would you like to use the key? (yes/no)")
                use_key = input("> ").lower()

                if use_key == "yes":
                    print("You unlock the closet and find Jade's dance partner, James, tied up inside. You take off his bindings and help him leave the building.")
                    print("Congratulations, you have completed the quest!")
                    print("Game Complete!")
                    break
                if use_key == "no":
                    print("You leave the door alone.")
            else:
                print("It appears to be locked. Maybe someone has the key to open it.")