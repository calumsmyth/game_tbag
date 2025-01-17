from room import Room

kitchen = Room()
kitchen.set_name("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies")

ballroom = Room()
ballroom.set_name("ballroom")
ballroom.set_description("A vast room with a shiny wooden floor")

dining_room = Room()
dining_room.set_name("dining hall")
dining_room.set_description("A large room with ornate golden decorations")


print(kitchen.name)
kitchen.describe()

print(ballroom.name)
ballroom.describe()

print(dining_room.name)
dining_room.describe()
