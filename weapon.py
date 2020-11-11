import random
from ability import *
class Weapon(Ability):
    def attack(self):
        random_value=random.randint(self.maxAttack//2, self.maxAttack)
        return random_value