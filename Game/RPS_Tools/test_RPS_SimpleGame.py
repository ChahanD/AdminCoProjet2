from RPS_SimpleGame import RPS_SimpleGame
def play_rps_game():
    game = RPS_SimpleGame()
    mode = input("Voulez-vous jouer contre [A]nother player ou [C]omputer? (A/C): ").upper()

    if mode not in ["A", "C"]:
        print("Mode de jeu invalide.")
        return

    if mode == "C":
        player_choice = input("Choisissez [R]ock, [P]aper, ou [S]cissors: ").upper()
        if player_choice not in ['R', 'P', 'S']:
            print("Choix invalide.")
            return
        result, computer_choice = game.SimplegameOnePlayer(player_choice)
        print(f"L'ordinateur a joué: {computer_choice}")
    else:
        player1_choice = input("Joueur 1, choisissez [R]ock, [P]aper, ou [S]cissors: ").upper()
        player2_choice = input("Joueur 2, choisissez [R]ock, [P]aper, ou [S]cissors: ").upper()
        if player1_choice not in ['R', 'P', 'S'] or player2_choice not in ['R', 'P', 'S']:
            print("Choix invalide.")
            return
        result = game.SimplegameTwoPlayers(player1_choice, player2_choice)

    if result == 0:
        print("Égalité!")
    elif result == 1:
        print("Joueur 1 gagne!" if mode == "A" else "Vous gagnez!")
    else:
        print("Joueur 2 gagne!" if mode == "A" else "L'ordinateur gagne!")

if __name__ == "__main__":
    play_rps_game()
