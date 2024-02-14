from RPS_MultipleGame import RPS_MultipleGame

def main():
    game = RPS_MultipleGame()
    player_id = input("Enter your player ID: ")

    while True:
        # Charger et afficher l'historique depuis le CSV
        game.load_history()  
        if game.history:
            game.load_history()

        # Jouer une partie
        game.play_game(player_id)

        # Demander si le joueur veut rejouer
        play_again = input("Voulez-vous jouer à nouveau ? (oui/non) ").lower()
        if play_again != 'oui':
            break

if __name__ == "__main__":
    main()
