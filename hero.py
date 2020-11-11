import random
from ability import *
from armor import *
from weapon import *
class Hero:
    def __init__(self, name, starting_health=100):
        self.name=name
        self.starting_health=starting_health
        self.current_health=starting_health
        self.abilities = list()
        self.armors = list()
        self.deaths = 0
        self.kills = 0
    def fight(self, opponent):
        if self.abilities is not list() and opponent.abilities is not list():
            while self.is_alive() and opponent.is_alive():
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
            if not self.is_alive() and not opponent.is_alive():
                print("Draw!")
            elif (self.is_alive()):
                print (self.name,"Wins!")
                self.add_kill(1)
                opponent.add_death(1)
                return 1
            else: 
                print (opponent.name,"Wins!")
                opponent.add_kill(1)
                self.add_death(1)
                return 2
        else:
            print("Draw!")
            return 3
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
    def add_weapon(self, weapon):
        self.abilities.append(weapon)
    def add_kill(self, num_kills):
        self.kills += num_kills
    def add_death(self, num_deaths):
        self.deaths += num_deaths
# Testing ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
hero = Hero("Wonder Woman")
weapon = Weapon("Lasso of Truth", 90)
hero.add_weapon(weapon)
print(hero.attack())