import random
from pygame import *
import pygame
from module.pygameCore import *
from module.LANscreen import *
from threading import Timer
import time
import cloudpickle as cpickle


# %% classes
class De:
    def __init__(self, lettres : str = None) -> None:
        """Crée un dé avec ses 6 faces contenant des lettres
        - lettres : chaîne contenant les 6 lettres du dé (optionnel)
        """
        if lettres:
            self.faces = lettres[:6]  # Assurez-vous que 'lettres' a au moins 6 caractères
            self.face_visible = self.faces[random.randint(0, 5)]
        else:
            self.faces = ['-'] * 6
            self.face_visible = '-'

    @property
    def Face_visible(self) -> str:
        """Retourne la face visible du dé"""
        return self.face_visible

    @Face_visible.setter
    def Face_visible(self, value : str) -> None:
        """Définit la face visible du dé"""
        self.face_visible = value

    @property
    def Faces(self) -> list:
        """Retourne la liste des 6 faces du dé"""
        return self.faces

    def Lancer(self) -> None:
        """Lance le dé et affecte une face aléatoire à la face visible"""
        self.face_visible = self.faces[random.randint(0, 5)]


class Dictionary:
    def __init__(self, langue : str) -> None:
        """
        Constructeur de la classe Dictionary, initialise les mots en fonction de la langue.
        """
        self.langue = langue

        if langue == "fr":
            with open("./annexes/MotsPossiblesFR.txt", "r") as f:
                self.mots = f.read().split(" ")
            self.mots = self.TriFusion(self.mots)
        else:
            self.mots = [""]

    @staticmethod
    def TriFusion(tab : list) -> list:
        """Trie un tableau de mots en utilisant l'algorithme de tri fusion
        - tab : tableau à trier
        - Retourne : le tableau trié
        """
        if len(tab) <= 1:
            return tab

        # Diviser le tableau en deux moitiés
        mid = len(tab) // 2
        a = tab[:mid]
        b = tab[mid:]

        # Appeler récursivement TriFusion sur chaque moitié
        return Dictionary.Fusion(Dictionary.TriFusion(a), Dictionary.TriFusion(b))

    @staticmethod
    def Fusion(a : list, b : list) -> list:
        """Fusionne deux listes triées en une seule liste triée
        - a : première liste triée
        - b : deuxième liste triée
        - Retourne : la liste fusionnée et triée
        """
        if b is None:
            return a
        if a is None:
            return b

        c = []
        i = j = 0

        # Comparer et fusionner les éléments de a et b
        while i < len(a) and j < len(b):
            if a[i] <= b[j]:
                c.append(a[i])
                i += 1
            else:
                c.append(b[j])
                j += 1

        # Ajouter les éléments restants de a ou b
        while i < len(a):
            c.append(a[i])
            i += 1

        while j < len(b):
            c.append(b[j])
            j += 1

        return c

    def RechDichoRecursif(self, mot : str, fin : int = None, debut : int = 0) -> bool:
        """Recherche dichotomique récursive pour vérifier si un mot est dans le dictionnaire
        - mot : mot à rechercher
        - fin : index de fin (optionnel)
        - debut : index de début (optionnel)
        - Retourne : True si le mot est trouvé, False sinon
        """
        if fin is None:
            fin = len(self.mots) - 1

        if debut > fin:
            return False

        mid_index = (debut + fin) // 2
        mid = self.mots[mid_index]

        if mid == mot:
            return True
        elif mid < mot:
            return self.RechDichoRecursif(mot, fin, mid_index + 1)
        else:
            return self.RechDichoRecursif(mot, mid_index - 1, debut)

class Plateau:
    def __init__(self, fichier : str = "./annexes/Lettres.txt", taille : int = 4, langue : str = "fr") -> None:
        """Crée le plateau de jeu avec une grille de dés
        - fichier : chemin du fichier contenant les lettres
        - taille : taille de la grille (4 par défaut)
        - langue : langue utilisée pour le dictionnaire
        """
        self.dico = Dictionary(langue)

        # Lire le fichier et remplir le tableau fich
        with open(fichier, 'r') as f:
            lines = f.readlines()
        
        self.fich = [line.strip().split(';') for line in lines]
        lettres = [['-' for _ in range(6)] for _ in range(taille * taille)]

        # Assigner aléatoirement les lettres aux dés
        r = random.Random()
        compt = 0
        tab = list(range(taille * taille))  # Table d'indices disponibles
        

        for i in range(26):
            lettre = self.fich[i][0]
            occurrences = int(self.fich[i][2])
            
            for _ in range(occurrences):
                a = r.randint(0, taille * taille - compt-1)
                k = 0
                while k < 6 and lettres[tab[a]][k] != '-':
                    k += 1
                if k < 6:
                    lettres[tab[a]][k] = lettre
                if k == 5:  # Lorsque le dé est plein
                    tab[tab.index(tab[a])] = tab[len(tab)-1 - compt]  
                    if(compt!=15):
                        compt += 1
                
                
        for i in range(0, 16):  # Exclure les bordures
            var = ""
            for j in range(0, 6):
                var+= lettres[i][j]+" "

        # Créer la matrice de dés
        self.grille = [[None for _ in range(taille + 2)] for _ in range(taille + 2)]
        comp = 0

        for i in range(taille + 2):
            for j in range(taille + 2):
                if i < 1 or j < 1 or i > taille or j > taille:
                    self.grille[i][j] = De()  # Bordures vides
                else:
                    self.grille[i][j] = De(lettres[comp])
                    comp += 1
    
    @property
    def Grille(self) -> list:
        """Retourne la grille de dés du plateau"""
        return self.grille
    
    def AfficheGrille(self, fenetre : pygame.Surface) -> None:
        """Affiche la grille des dés sur la fenêtre
        - fenetre : la fenetre pygame où afficher
        """
        fenetre.fill("#A2B203")
        for i in range(1, len(self.grille) - 1):  # Exclure les bordures
            for j in range(1, len(self.grille[i]) - 1):

                rect = printImage("./image/421/blanc.png", (75, 75), [312.5+(j-1)*100, 112.5+(i-1)*100], fenetre).width
                printText(self.grille[i][j].face_visible, 60, pygame.Color("black"), (312.5+(j-1)*100+rect/2, 135+(i-1)*100), fenetre, Alignement="Center")
                pygame.display.flip()

                

    def MotLie(self, mot : str, x : int, y : int, pos : int = 0) -> bool:
        """Vérifie si les lettres du mot sont liées adjacentes sur le plateau
        - mot : mot à vérifier
        - x, y : position de départ
        - pos : position courante dans le mot
        - Retourne : True si le mot est valide, False sinon
        """
        if pos >= len(mot):
            return True  # Si toutes les lettres ont été trouvées

        # Obtenir la face visible actuelle
        c = self.grille[x][y].face_visible

        # Explorer toutes les cases adjacentes (y compris diagonales)
        for i in range(-1, 2):  # -1, 0, 1
            for j in range(-1, 2):
                if self.grille[x + i][y + j].face_visible == mot[pos]:
                    # Appel récursif pour vérifier la prochaine lettre
                    self.grille[x][y].face_visible = '-'
                    res = self.MotLie(mot, x + i, y + j, pos + 1)
                    if res:
                        # Restaurer la face visible avant de retourner
                        self.grille[x][y].face_visible = c
                        return True

        # Restaurer la face visible si aucune correspondance n'est trouvée
        self.grille[x][y].face_visible = c
        return False
    

    def MotDansGrille(self, mot : str) -> bool:
        """Vérifie si un mot complet existe dans la grille
        - mot : mot à vérifier
        - Retourne : True si le mot est dans la grille, False sinon
        """
        res = False
        for i in range(1, len(self.grille) - 1):  # Parcourir les cases internes de la grille
            if res:
                break  # Sortir si le mot a été trouvé
            for j in range(1, len(self.grille[i]) - 1):
                if mot[0] == self.grille[i][j].face_visible:  # Vérifier la première lettre
                    res = self.MotLie(mot, i, j)  # Appeler MotLie
                    if res:
                        break  # Sortir dès que le mot est trouvé
        return res

    def Test_Plateau(self, mot : str) -> bool:
        """Teste si un mot est valide (existe dans le dictionnaire et la grille)
        - mot : mot à tester
        - Retourne : True si le mot est valide, False sinon
        """
        return self.MotDansGrille(mot) and self.dico.RechDichoRecursif(mot)

    def LancePlateau(self) -> None:
        """Lance tous les dés du plateau pour générer de nouvelles faces visibles"""
        for i in range(1, len(self.grille) - 1):  # Parcourir les cases internes de la grille
            for j in range(1, len(self.grille[i]) - 1):
                self.grille[i][j].Lancer()

    def ScoreMot(self, mot : str) -> int:
        """Calcule le score d'un mot en fonction de sa longueur
        - mot : mot dont calculer le score
        - Retourne : le score du mot
        """
        score = 0
        atteind = False

        for i in range(len(mot)):
            atteind = False
            for j in range(26):  # Parcourir les 26 lettres de l'alphabet
                if not atteind and mot[i] == self.fich[j][0]:
                    score += int(self.fich[j][1])
                    atteind = True

        return score


class Player:
    def __init__(self, name : str) -> None:
        """Crée un joueur avec un nom et initialise son score et ses mots
        - name : nom du joueur
        """
        self.name = name
        self.score = 0
        self.list = []

    def Contain(self, mot : str) -> bool:
        """Vérifie si un mot a déjà été trouvé par le joueur
        - mot : mot à vérifier
        - Retourne : True si le mot est déjà trouvé, False sinon
        """
        test = 0
        for c in self.list:
            if mot == c:
                test += 1
        return test > 0

    def Add_Mot(self, mot : str) -> None:
        """Ajoute un mot à la liste des mots trouvés par le joueur
        - mot : mot à ajouter
        """
        if not self.Contain(mot):
            self.list.append(mot)


class Jeu:
    def __init__(self, langue : str, taille : int, nb_joueur : int, connexion : list, fenetre : pygame.Surface, nomj1 : str, nomj2 : str) -> None:
        """Initialise une partie de Boogle
        - langue : langue du jeu
        - taille : taille de la grille
        - nb_joueur : nombre de joueurs
        - connexion : paramètres de connexion LAN
        - fenetre : fenetre pygame du jeu
        - nomj1, nomj2 : noms des joueurs
        """
        self.joueurs = [Player(nomj1)]
        self.grille = Plateau("./annexes/Lettres.txt", taille, langue)
        self.connexion = connexion
        self.kijou=0
        self.fenetre = fenetre

        if nb_joueur==2:
            self.joueurs.append(Player(nomj2))

    def Gagnant(self) -> 'Player':
        """Détermine et retourne le joueur avec le score le plus élevé"""
        max_score = 0
        gagnant = self.joueurs[0]

        for joueur in self.joueurs:
            if joueur.score > max_score:
                max_score = joueur.score
                gagnant = joueur

        return gagnant

    def OnTimedEvent(self) -> None:
        """Gère l'événement de fin de temps (timeout) pour un tour de jeu"""
        printImage("./image/boogle/vert.png", (800, 80), (100,10), self.fenetre)
        printImage("./image/boogle/suivant.png", (250, 60.913), [740, 270], self.fenetre)
        printText("Fin du tour, appuyez sur entrée", 60, pygame.Color("black"), (200, 10), self.fenetre)
        pygame.display.flip()
        self.fin_timer = True
        self.kijou+=1

    def get_lettre(self, startTime : float) -> str:
        """Récupère la lettre saisie par le joueur (clavier ou souris)
        - startTime : timestamp du début du tour
        - Retourne : la lettre saisie ou un caractère spécial (< pour backspace, > pour valider)
        """
        end = 0
        conn = self.connexion[0]
        lettre=" "
        while end==0:
            if conn==None or self.connexion[2]==True and self.kijou%2 == 0 or self.connexion[2]==False and self.kijou%2 == 1:
                for event in pygame.event.get():
                    if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]

                        posj = (x-312.5)/100 + 1
                        posi = (y-112.5)/100 + 1
                        j = int((x-312.5)//100 + 1)
                        i = int((y-112.5)//100 + 1)
                        
                        if y>277 and y<327 and x>740 and self.fin_timer:
                            lettre = ">"
                        if i>0 and i<=4 and j>0 and j<=4 and posi-i<0.735 and posj-j<0.735:
                            lettre = self.grille.Grille[i][j].Face_visible

                    if event.type == KEYDOWN:
                        if event.key<=122 and event.key>=97:
                            lettre = chr(event.key).upper()
                        elif event.key==8:
                            lettre = "<"
                        elif event.key==13:
                            lettre = ">"
                        
                    if (event.type == QUIT): 
                        if conn!=None:
                            conn.send(b"404")
                        return 0
                    
                    if lettre!=" ":
                        if conn!=None:
                            send_data(self.connexion, bytes(lettre, "utf-8"), self.fenetre, "#778100", "#323600")
                        return lettre
                    
            else:
                try:
                    data = conn.recv(1024)
                    prop = str(data, "utf-8")
                    if prop=="404":
                        result = quitScreen(self.fenetre, self.connexion, "#778100", "#323600")
                        if result=="NULL":
                            return 0
                    else:
                        return prop
                except BlockingIOError:
                    pass
                                
                for event in pygame.event.get():
                    if (event.type == pygame.QUIT): 
                        conn.send(bytes("404", "utf-8"))
                        return 0
            
            if not self.fin_timer:
                pygame.draw.rect(self.fenetre, "#A2B203", (850, 500, 200, 200))
                printText("Timer : ", 60, "black", (850, 500), self.fenetre)
                printText(str(round(30-(time.time()-startTime))), 60, "black", (900, 550), self.fenetre)
                pygame.display.flip()        
    
    def get_mot(self, startTime : float) -> str:
        """Récupère le mot complet saisi par le joueur lettre par lettre
        - startTime : timestamp du début du tour
        - Retourne : le mot saisi ou une chaîne vide si timeout
        """
        
        printImage("./image/boogle/vert.png", (1000, 80), (0,520), self.fenetre)
        pygame.display.flip()

        chaine = ""
        chainebis = ""
        lettre = self.get_lettre(startTime)
        while(lettre!=">"):
            if(lettre==0):
                return 0
            elif(lettre!="<"):
                chaine+=lettre
            else:
                for i in range(len(chaine)-1):
                    chainebis += chaine[i]
                chaine=""
                for j in range(len(chainebis)):
                    chaine += chainebis[j]
                chainebis=""

            printImage("./image/boogle/vert.png", (800, 80), (0,520), self.fenetre)
            printText(f"{chaine}", 60, pygame.Color("black"), (500, 540), self.fenetre, Alignement="Center")
            pygame.display.flip()
            lettre = self.get_lettre(startTime)
        return chaine

    def Jouer(self) -> int:
        """Lance la partie de Boogle avec 3 tours par joueur
        - Retourne : 0 en cas d'interruption, 1 si la partie s'est déroulée correctement
        """
        for _ in range(3):  # Trois tours par joueur
            self.kijou=0
            for joueur in self.joueurs:
                if self.connexion[0]==None or self.connexion[2]==True:
                    self.grille.LancePlateau()
                    if self.connexion[0]!=None:
                        data = pickle.dumps(self.grille)
                        self.connexion[0].send(len(data).to_bytes(4))
                        self.connexion[0].sendall(data)
                else:
                    while True:
                        size_bytes = recv_all(self.connexion[0], 4)
                        size = int.from_bytes(size_bytes, "big")
                        data = recv_all(self.connexion[0], size)
                        if not data:
                            continue
                        
                        self.grille = pickle.loads(data)
                        break

                self.grille.AfficheGrille(self.fenetre)

                printImage("./image/boogle/vert.png", (250, 250), (10,200), self.fenetre)
                if(len(self.joueurs)==2):
                    printText(f"Au tour de {joueur.name}", 60, pygame.Color("black"), (500, 10), self.fenetre, Alignement="Center")
                    printText(f"{self.joueurs[0].name} : {self.joueurs[0].score}", 50, pygame.Color("black"), (10, 270), self.fenetre)
                    printText(f"{self.joueurs[1].name} : {self.joueurs[1].score}", 50, pygame.Color("black"), (10, 330), self.fenetre)
                    pygame.display.flip()
                else:
                    printText("Choisissez un mot", 60, pygame.Color("black"), (320, 10), self.fenetre)
                    printText(f"Score : {self.joueurs[0].score}", 60, pygame.Color("black"), (10, 300), self.fenetre)
                    pygame.display.flip()

                self.fin_timer = False

                # Définir un timer de 30 secondes
                timer = Timer(30.0, self.OnTimedEvent)
                timer.start()
                start = time.time()

                while not self.fin_timer:
                    mot = ""
                    while not mot or len(mot) <= 2 or not self.grille.Test_Plateau(mot) or joueur.Contain(mot):
                        mot = self.get_mot(start)
                        if(mot==0):
                            timer.cancel()
                            return 0
                            
                        if self.fin_timer:
                            break
                        

                    if not self.fin_timer:
                        score = self.grille.ScoreMot(mot)
                        joueur.score += score
                        joueur.Add_Mot(mot)

                        printImage("./image/boogle/vert.png", (250, 200), (10,250), self.fenetre)
                        if(len(self.joueurs)==2):
                            printText(f"{self.joueurs[0].name} : {self.joueurs[0].score}", 50, pygame.Color("black"), (10, 270), self.fenetre)
                            printText(f"{self.joueurs[1].name} : {self.joueurs[1].score}", 50, pygame.Color("black"), (10, 330), self.fenetre)
                            pygame.display.flip()
                        else:
                            printText(f"Score : {self.joueurs[0].score}", 60, pygame.Color("black"), (10, 300), self.fenetre)
                            pygame.display.flip()
                        

                timer.cancel()

        # Déterminer et afficher le gagnant
        
        printImage("./image/boogle/vert.png", (900, 100), (5,5), self.fenetre)
        if(len(self.joueurs)==2):
            gagnant = self.Gagnant()
            printText(f"Victoire de {gagnant.name}", 60, pygame.Color("black"), (500, 10), self.fenetre, Alignement="Center")
            pygame.display.flip()
        else:
            printText(f"Bravo tu as {joueur.score} points", 60, pygame.Color("black"), (290, 10), self.fenetre)
            pygame.display.flip()


def boogle(connexion=[None, None, None]) -> int:
    """Fonction principale du jeu Boogle
    - connexion : paramètres de connexion LAN
    """

    fenetre = initScreen((1000,600), "boogle", "#A2B203","./image/boogle/icon.png")

    printImage("./image/boogle/play.png", (700, 428.75), (150,50), fenetre)
    pygame.display.flip()

    nomj1, nomj2 = get_nom()
    conn = None
    if connexion[0]!=None and connexion[2]==True:
        nomj2=connexion[1]
    elif connexion[0]!=None and connexion[2]==False:
        nomj2=nomj1
        nomj1=connexion[1]
            

    fin = 0
    while fin == 0:
        for event in pygame.event.get():
            if (event.type == MOUSEBUTTONUP):
                x = event.pos[0]
                y = event.pos[1]
                if x > 150 and x < 850 and y > 50 and y < 478:
                    fin = 1 
                        
            if (event.type == KEYDOWN) or (event.type == QUIT): 
                return 0
            
    restart = 0
    while restart == 0:
        fenetre.fill("#A2B203")
        end = 0
        while end==0:
            printImage("./image/boogle/1joueur.png", (750, 185.7), (150, 65), fenetre)
            printImage("./image/boogle/2joueur.png", (750, 185.7), (150, 350), fenetre)
            pygame.display.flip()

            for event in pygame.event.get():

                if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]
                        if x>150 and x<900 and y>65 and y<250.7:
                            end=1
                            nbjoueur = 1
                        elif x>150 and x<900 and y>350 and y<535.7:
                            if connexion[0]!=None:
                                quit = waitScreen(fenetre, connexion, "#778100", "#323600", "boogle")
                                fenetre.fill("#A2B203")
                                printImage("./image/boogle/1joueur.png", (750, 185.7), (150, 65), fenetre)
                                printImage("./image/boogle/2joueur.png", (750, 185.7), (150, 350), fenetre)
                                if quit=="NULL":
                                    return 0
                                elif quit==1:
                                    end=1
                                    nbjoueur = 2
                                    conn = connexion[0]
                            else:
                                end=1
                                nbjoueur = 2


                if (event.type == QUIT): 
                    return 0

        rejouer=0
        while(rejouer==0):
            jeu = Jeu("fr", 4, nbjoueur, connexion, fenetre, nomj1, nomj2)
            a=jeu.Jouer()
            
            if(a!=0):
                printImage("./image/boogle/rejouer.png", (250, 68.059), [740, 270], fenetre)
                printImage("./image/juste prix/fleche.png", (50,34.35), [5, 5], fenetre, rotation=180)
                pygame.display.flip()

                        
                fin=0
                while fin==0:
                    for event in pygame.event.get():
                        if (event.type == MOUSEBUTTONUP):
                            x = event.pos[0]
                            y = event.pos[1]
                            if y>277 and y<327 and x>740 and x<990:
                                if conn!=None:
                                    quit = waitScreen(fenetre, connexion, "#778100", "#323600", "boogle")
                                    if quit=="NULL":
                                        return 0
                                    elif quit==1:
                                        fin=1
                                else:
                                    fin=1
                            if(x>21 and x<51 and y>10 and y<21) or (x>5 and x<20 and y>1 and y<31):
                                fin=1
                                rejouer=1
                                if conn!=None:
                                    conn.send(b"404")

                        if (event.type == QUIT): 
                            return 0
            else:
                rejouer=1
                restart=1


if __name__ == "__main__":
    boogle()