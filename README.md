# <span style="color:#1591C0">Pierre/Feuille/Ciseaux
## <span style="color:#1591C0">À propos du projet
Ce projet implémente une version interactive du jeu classique Pierre/Feuille/Ciseaux. Contrairement à l'approche traditionnelle qui retourne 0, 1, ou 2 pour indiquer respectivement une égalité, une victoire du joueur 1, ou une victoire du joueur 2, notre implémentation retourne directement le résultat sous forme de texte ("Égalité", "Joueur 1 gagne", "Joueur 2 gagne", ou "L'ordinateur gagne").

> Nous avons pris cette liberté afin de pouvoir plus facilement ajouter des améliorations comme d'autres joueurs et augmenter la lisibilité des résultats.

## <span style="color:#1591C0">Structure du projet
```bash 
AdminCoProjet2/
├── .git/
│   ├── (fichiers et dossiers de configuration git)
├── Game/
│   ├── __init__.py
│   ├── RPS_Tools/
│   │   ├── __init__.py
│   │   ├── RPS_MultipleGame.py
│   │   ├── RPS_SimpleGame.py
│   │   ├── ScriptMultiple.py
│   │   ├── ScriptSimpleGame.py
│   │   └── __pycache__/
│   │       ├── __init__.cpython-310.pyc
│   │       ├── RPS_MultipleGame.cpython-310.pyc
│   │       └── RPS_SimpleGame.cpython-310.pyc
│   └── tests/
│       ├── __init__.py
│       ├── test_multiplegame.py
│       └── test_simplegame.py
├── README.md
└── rps_history.csv
```

## <span style="color:#1591C0">Installation
```bash
git clone [URL_DU_DEPOT]
cd AdminCoProjet2
pip install -r requirements.txt
```

## <span style="color:#1591C0">Fonctionnalités
- ***Mode de jeu flexible*** : Les utilisateurs peuvent choisir de jouer contre un autre joueur ou contre l'ordinateur.
Affichage du choix de l'ordinateur : En mode un joueur, le choix de l'ordinateur est affiché après chaque tour.
- ***Historique des parties*** : Les résultats des parties précédentes sont enregistrés et peuvent être consultés pour des analyses.
- ***Règles standard de Pierre/Feuille/Ciseaux*** : La logique du jeu suit les règles standard de Pierre/Feuille/Ciseaux.
- ***Automatisation des tests et intégration continue*** : Tests unitaires et utilisation d'outils CI pour garantir la qualité et la fiabilité du code.
- ***Stratégie non aléatoire basée sur l'historique*** : L'ordinateur utilise l'historique des parties précédentes pour proposer une stratégie plus prédictive et moins aléatoire.


## <span style="color:#1591C0">Fichiers et Fonctions Principales

- ***RPS_SimpleGame.py*** : Ce fichier contient la classe RPS_SimpleGame avec deux méthodes principales :
- ***SimplegameTwoPlayers(player1choice, player2choice)***: Détermine le gagnant entre deux joueurs.
- ***SimplegameOnePlayer(player1choice)*** : Permet à un joueur de jouer contre l'ordinateur, retournant le résultat du jeu et le choix de l'ordinateur.
- ***RPS_MultipleGame.py*** : Classe pour gérer des sessions de jeu multiples, enregistre l'historique des parties dans un fichier CSV.
- ***Stratégies dans RPS_MultipleGame.py*** : Implémentation de stratégies basées sur l'historique pour améliorer les choix de l'ordinateur.
- ***ScriptSimpleGame.py*** : Script pour jouer une session de jeu simple.
- ***ScriptMultiple.py*** : Script pour jouer des sessions de jeu multiples avec historique.



## <span style="color:#1591C0">Tests Unitaires
- ***test_RPS_SimpleGame.py*** : Fichier contenant les tests unitaires pour la classe RPS_SimpleGame. Ces tests assurent le bon fonctionnement de la logique du jeu.
- ***test_RPS_MultipleGame.py*** : Fichier contenant les tests unitaires pour la classe RPS_MultipleGame, vérifiant le bon fonctionnement des parties multiples et de l'enregistrement de l'historique et vérifier les fonctionnalités de stratégie non aléatoire.


## <span style="color:#1591C0">Respect des Normes PEP 8 et PEP 20
 Ce projet adhère aux normes de codage PEP 8 pour garantir la clarté et la cohérence du code. Les principes PEP 20 tels que "Simple is better than complex" et "Readability counts" ont été suivis pour faciliter la maintenance et la compréhension du code.

## <span style="color:#1591C0">Utilisation
- Exécutez *ScriptSimpleGame.py* pour une session de jeu simple.
- Utilisez *ScriptMultiple.py*  pour des sessions de jeu multiples avec historique.

## <span style="color:#1591C0">Qualité du Code (Pylint Scores)
Dans le cadre de nos efforts pour maintenir un code de haute qualité, nous utilisons pylint et black pour évaluer et améliorer notre code. Voici les notes actuelles de pylint pour nos principaux fichiers :

Pour le fichier *RPS_MultipleGame.py* : 
```bash
Your code has been rated at 9.00/10 (previous run: 8.95/10, +0.05)
```

Pour le fichier *RPS_SimpleGame.py* : 
```bash
Your code has been rated at 7.50/10 (previous run: 6.67/10, +0.83)
```

Pour le fichier *test_multiplegame.py* : 
```bash
Your code has been rated at 7.50/10
```

Pour le fichier *test_simplegame.py* : 
```bash
Your code has been rated at 6.00/10 (previous run: 4.67/10, +1.33)
```

Pour le fichier *ScriptSimpleGame.py* : 
```bash
Your code has been rated at 7.33/10 (previous run: 5.52/10, +1.82)
```
Pour le fichier *ScriptMultipleGame.py* : 
```bash
Your code has been rated at 5.71/10 (previous run: 5.71/10, +0.00)
```

## <span style="color:#1591C0">Contribuer
Pour contribuer au projet, veuillez suivre ces étapes :

1. Fork le projet
2. Créez votre branche de fonctionnalité (git checkout -b feature/AmazingFeature)
3. Committez vos changements (git commit -m 'Add some AmazingFeature')
4. Push vers la branche (git push origin feature/AmazingFeature)

## <span style="color:#1591C0">Conclusion
Ce projet a été une opportunité d'explorer des approches interactives et utilisateurs-friendly pour un jeu classique. L'accent a été mis sur la clarté du code et sur une implémentation intuitive pour l'utilisateur.

