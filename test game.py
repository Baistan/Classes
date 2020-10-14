from Game import Game,Warrior,Marksman
from unittest import TestCase

class TestGame(TestCase):

    def test_kind_of_weapon(self):
        new_warrior = Warrior("Orc")
        new_warrior.set_sword("onehanded blade")
        self.assertEqual(new_warrior.strength,170)

    def test_kind_of_armor(self):
        new_warrior = Warrior("Human")
        new_warrior.plate("legend")
        self.assertEqual(new_warrior.health,700)

    def test_kind_of_power(self):
        new_warrior = Warrior("Orc")
        new_warrior.power("second")
        self.assertEqual(new_warrior.strength,170)

    def test_kind_of_speed(self):
        new_warrior = Marksman("Orc")
        new_warrior.set_crossbow("megaspeed")
        self.assertEqual(new_warrior.health,150)

    def test_how_is_mana(self):
        new_warrior = Warrior("Human")
        new_warrior.magic("three")
        self.assertEqual(new_warrior.health,200)

    def test_kind_of_arrmor(self):
        new_warrior = Warrior("Human")
        new_warrior.plate("epic")
        self.assertEqual(new_warrior.health,260)

    def test_kind_of_armorr(self):
        new_warrior = Warrior("Human")
        new_warrior.plate("mythic")
        self.assertEqual(new_warrior.health,1200)

    def test_kind_of_poower(self):
        new_warrior = Warrior("Orc")
        new_warrior.power("first")
        self.assertEqual(new_warrior.strength,120)

    def test_kind_of_powerr(self):
        new_warrior = Warrior("Orc")
        new_warrior.power("third")
        self.assertEqual(new_warrior.strength,220)

    def test_kind_of_speeed(self):
        new_warrior = Marksman("Orc")
        new_warrior.set_crossbow("extraspeed")
        self.assertEqual(new_warrior.agility,340)



