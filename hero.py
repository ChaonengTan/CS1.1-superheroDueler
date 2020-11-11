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
        heros=[self.name, opponent.name]
        print(random.choice(heros),"wins!")
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
hero = Hero("Grace Hopper", 200)
hero.take_damage(150)
print(hero.is_alive())
hero.take_damage(15000)
print(hero.is_alive())