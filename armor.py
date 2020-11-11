import random
class Armor:
    def __init__(self, name, maxBlock):
        self.name=name
        self.maxBlock=maxBlock
    def block(self):
      random_value=random.randint(0, self.maxBlock)
      return random_value