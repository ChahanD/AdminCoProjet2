import os
import sys

# Ajout du chemin du dossier parent au sys.path pour permettre l'importation de modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from RPS_Tools.RPS_MultipleGame import RPS_MultipleGame

def test_game():
    """
    Fonction pour tester le jeu RPS_MultipleGame.
    Permet à l'utilisateur de jouer plusieurs parties et affiche l'historique à la fin.
    """
    game = RPS_MultipleGame()
    while True:
        game.play_game()
        if input("Relancer une partie? (O/N): ").upper() != 'O':
            break
    game.show_history()

if __name__ == "__main__":
    test_game()
