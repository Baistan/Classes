class Human:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

class Planet:
    """hier must be decsription of class"""

    count = 0


    def __init__(self,name,population=None):
        self.name = name
        self.population = population or []
        Planet.count += 1

    def __str__(self):
        return self.name

    def add_human(self,human):
        print(f'Welcome to {self.name}, {human}')
        self.population.append(human)

planet = Planet("Earth")
planet1 = Planet("Mars")
human = Human("Bob")
human1 = Human("Kevin")
planet.add_human(human)
planet1.add_human(human1)

