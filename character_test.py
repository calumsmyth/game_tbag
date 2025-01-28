from character import Character, Enemy
from item import Item
from room import Room

'''dave = Enemy("Dave", "A smelly zombie")

dave.describe()
dave.set_conversation("Hello there! I am going to join your OOP game very soon")
dave.talk()

dave.set_weakness("cheese")

print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)'''

key = Item()
key.set_name("ballroom closet key")
key.set_description("An old rusty key. There is a tag hanging from it with faded writing which seems to say 'Ballroom closet'.")

kitchen = Room()
kitchen.set_name("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")



kitchen.set_item(key)
if kitchen.get_item():
    print("Item in the kitchen is:" + kitchen.get_item().get_name())
    print("Item description is:" + kitchen.get_item().get_description())
else:
    print("There is no item in the kitchen")
