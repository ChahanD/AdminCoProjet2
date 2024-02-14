import unittest
from RPS_MultipleGame import RPS_MultipleGame
import os

class TestRPSMultipleGame(unittest.TestCase):
    def setUp(self):
        self.game = RPS_MultipleGame()
        self.player_id = 'TestPlayer'

    def test_play_game_updates_history(self):
        # Simuler un choix de joueur pour éviter l'interaction utilisateur
        simulated_player_choice = 'R'
        self.game.play_game(self.player_id, simulated_player_choice)
        self.assertGreater(len(self.game.history), 0)

    def test_csv_file_creation(self):
        self.game.play_game(self.player_id)
        self.assertTrue(os.path.exists(self.game.csv_file))

    def tearDown(self):
        if os.path.exists(self.game.csv_file):
            os.remove(self.game.csv_file)

    # Ajouter d'autres tests si nécessaire, par exemple pour vérifier le contenu du fichier CSV

if __name__ == '__main__':
    unittest.main()