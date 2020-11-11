import random
from ability import *
from armor import *
class Hero:
    def __init__(self, name, starting_health=100):
        self.name=name
        self.starting_health=starting_health
        self.current_health=starting_health
        self.abilities = list()
        self.armors = list()
    def fight(self, opponent):
        if self.abilities is not list() and opponent.abilities is not list():
            while self.is_alive() and opponent.is_alive():
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
            if not self.is_alive() and not opponent.is_alive():
                print("Draw!")
            elif (self.is_alive()):
                print (self.name,"Wins!")
            else: 
                print (opponent.name,"Wins!")
        else:
            print("Draw!")
        # heros=[self.name, opponent.name]
        # print(random.choice(heros),"wins!")
    def add_ability(self, ability):
        self.abilities.append(ability)
    def attack(self):
        total_damage=0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage
    def add_armor(self, armor):
        self.armors.append(armor)
    def defend(self):
        totalBlock=0
        for armor in self.armors:
            totalBlock+=armor.block()
        return totalBlock
    def take_damage(self, damage):
        self.current_health-=(damage-self.defend())
    def is_alive(self):  
        if self.current_health>0:
            return True
        else:
            return False

# Testing ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
hero1 = Hero("Wonder Woman")
hero2 = Hero("Dumbledore")
ability1 = Ability("Super Speed", 300)
ability2 = Ability("Super Eyes", 130)
ability3 = Ability("Wizard Wand", 80)
ability4 = Ability("Wizard Beard", 20)
hero1.add_ability(ability1)
hero1.add_ability(ability2)
hero2.add_ability(ability3)
hero2.add_ability(ability4)
hero1.fight(hero2)