import random
from ability import *
class Hero:
    def __init__(self, name, starting_health=100):
        self.name=name
        self.starting_health=starting_health
        self.current_health=starting_health
    def fight(self, opponent):
        heros=[self.name, opponent.name]
        print(random.choice(heros),"wins!")

# Testing ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
hero1=Hero("Grace Hopper", 200)
hero2=Hero("bob", 100)
hero1.fight(hero2)
ability = Ability("Debugging Ability", 20)
print(ability.name)
print(ability.attack())