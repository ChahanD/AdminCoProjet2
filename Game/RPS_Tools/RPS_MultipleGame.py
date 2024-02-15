"""
Module pour le jeu Pierre-Feuille-Ciseaux avec gestion de multiples parties.
"""

import csv
import os
import random
from RPS_SimpleGame import RPS_SimpleGame

class RPS_MultipleGame:
    """
    Classe gérant plusieurs parties de Pierre-Feuille-Ciseaux avec historique.
    """

    def __init__(self, csv_file='rps_history.csv'):
        """
        Initialise le jeu avec un fichier CSV spécifié pour l'historique.
        """
        self.simple_game = RPS_SimpleGame()
        self.csv_file = csv_file
        self.load_history()

    def load_history(self):
        """
        Charge l'historique des parties à partir du fichier CSV.
        """
        if os.path.exists(self.csv_file):
            with open(self.csv_file, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.history = list(reader)
        else:
            self.history = []

    def play_game(self, player_id, player_choice=None):
        """
        Joue une partie et met à jour l'historique et le fichier CSV.
        """
        if player_choice is None or not player_choice in ['R', 'P', 'S']:
            player_choice = self.get_user_choice()

        computer_choice = random.choice(['R', 'P', 'S'])
        result = self.simple_game.simple_game_two_players(player_choice, computer_choice)

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
        """
        Met à jour le fichier CSV avec les détails de la dernière partie.
        """
        with open(self.csv_file, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['PlayerID', 'PlayerChoice', 'ComputerChoice', 'Result'])
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(game_details)

    def get_user_choice(self):
        """
        Obtient le choix de l'utilisateur pour le jeu.
        """
        choice = ''
        while choice not in ['R', 'P', 'S']:
            choice = input("Choisissez Pierre (R), Papier (P), ou Ciseaux (S): ").upper()
        return choice

    def show_result(self, player_choice, computer_choice, result):
        """
        Affiche le résultat de la partie.
        """
        result_text = "Égalité" if result == 0 else "Le joueur gagne" if result == 1 else "L'ordinateur gagne"
        print(f"Joueur: {player_choice}, Ordinateur: {computer_choice}, Résultat: {result_text}")
