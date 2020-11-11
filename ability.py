import random
class Ability:
    def __init__(self, name, maxAttack):
        self.name=name
        self.maxAttack=maxAttack
    def attack(self):
      random_value=random.randint(0, self.maxAttack)
      return random_value