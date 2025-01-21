class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
    
    def describe(self):
        print(self.name + " is here!")
        print(self.description)
    
    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]:" + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")
        
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    
    def bribe(self, bribe_item):
        print(self.name + " can't be bribed.")
        return True
    


    
class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
    
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print(self.name + " crushes you, puny adventurer")
            return False
    def set_favourite(self, favourite_item):
        self.favourite = favourite_item

    def get_favourite(self):
        return self.favourite 
    
    def bribe(self, bribe_item):
        if bribe_item == self.favourite:
            print(self.name + " takes the " + bribe_item + " with a smile. They have accepted your bribe.")
            return True
        else:
            print(self.name + " has no interest in the " + bribe_item + ". " + self.name + " didn't like your attempt to bribe them. They make sure you can never try to bribe anyone ever again!")
            return False
    def gift(self, gift_item):
        self.gift_item = gift_item
        print(self.name + " doesn't want any gifts.")


class Friend(Character):
    def __init__(self, char_name, char_description):
        super(). __init__ (char_name, char_description)

    def set_gift_item(self, gift_item):
        self.gift_item = gift_item

    def get_gift_item(self):
        return self.gift_item
    
    def gift(self, give_gift):
        if give_gift == self.gift_item:
            print(self.name + " accepts your " + give_gift + " with a big smile.")
        else:
            print(self.name + " politely declines your " + give_gift + ".")

