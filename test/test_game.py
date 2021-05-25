import unittest
import sys
sys.path.append("..")
from game import *


class test_game(unittest.TestCase):
    def test_game_is_instance_game(self):
        Game1 = Puissance_4_1(3,4)
        self.assertIsInstance(Game1, Puissance_4_1)



if __name__ == '__main__':
    unittest.main()