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

class Wizzard(Game):
    def __init__(self,rase,attack=50,health=130,mana=150):
        super().__init__(rase,attack,health,mana)
        self.magic_attack = 30
        self.strength = 40


    def hero(self):
        return f'{self.rase} {self.attack} {self.health} {self.mana} {self.magic_attack}'


    def set_staff(self,new_staff):
        if new_staff == "bronze":
            self.magic_attack += 100
        elif new_staff == "silver":
            self.magic_attack += 200
        elif new_staff == "gold":
            self.magic_attack += 300


class Gnome(Game):
    def __init__(self,rase,attack=150,health=230,mana=100):
        super().__init__(rase,attack,health,mana)
        self.crit_attack = 30
        self.strength = 55


    def hero(self):
        return f'{self.rase} {self.attack} {self.health} {self.mana} {self.crit_attack}'


    def set_hammer(self,new_hammer):
        if new_hammer == "invincible":
            self.crit_attack += 120
        elif new_hammer == "fearless":
            self.crit_attack += 220
        elif new_hammer == "savage":
            self.crit_attack += 320





gamer1 = Warrior(rase="Orc")
gamer1.plate("mythic")
gamer1.set_sword("mega axe")
gamer1.power("third")
print(gamer1.hero())

gamer2 = Marksman("Human")
gamer2.plate("mythic")
gamer2.set_crossbow("extraspeed")
gamer2.power("third")
gamer2.magic("three")
print(gamer2.hero())

gamer3 = Wizzard(rase="Elf")
gamer3.plate("legend")
gamer3.set_staff("silver")
gamer3.power("second")
gamer3.magic("three")
print(gamer3.hero())

gamer4 = Gnome(rase="Dwarf")
gamer4.plate("mythic")
gamer4.set_hammer("savage")
gamer4.power("third")
gamer4.magic("one")
print(gamer4.hero())


class Fight():
    def __init__(self, health, attack):
        self.health = health
        self.attack = attack

    def __add__(self, other):
        res = self.health - other.attack
        return res

end_fight1 = Fight(health=gamer1.health,attack=gamer1.attack)
end_fight2 = Fight(health=gamer2.health,attack=gamer2.attack)


fight1 = Fight(gamer1.health,gamer1.attack)
fight2 = Fight(gamer2.health,gamer2.attack)
sim1 = fight1 + fight2
print("Оставшееся здоровье Орка",sim1)
sim2 = fight2 + fight1
print("Оставшееся здоровье Человека",sim2)

res1, res2 = 1,1
while res1 <= 0 or res2 <=0:
    res1 = end_fight1 + end_fight2
    res2 = end_fight2 + end_fight1
    print(res1,res2)
    end_fight1 = Fight(res1,gamer1.attack)
    end_fight2 = Fight(res2,gamer2.attack)
    if res1 == 0 and res2 != 0:
        print("Выиграл Орк","Запас жизни=",res2)
    else:
        print("Выиграл Человек", "Запас жизни=", res1)

fight3 = Fight(gamer3.health,gamer3.attack)
fight4 = Fight(gamer4.health,gamer4.attack)
sim3 = fight3 + fight4
print("Оставшееся здоровье Эльфа")
sim4 = fight4 + fight3
print("Оставшееся здоровье Гнома")

# res1, res2 = 1,1
# while res1 <= 0 or res2 <=0:
#     res1 = end_fight1 + end_fight2
#     res2 = end_fight2 + end_fight1
#     print(res1,res2)
#     end_fight1 = Fight(res1,gamer1.attack)
#     end_fight2 = Fight(res2,gamer2.attack)
#     if res1 == 0 and res2 != 0:
#         print("Выиграл Орк","Запас жизни=",res2)
#     else:
#         print("Выиграл Человек", "Запас жизни=", res1)
















# fight_one = Fight_for_armor(gamer1.armor,gamer1.attack)
# last_armor_one = gamer1.armor - fight_one
# print("Броня Орка снижена на",last_armor_one)
# fight_two = Fight_for_armor(gamer2.armor,gamer2.attack)
# last_armor_two = gamer2.armor - fight_two
# print("Броня Человека снижена на",last_armor_two)
# sim_one = fight_one + fight_two
# print("Оставшееся здоровье Орка",sim1)
# sim_two = fight_two + fight_one
# print("Оставшееся здоровье Человека",sim2)
#
# while gamer1.armor != 0 or gamer2.armor != 0:
#     simulation1 += 1
#     print(simulation1)

