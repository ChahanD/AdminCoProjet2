"""
Tests unitaires pour la classe RPS_SimpleGame.
"""

import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from RPS_Tools.RPS_SimpleGame import RPS_SimpleGame


class TestRPSSimpleGame(unittest.TestCase):
    """Tests unitaires pour la classe RPS_SimpleGame."""

    def setUp(self):
        """Préparation avant chaque test."""
        self.game = RPS_SimpleGame()

    def test_game_logic(self):
        """Teste la logique du jeu."""
        self.assertEqual(self.game.simple_game_two_players("R", "S"), 1)
        self.assertEqual(self.game.simple_game_two_players("P", "R"), 1)
        self.assertEqual(self.game.simple_game_two_players("S", "P"), 1)
        self.assertEqual(self.game.simple_game_two_players("R", "R"), 0)


if __name__ == "__main__":
    unittest.main()
