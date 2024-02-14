import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from RPS_Tools.RPS_MultipleGame import RPS_MultipleGame
def test_game():
    game = RPS_MultipleGame()
    while True:
        game.play_game()
        if input("Relancer une partie? (O/N): ").upper() != 'O':
            break
    game.show_history()

if __name__ == "__main__":
    test_game()