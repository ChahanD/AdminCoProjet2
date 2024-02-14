"""
Module for executing multiple sessions of Rock-Paper-Scissors game.
"""

from RPS_MultipleGame import RPS_MultipleGame

def main():
    """
    Main function to execute the game with multiple sessions.
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
        if play_again != 'oui':
            break

if __name__ == "__main__":
    main()
