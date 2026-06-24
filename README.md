# Duolité 🎮

**"Duolité, le n°1 des jeux seul ou à deux"**

Duolité est une suite complète de 12 jeux classiques et modernes, entièrement développée en Python avec Pygame. Jouez en solo ou en multijoueur local, avec support de connexion LAN pour les jeux multijoueurs.

## 📋 Fonctionnalités

- **12 jeux différents** à découvrir et maîtriser
- **Mode solo et multijoueur** : jouez seul contre l'ordinateur ou affrontez un ami
- **Connexion LAN** : défiez vos amis en réseau local
- **Interface graphique intuitive** : navigation facile entre les jeux
- **Profils joueurs** : enregistrez les noms de vos joueurs
- **Exécutable standalone** : executable fourni (compilé avec PyInstaller)

## 🎯 Les Jeux

### Page 1
| Jeu | Description |
|-----|-------------|
| **Bataille Navale** | Coullez les navires ennemis en devinant leurs positions |
| **Pendu** | Trouvez le mot caché avant d'être pendu |
| **Chifoumi (Pierre-Papier-Ciseaux)** | Le classique affrontement main contre main |
| **Puissance 4** | Alignez 4 pions pour remporter la partie |
| **Juste Prix** | Devinez le prix d'un objet mystérieux |
| **Morpion (Tic-Tac-Toe)** | Trois en ligne pour gagner |

### Page 2
| Jeu | Description |
|-----|-------------|
| **421** | Jeu de dés avec des combinaisons spéciales |
| **Motus** | Trouvez le mot secret en 6 tentatives |
| **Mémorie** | Retournez les paires de cartes identiques |
| **Mastermind** | Décryptez le code secret couleur |
| **Yams (Yahtzee)** | Jeu de dés avec des stratégies combinatoires |
| **Boogle** | Trouvez le maximum de mots dans une grille |

## 🚀 Installation

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Depuis les sources

1. **Clonez le dépôt**
   ```bash
   git clone https://github.com/TomaLamp/Duolite.git
   cd Duolite
   ```

2. **Créez un environnement virtuel** (optionnel mais recommandé)
   ```bash
   python -m venv venv
   # Sous Windows
   venv\Scripts\activate
   # Sous macOS/Linux
   source venv/bin/activate
   ```

3. **Installez les dépendances**
   ```bash
   pip install -r requirements.txt
   ```
   ou
   ```bash
   pip install pygame
   ```

4. **Lancez le jeu**
   ```bash
   python main.py
   ```

### Construire l'Exécutable
Le projet utilise PyInstaller pour compiler en exécutable (Windows/MacOS/Linux) :

```bash
pip install pyinstaller
pyinstaller --clean --noconfirm main.spec
```

L'exécutable sera généré dans le dossier `dist/Duolité`.


## 📖 Comment Utiliser

### Écran Principal
1. Au lancement, vous accédez à l'écran de sélection des jeux
2. Cliquez sur le jeu de votre choix pour commencer
3. Utilisez les flèches pour naviguer entre les pages de jeux

### Avant de Jouer
1. Cliquez sur l'icône ⚙️ **Réglages** pour configurer les noms des joueurs
2. Entrez les noms de joueur 1 et joueur 2
3. Cliquez sur **Sauvegarder**

### Mode Multijoueur en Réseau (LAN)
1. Cliquez sur **Connexion LAN** sur l'écran principal
2. Choisissez si vous êtes l'hôte ou le client
3. Entrez l'adresse IP du destinataire
4. Lancez un jeu multijoueur et jouez en réseau !

### Pendant un Jeu
- Les contrôles spécifiques varient selon le jeu
- Consultez les instructions affichées à l'écran
- Utilisez la souris et le clavier selon les besoins

## 🛠️ Développement

### Structure du Projet
```
Duolité/
├── main.py                 # Point d'entrée principal
├── main.spec              # Configuration PyInstaller
├── jeux/                  # Tous les jeux
│   ├── bataille_naval.py
│   ├── pendu.py
│   ├── chifoumi.py
│   └── ...
├── module/                # Modules partagés
│   ├── pygameCore.py      # Fonctions Pygame communes
│   ├── config.py          # Gestion configuration
│   ├── LANscreen.py       # Connexion réseau
│   └── connectLAN.py      # Client/serveur LAN
├── image/                 # Ressources graphiques
├── police/                # Fichiers police
└── annexes/               # Données supplémentaires
```

## 🐛 Dépannage

**Le jeu refuse de démarrer**
- Vérifiez que Python 3.8+ est installé : `python --version`
- Assurez-vous que Pygame est installé : `pip install pygame`
- Vérifiez que toutes les ressources (`image/`, `annexes/`, etc.) sont présentes

**Les images ne s'affichent pas**
- Vérifiez que le dossier `image/` existe et contient les fichiers PNG/JPG
- Assurez-vous que le répertoire de travail est la racine du projet

**Les jeux multijoueurs LAN ne fonctionnent pas**
- Vérifiez que les deux ordinateurs sont sur le même réseau local
- Vérifiez l'adresse IP du destinataire (`ipconfig` sur Windows)
- Assurez-vous qu'aucun pare-feu ne bloque les connexions

## 📝 Licence

[Spécifiez votre licence ici, ex: MIT, GPL, etc.]

## 👥 Contributeurs

- **LAMPURE Thomas**
- **DUCASSE Léo**

## 📧 Contact

Pour toute question, problème ou suggestion, veuillez ouvrir une issue sur GitHub.

---

**Bon jeu ! 🎉**
