"""
Ce module 'script_multiple.py' fournit une interface pour lancer une partie 
du jeu Pierre-Papier-Ciseaux avec plusieurs joueurs ou contre l'ordinateur, en utilisant le 
module RPS_MultipleGame. Il permet de démarrer une partie, de recevoir les choix des joueurs, 
et d'afficher les résultats.

Il démontre l'utilisation des importations, des fonctions, et de la gestion des chemins 
d'accès au sein d'un projet Python plus vaste.
"""

from RPS_MultipleGame import RPS_MultipleGame


def main():
    """
    Fonction principale pour exécuter le jeu multiple.

    Cette fonction crée une instance du jeu Pierre-Papier-Ciseaux avec plusieurs joueurs,
    initie le jeu, reçoit les choix des joueurs et affiche le résultat final.

    Returns:
        None
    """
    game = RPS_MultipleGame()
    player_id = input("Enter your player ID: ")

    while True:
        # Load and display history from CSV
        game.load_history()
        if game.history:
            game.load_history()

        # Play a game
        game.play_game(player_id)

        # Ask if player wants to play again
        play_again = input("Voulez-vous jouer à nouveau ? (oui/non) ").lower()
        if play_again != "oui":
            break


if __name__ == "__main__":
    main()
