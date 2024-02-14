from RPS_SimpleGame import RPS_SimpleGame
import random

class RPS_MultipleGame:
    """Classe pour jouer plusieurs parties de Pierre-Papier-Ciseaux contre l'ordinateur."""

    def __init__(self):
        """Initialise le jeu avec un jeu simple et un historique vide."""
        self.simple_game = RPS_SimpleGame()
        self.history = []

    def play_game(self):
        """
        Joue une partie de Pierre-Papier-Ciseaux.
        Affiche l'historique des parties précédentes s'il y en a.
        Enregistre et affiche le résultat de la partie actuelle.
        """
        if self.history:
            print("Historique des parties précédentes :")
            self.show_history()
            print("\nNouvelle partie :\n")
        
        player_choice = self.get_user_choice()
        computer_choice = random.choice(['R', 'P', 'S'])
        result = self.simple_game.SimplegameTwoPlayers(player_choice, computer_choice)
        self.history.append({'Player': player_choice, 'Computer': computer_choice, 'Result': result})
        self.show_result(player_choice, computer_choice, result)

    def get_user_choice(self):
        """
        Demande et valide le choix de l'utilisateur.
        :return: Le choix de l'utilisateur ('R', 'P', 'S')
        """
        choice = ''
        while choice not in ['R', 'P', 'S']:
            choice = input("Choisissez Pierre (R), Papier (P), ou Ciseaux (S) : ").upper()
        return choice

    def show_result(self, player_choice, computer_choice, result):
        """
        Affiche le résultat de la partie actuelle.
        :param player_choice: Choix du joueur
        :param computer_choice: Choix de l'ordinateur
        :param result: Résultat de la partie
        """
        result_text = "Egalité" if result == 0 else "Joueur gagne" if result == 1 else "Ordinateur gagne"
        print(f"Le joueur a joué : {player_choice}, L'ordinateur a joué : {computer_choice}, Résultat : {result_text}")

    def show_history(self):
        """Affiche l'historique des parties jouées."""
        print("\nHistorique des parties :")
        for game in self.history:
            result_text = "Egalité" if game['Result'] == 0 else "Joueur gagne" if game['Result'] == 1 else "Ordinateur gagne"
            print(f"Le joueur a joué : {game['Player']}, L'ordinateur a joué : {game['Computer']}, Résultat : {result_text}")
