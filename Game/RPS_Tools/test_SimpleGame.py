import unittest
from RPS_SimpleGame import RPS_SimpleGame

class TestRPSSimpleGame(unittest.TestCase):
    def setUp(self):
        self.game = RPS_SimpleGame()

    def test_game_logic(self):
        self.assertEqual(self.game.SimplegameTwoPlayers('R', 'S'), 1)
        self.assertEqual(self.game.SimplegameTwoPlayers('P', 'R'), 1)
        self.assertEqual(self.game.SimplegameTwoPlayers('S', 'P'), 1)
        self.assertEqual(self.game.SimplegameTwoPlayers('R', 'R'), 0)

    # Vous pouvez ajouter plus de tests pour couvrir tous les cas possibles

if __name__ == '__main__':
    unittest.main()