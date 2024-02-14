from RPS_SimpleGame import RPS_SimpleGame
import random
class RPS_MultipleGame:
    def __init__(self):
        self.simple_game = RPS_SimpleGame()
        self.history = []

    def play_game(self):
        if self.history:  # Vérifie si l'historique n'est pas vide
            print("Historique des parties précédentes :")
            self.show_history()
            print("\nNouvelle partie :\n")
        
        player_choice = self.get_user_choice()
        computer_choice = random.choice(['R', 'P', 'S'])
        result = self.simple_game.SimplegameTwoPlayers(player_choice, computer_choice)
        self.history.append({'Player': player_choice, 'Computer': computer_choice, 'Result': result})
        self.show_result(player_choice, computer_choice, result)

    def get_user_choice(self):
        choice = ''
        while choice not in ['R', 'P', 'S']:
            choice = input("Choose Rock (R), Paper (P), or Scissors (S): ").upper()
        return choice

    def show_result(self, player_choice, computer_choice, result):
        result_text = "Tie" if result == 0 else "Player Wins" if result == 1 else "Computer Wins"
        print(f"Le joueur a joué: {player_choice}, L'ordinateur a joué: {computer_choice}, Le résultat est : {result_text}")

    def show_history(self):
        print("\nGame History:")
        for game in self.history:
            result_text = "Egalité" if game['Result'] == 0 else "Joueur gagne !" if game['Result'] == 1 else "Dommage l'ordinateur a gagné"
            print(f"Le joueur a joué: {game['Player']}, L'ordinateur a joué: {game['Computer']}, Le résultat est : {result_text}")

