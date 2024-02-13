from RPS_SimpleGame import RPS_SimpleGame
import random

class RPS_MultipleGame:
    """
    Classe permettant de jouer plusieurs parties de Pierre/Feuille/Ciseaux contre l'ordinateur.
    Elle garde un historique des parties jouées, y compris les choix et les résultats.
    """
    def __init__(self, player_name):
        """
        Initialise l'instance de RPS_MultipleGame.

        :param player_name: Nom du joueur humain.
        """
        self.game = RPS_SimpleGame()
        self.history = []
        self.player_name = player_name 
    
    def play_game(self, player_choice):
        """
        Permet au joueur de jouer une partie contre l'ordinateur et enregistre le résultat.
        """
         # Affichage de l'historique des parties précédentes
        if self.history:
            print("Historique des parties précédentes:")
            for game in self.history:
                print(game)
        while True : 
            player_choice = input(f"{self.player_name}, Veuillez choisir [R]ock, [P]aper, [S]cissors: ").upper()
            if player_choice not in ['R', 'P', 'S']:
                print("Choix invalide")
                return
            computer_choice = random.choice(['R', 'P', 'S'])
            result = self.game.SimplegameTwoPlayers(player_choice, computer_choice)

            # partie qui s'occupe de l'historique des parties
            game_record = {
                'player_name': self.player_name,
                'player_choice': player_choice,
                'computer_choice': computer_choice,
                'result': result
            }
            self.history.append(game_record)
            replay = input("Voulez vous rejouer une partie? (Oui/Non)").lower()
            if replay != "oui":
                break


        # Affichage de nos résultats
        if result == 0:
            print(f"Egalité ! L'ordinateur a également choisi {computer_choice}.")
        elif result == 1:
            print(f"{self.player_name} gagne ce duel ! L'ordinateur avait choisi {computer_choice}.")
        else: 
            print(f"L'ordinateur gagne ! il avait choisi {computer_choice}.")

    def get_history(self):
        """
        Retourne l'historique des parties jouées.

        :return: Liste des enregistrements de chaque partie jouée.
        """
        return self.history
    