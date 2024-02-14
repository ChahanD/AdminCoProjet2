import csv
import os
import random
from RPS_SimpleGame import RPS_SimpleGame

class RPS_MultipleGame:
    def __init__(self, csv_file='rps_history.csv'):
        self.simple_game = RPS_SimpleGame()
        self.csv_file = csv_file
        self.load_history()

    def load_history(self):
        if os.path.exists(self.csv_file):
            with open(self.csv_file, mode='r', newline='') as file:
                reader = csv.DictReader(file)
                self.history = [row for row in reader]
        else:
            self.history = []

    def play_game(self, player_id, player_choice=None):
        if player_choice is None:
            player_choice = self.get_user_choice()
        else:
            # Simule le choix du joueur sans demander d'entrée
            assert player_choice in ['R', 'P', 'S'], "Invalid choice"

        computer_choice = random.choice(['R', 'P', 'S'])
        result = self.simple_game.SimplegameTwoPlayers(player_choice, computer_choice)
        
        game_details = {
            'PlayerID': player_id,
            'PlayerChoice': player_choice,
            'ComputerChoice': computer_choice,
            'Result': result
        }
        self.history.append(game_details)
        self.update_csv(game_details)
        self.show_result(player_choice, computer_choice, result)

    def update_csv(self, game_details):
        with open(self.csv_file, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['PlayerID', 'PlayerChoice', 'ComputerChoice', 'Result'])
            if file.tell() == 0:  # If file is empty, write header
                writer.writeheader()
            writer.writerow(game_details)

    def get_user_choice(self):
        choice = ''
        while choice not in ['R', 'P', 'S']:
            choice = input("Choose Rock (R), Paper (P), or Scissors (S): ").upper()
        return choice

    def show_result(self, player_choice, computer_choice, result):
        result_text = "Draw" if result == 0 else "Player wins" if result == 1 else "Computer wins"
        print(f"Player: {player_choice}, Computer: {computer_choice}, Result: {result_text}")
