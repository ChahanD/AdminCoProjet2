"""
Ce module 'script_simple_game' implémente un script pour lancer une partie simple 
du jeu Pierre-Papier-Ciseaux en utilisant le module RPS_SimpleGame.
"""

import os
import sys

# Ajustez ce chemin selon la structure de votre projet.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from RPS_Tools.RPS_SimpleGame import RPS_SimpleGame


def play_rps_game():
    """
    Fonction principale pour exécuter le jeu.
    """
    game = RPS_SimpleGame()
    # Demander à l'utilisateur s'il veut jouer contre un autre joueur ou l'ordinateur.
    mode = input(
        "Voulez-vous jouer contre [A]nother player ou [C]omputer? (A/C): "
    ).upper()

    # Vérification de la validité de la réponse de l'utilisateur.
    if mode not in ["A", "C"]:
        print("Mode de jeu invalide.")
        return
    # Si l'utilisateur veut jouer contre l'ordinateur.

    if mode == "C":
        # Demander le choix de l'utilisateur.
        player_choice = input("Choisissez [R]ock, [P]aper, ou [S]cissors: ").upper()
        # Vérifier si le choix de l'utilisateur est valide.
        if player_choice not in ["R", "P", "S"]:
            print("Choix invalide.")
            return

        # Obtenir le résultat du jeu et le choix de l'ordinateur.
        result, computer_choice = game.simple_game_one_player(player_choice)

        # Afficher le choix de l'ordinateur.
        print(f"L'ordinateur a joué: {computer_choice}")
    # Si l'utilisateur veut jouer contre un autre joueur.
    else:
        # Demander les choix des deux joueurs.
        player1_choice = input(
            "Joueur 1, choisissez [R]ock, [P]aper, ou [S]cissors: "
        ).upper()
        player2_choice = input(
            "Joueur 2, choisissez [R]ock, [P]aper, ou [S]cissors: "
        ).upper()

        # Vérifier si les choix des joueurs sont valides.
        if player1_choice not in ["R", "P", "S"] or player2_choice not in [
            "R",
            "P",
            "S",
        ]:
            print("Choix invalide.")
            return

        # Obtenir le résultat du jeu entre les deux joueurs.
        result = game.simple_game_two_players(player1_choice, player2_choice)

    # Affichage du résultat du jeu.
    if result == 0:
        print("Égalité!")
    elif result == 1:
        print("Joueur 1 gagne!" if mode == "A" else "Vous gagnez!")
    else:
        print("Joueur 2 gagne!" if mode == "A" else "L'ordinateur gagne!")


# Point d'entrée principal pour exécuter le jeu si ce fichier est exécuté directement.
if __name__ == "__main__":
    play_rps_game()
