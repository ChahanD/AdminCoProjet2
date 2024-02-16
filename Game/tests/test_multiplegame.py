"""
Tests unitaires pour la classe RPS_MultipleGame.
"""

import unittest
import os
import sys
from unittest.mock import patch
from unittest.mock import mock_open

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from RPS_Tools.RPS_MultipleGame import RPS_MultipleGame


class TestRPSMultipleGame(unittest.TestCase):
    """Tests unitaires pour la classe RPS_MultipleGame."""

    def setUp(self):
        """Préparation avant chaque test."""
        self.game = RPS_MultipleGame(csv_file="rps_history.csv")

    def test_load_history_no_file(self):
        # Test loading history when no file exists
        with patch("os.path.exists", return_value=False):
            self.game.load_history()
            self.assertEqual(self.game.history, [])

    def test_play_game_with_correct_input(self):
        # Test playing a game with correct user input
        with patch("builtins.input", return_value="R"):
            with patch("random.choice", return_value="S"):
                self.game.play_game("TestPlayer")
                self.assertGreater(len(self.game.history), 0)

    def test_play_game_with_incorrect_then_correct_input(self):
        # Test playing a game with incorrect input followed by correct input
        with patch("builtins.input", side_effect=["X", "R"]):
            with patch("random.choice", return_value="S"):
                self.game.play_game("TestPlayer")
                self.assertGreater(len(self.game.history), 0)

    def test_update_csv(self):
        # Test if CSV file is updated correctly
        game_details = {
            "PlayerID": "TestPlayer",
            "PlayerChoice": "R",
            "ComputerChoice": "S",
            "Result": 1,
        }
        with patch("builtins.open", mock_open()) as mocked_file:
            self.game.update_csv(game_details)
            self.assertTrue(mocked_file.called)

    def test_show_result(self):
        # Test if the correct result is displayed
        with patch("builtins.print") as mocked_print:
            self.game.show_result("R", "S", 1)
            mocked_print.assert_called_with(
                "Joueur: R, Ordinateur: S, Résultat: Le joueur gagne"
            )

    def test_load_history_with_file(self):
        # Mock data for testing
        mock_data = [
            {
                "PlayerID": "Player1",
                "PlayerChoice": "R",
                "ComputerChoice": "S",
                "Result": 1,
            },
            {
                "PlayerID": "Player2",
                "PlayerChoice": "S",
                "ComputerChoice": "R",
                "Result": 2,
            },
        ]
        with patch("os.path.exists", return_value=True):
            with patch("csv.DictReader", return_value=mock_data):
                self.game.load_history()
                self.assertEqual(self.game.history, mock_data)

    def test_csv_file_creation(self):
        # Mocking open to simulate file creation
        with patch("builtins.open", mock_open()):
            self.game.update_csv({})
            self.assertTrue(os.path.exists(self.game.csv_file))

    def test_repeated_invalid_choices(self):
        with patch("builtins.input", side_effect=["X", "Y", "Z", "R"]):
            choice = self.game.get_user_choice()
            self.assertEqual(choice, "R")

    def test_game_result_scenarios(self):
        # Test for different game results
        with patch("random.choice", side_effect=["R", "R", "R"]):
            self.game.play_game("TestPlayer", "R")  # Tie
            self.game.play_game("TestPlayer", "P")  # Player wins
            self.game.play_game("TestPlayer", "S")  # Computer wins
            self.assertEqual(self.game.history[-3]["Result"], 0)
            self.assertEqual(self.game.history[-2]["Result"], 1)
            self.assertEqual(self.game.history[-1]["Result"], 2)


if __name__ == "__main__":
    unittest.main()
