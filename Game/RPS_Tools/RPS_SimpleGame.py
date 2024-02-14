"""
Module pour la classe RPS_SimpleGame qui gère la logique du jeu Pierre/Feuille/Ciseaux.
"""

import random

class RPS_SimpleGame:
    """
    Classe pour jouer à Pierre/Feuille/Ciseaux.
    """

    def simple_game_two_players(self, player1choice, player2choice):
        """
        Détermine le gagnant entre deux joueurs.
        :param player1choice: Choix du joueur 1 ('R', 'P', 'S')
        :param player2choice: Choix du joueur 2 ('R', 'P', 'S')
        :return: 0 pour égalité, 1 si joueur 1 gagne, 2 si joueur 2 gagne
        """
        if player1choice == player2choice:
            return 0
        if (player1choice == 'R' and player2choice == 'S') or \
           (player1choice == 'S' and player2choice == 'P') or \
           (player1choice == 'P' and player2choice == 'R'):
            return 1
        return 2
    
    def simple_game_one_player(self, player1choice):
        """
        Joue une partie contre l'ordinateur.
        :param player1choice: Choix du joueur ('R', 'P', 'S')
        :return: 0 pour égalité, 1 si joueur gagne, 2 si ordinateur gagne
        """
        computer_choice = random.choice(['R', 'P', 'S'])
        result = self.simple_game_two_players(player1choice, computer_choice)
        return result, computer_choice
