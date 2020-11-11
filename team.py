from hero import *
class Team:
    def __init__(self, name):
        self.name = name
        self.heroes = list()
    def remove_hero(self, name):
        foundHero=False
        for hero in self.heroes:
            if hero.name==name:
                self.heroes.remove(hero)
                foundHero = True
        if not foundHero:
            return 0
    def view_all_heroes(self):
        for hero in self.heroes:
            print(hero.name)
    def add_hero(self, hero):
        self.heroes.append(hero)
    def stats(self):
        '''Print team statistics'''
        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f"{hero.name} Kill/Deaths:{kd}")
    def revive_heroes(self, health=100):
        for hero in self.heroes:
            hero.current_health=hero.starting_health
    def attack(self, other_team):
        ''' Battle each team against each other.'''

        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents)> 0:
            t1hero=random.choice(living_heroes)
            t2hero=random.choice(living_opponents)
            if t1hero.fight(t2hero) == 1:
                living_opponents.remove(t2hero)
            elif t1hero.fight(t2hero) == 2:
                living_heroes.remove(t1hero)
            else:
                living_opponents.remove(t2hero)
                living_heroes.remove(t1hero)