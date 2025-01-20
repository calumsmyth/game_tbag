from character import Character, Enemy

dave = Enemy("Dave", "A smelly zombie")

dave.describe()
dave.set_conversation("Hello there! I am going to join your OOP game very soon")
dave.talk()

dave.set_weakness("cheese")

print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)
