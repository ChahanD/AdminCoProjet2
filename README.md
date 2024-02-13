# Pierre/Feuille/Ciseaux



## À propos du projet
Ce projet implémente une version interactive du jeu classique Pierre/Feuille/Ciseaux. Contrairement à l'approche traditionnelle qui retourne 0, 1, ou 2 pour indiquer respectivement une égalité, une victoire du joueur 1, ou une victoire du joueur 2, notre implémentation retourne directement le résultat sous forme de texte ("Égalité", "Joueur 1 gagne", "Joueur 2 gagne", ou "L'ordinateur gagne")
> Nous avons prit cette liberté afin de pouvoir plus facilement ajouter des ameliorations comme d'autres joueurs et augmenter la lisibilité des résultats.

## Fonctionnalités
- Mode de jeu flexible : Les utilisateurs peuvent choisir de jouer contre un autre joueur ou contre l'ordinateur.
- Affichage du choix de l'ordinateur : En mode un joueur, le choix de l'ordinateur est affiché après chaque tour.
- Règles standard de Pierre/Feuille/Ciseaux : La logique du jeu suit les règles standard de Pierre/Feuille/Ciseaux.

## Fichiers et Fonctions Principales
- 'RPS_SimpleGame.py' : Ce fichier contient la classe RPS_SimpleGame avec deux méthodes principales :
    - SimplegameTwoPlayers(player1choice, player2choice) : Détermine le gagnant entre deux joueurs.
    - SimplegameOnePlayer(player1choice) : Permet à un joueur de jouer contre l'ordinateur, retournant le résultat du jeu et le choix de l'ordinateur.
- 'play_rps_game.py' : Script principal qui implémente l'interface utilisateur pour jouer au jeu. Ce script utilise la classe 'RPS_SimpleGame' pour gérer la logique du jeu.
- Tests Unitaires :
    - 'test_RPS_SimpleGame.py' : Fichier contenant les tests unitaires pour la classe 'RPS_SimpleGame'. Ces tests assurent le bon fonctionnement de la logique du jeu.

# Utilisation
Pour lancer le jeu, exécutez le script play_rps_game.py. Suivez les instructions à l'écran pour choisir le mode de jeu et faire vos choix en tant que joueur.

# Conclusion
Ce projet a été une opportunité d'explorer des approches interactives et utilisateurs-friendly pour un jeu classique. L'accent a été mis sur la clarté du code et sur une implémentation intuitive pour l'utilisateur.