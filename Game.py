class Game:
    def __init__(self,rase,attack,health,mana):
        self.rase = rase
        self.attack = attack
        self.health = health
        self.mana = mana

    def hero(self):
        return f'{self.rase} {self.attack} {self.health} {self.mana}'


    def power(self,type_attack):
        if type_attack == "first":
            self.strength = self.strength + 50
        elif type_attack == "second":
            self.strength = self.strength + 100
        elif type_attack == "third":
            self.strength = self.strength + 150

    def plate(self,type_plate):
        if type_plate == "epic":
            self.health += 60
        elif type_plate == "legend":
            self.health += 500
        elif type_plate == "mythic":
            self.health += 1000



    def magic(self,type_magic):
        if type_magic == "one":
            self.mana += 60
        elif type_magic == "two":
            self.mana += 120
        elif type_magic == "three":
            self.mana += 180

class Warrior(Game):

    def __init__(self,rase,attack=150,health=200,mana=0):
        super().__init__(rase,attack,health,mana)
        self.strength = 70

    def set_sword(self,new_sword):
        if new_sword == "onehanded blade":
            self.attack += 200
            self.strength += 100
        elif new_sword == "twohanded blade":
            self.attack += 300
            self.strength += 150
        elif new_sword == "mega axe":
            self.attack += 500
            self.strength += 200
            self.health += 100


class Marksman(Game):
    def __init__(self,rase,attack=80,health=150,mana=90):
        super().__init__(rase,attack,health,mana)
        self.agility = 40
        self.strength = 20


    def hero(self):
        return f'{self.rase} {self.attack} {self.health} {self.mana} {self.agility}'


    def set_crossbow(self,new_crossbow):
        if new_crossbow == "speed":
            self.agility += 100
        elif new_crossbow == "megaspeed":
            self.agility += 200
        elif new_crossbow == "extraspeed":
            self.agility += 300




gamer1 = Warrior(rase="orc")
print(gamer1.hero())
gamer1.plate("mythic")
gamer1.set_sword("mega axe")
gamer1.power("third")
print(gamer1.hero())

gamer2 = Marksman("Human")
print(gamer2.hero())
gamer2.plate("mythic")
gamer2.set_crossbow("extraspeed")
gamer2.power("third")
gamer2.magic("three")
print(gamer2.hero())