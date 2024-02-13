from RPS_MultipleGame import RPS_MultipleGame

def interactive_test():
    player_name = input("Entrez votre nom de joueur: ")
    game = RPS_MultipleGame(player_name)

    while True:
        print("\nNouvelle partie de Pierre/Feuille/Ciseaux")
        player_choice = input(f"{player_name}, choisissez [R]ock, [P]aper, ou [S]cissors: ").upper()
        while player_choice not in ['R', 'P', 'S']:
            print("Choix invalide. Veuillez choisir entre R, P ou S.")
            player_choice = input(f"{player_name}, choisissez [R]ock, [P]aper, ou [S]cissors: ").upper()

        game.play_game(player_choice)

        print("Résultat de la partie actuelle:")
        last_game = game.get_history()[-1]
        result = "Égalité" if last_game['result'] == 0 else "Vous gagnez" if last_game['result'] == 1 else "L'ordinateur gagne"
        print(f"Votre choix: {last_game['player_choice']}, Choix de l'ordinateur: {last_game['computer_choice']}. {result}.")

        replay = input("Voulez-vous jouer une autre partie? (oui/non): ").lower()
        if replay != "oui":
            break

        print("\nHistorique des parties précédentes:")
        for record in game.get_history():
            result = "Égalité" if record['result'] == 0 else "Victoire" if record['result'] == 1 else "Défaite"
            print(f"{record['player_name']} a choisi {record['player_choice']}, l'ordinateur a choisi {record['computer_choice']}. Résultat: {result}.")

if __name__ == "__main__":
    interactive_test()
