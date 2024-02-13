from RPS_SimpleGame import RPS_SimpleGame
import random

class RPS_MultipleGame:
    def __init__(self, player_name):
        self.game = RPS_SimpleGame()
        self.history = []
        self.player_name = player_name 
    
    def play_game(self):
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

        # Affichage de nos résultats
        if result == 0:
            print(f"Egalité ! L'ordinateur a également choisi {computer_choice}.")
        elif result == 1:
            print(f"{self.player_name} gagne ce duel ! L'ordinateur avait choisi {computer_choice}.")
        else: 
            print(f"L'ordinateur gagne ! il avait choisi {computer_choice}.")

    def get_history(self):
        return self.history
    