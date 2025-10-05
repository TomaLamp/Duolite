import random
from pygame import *
import pygame
from module.pygameCore import *
from threading import Timer
import time

def boogle():

    # %% classes
    class De:
        def __init__(self, lettres=None):
            if lettres:
                self.faces = lettres[:6]  # Assurez-vous que 'lettres' a au moins 6 caractères
                self.face_visible = self.faces[random.randint(0, 5)]
            else:
                self.faces = ['-'] * 6
                self.face_visible = '-'

        @property
        def Face_visible(self):
            return self.face_visible

        @Face_visible.setter
        def Face_visible(self, value):
            self.face_visible = value

        @property
        def Faces(self):
            return self.faces

        def Lancer(self):
            self.face_visible = self.faces[random.randint(0, 5)]


    class Dictionary:
        def __init__(self, langue):
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
        def TriFusion(tab):
            """
            Implémentation de l'algorithme de tri fusion pour trier un tableau de mots.
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
        def Fusion(a, b):
            """
            Fusionne deux listes triées en une seule liste triée.
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

        def RechDichoRecursif(self, mot, fin=None, debut=0):
            """
            Recherche dichotomique récursive pour vérifier si un mot est dans la liste triée des mots.
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
        def __init__(self, fichier="./annexes/Lettres.txt", taille=4, langue="fr"):
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
        

        def AfficheGrille(self):
            """
            Affiche la grille en ne considérant que les éléments à l'intérieur des bordures.
            """
            fenetre.fill("#A2B203")
            for i in range(1, len(self.grille) - 1):  # Exclure les bordures
                for j in range(1, len(self.grille[i]) - 1):

                    
                    rect = printImage("./image/421/blanc.png", (75, 75), [312.5+(j-1)*100, 112.5+(i-1)*100], fenetre).width
                    printText(self.grille[i][j].face_visible, 60, pygame.Color("black"), (312.5+(j-1)*100+rect/2, 135+(i-1)*100), fenetre, Alignement="Center")
                    pygame.display.flip()

                    

        def MotLie(self, mot, x, y, pos=0):
            """
            Vérifie si le mot est lié à partir de la position (x, y).
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
        

        def MotDansGrille(self, mot):
            """
            Vérifie si un mot est présent dans la grille.
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

        def Test_Plateau(self, mot):
            """
            Vérifie si un mot est dans la grille et dans le dictionnaire.
            """
            return self.MotDansGrille(mot) and self.dico.RechDichoRecursif(mot)

        def LancePlateau(self):
            """
            Lance tous les dés dans la grille.
            """
            for i in range(1, len(self.grille) - 1):  # Parcourir les cases internes de la grille
                for j in range(1, len(self.grille[i]) - 1):
                    self.grille[i][j].Lancer()

        def ScoreMot(self, mot):
            """
            Calcule le score d'un mot en fonction de la valeur des lettres définies dans le fichier de configuration.
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
        def __init__(self, name):
            """
            Constructeur de la classe Player.
            Initialise le nom du joueur, le score et la liste des mots trouvés.
            """
            self.name = name
            self.score = 0
            self.list = []

        def Contain(self, mot):
            """
            Vérifie si le mot donné est déjà présent dans la liste des mots du joueur.
            """
            test = 0
            for c in self.list:
                if mot == c:
                    test += 1
            return test > 0

        def Add_Mot(self, mot):
            """
            Ajoute un mot à la liste des mots du joueur si celui-ci n'y figure pas déjà.
            """
            if not self.Contain(mot):
                self.list.append(mot)

    
    class Jeu:
        def __init__(self, langue, taille, nb_joueurs):
            """
            Constructeur de la classe Jeu.
            Initialise les joueurs et la grille du jeu.
            """
            self.joueurs = [Player(nomj1)]
            self.grille = Plateau("./annexes/Lettres.txt", taille, langue)

            if nb_joueur==2:
                self.joueurs.append(Player(nomj2))

        def Gagnant(self):
            """
            Détermine le joueur avec le score le plus élevé.
            """
            max_score = 0
            gagnant = self.joueurs[0]

            for joueur in self.joueurs:
                if joueur.score > max_score:
                    max_score = joueur.score
                    gagnant = joueur

            return gagnant

        def OnTimedEvent(self):
            """
            Gère l'événement de fin de temps pour un tour.
            """
            printImage("./image/boogle/vert.png", (800, 80), (100,10), fenetre)
            printImage("./image/boogle/suivant.png", (250, 60.913), [740, 270], fenetre)
            printText("Fin du tour, appuyez sur entrée", 60, pygame.Color("black"), (200, 10), fenetre)
            pygame.display.flip()
            self.fin_timer = True

        def get_lettre(self, startTime):
            lettre = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "<", ">"]
            end = 0
            while end==0:
                for event in pygame.event.get():
                    if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]
                        if y>277 and y<327 and x>740 and self.fin_timer:
                            return ">"

                    if event.type == KEYDOWN:
                        if event.key<=122 and event.key>=97:
                            return chr(event.key).upper()
                        elif event.key==8:
                            return("<")
                        elif event.key==13:
                            return(">")
                        
                    if (event.type == QUIT): 
                        return 0
                
                if not self.fin_timer:
                    pygame.draw.rect(fenetre, "#A2B203", (850, 500, 200, 200))
                    printText("Timer : ", 60, "black", (850, 500), fenetre)
                    printText(str(round(time.time()-startTime)), 60, "black", (900, 550), fenetre)
                    pygame.display.flip()        
        
        def get_mot(self, startTime):
            
            printImage("./image/boogle/vert.png", (1000, 80), (0,520), fenetre)
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

                printImage("./image/boogle/vert.png", (1000, 80), (0,520), fenetre)
                printText(f"{chaine}", 60, pygame.Color("black"), (500, 540), fenetre, Alignement="Center")
                pygame.display.flip()
                lettre = self.get_lettre(startTime)
            return chaine

        def Jouer(self):
            """
            Lance la partie.
            Chaque joueur joue trois tours où ils choisissent des mots dans la grille.
            """
            for _ in range(3):  # Trois tours par joueur
                for joueur in self.joueurs:
                    self.grille.LancePlateau()
                    self.grille.AfficheGrille()

                    printImage("./image/boogle/vert.png", (250, 250), (10,200), fenetre)
                    if(len(self.joueurs)==2):
                        printText(f"Au tour de {joueur.name}", 60, pygame.Color("black"), (500, 10), fenetre, Alignement="Center")
                        printText(f"{self.joueurs[0].name} : {self.joueurs[0].score}", 50, pygame.Color("black"), (10, 270), fenetre)
                        printText(f"{self.joueurs[1].name} : {self.joueurs[1].score}", 50, pygame.Color("black"), (10, 330), fenetre)
                        pygame.display.flip()
                    else:
                        printText("Choisissez un mot", 60, pygame.Color("black"), (320, 10), fenetre)
                        printText(f"Score : {self.joueurs[0].score}", 60, pygame.Color("black"), (10, 300), fenetre)
                        pygame.display.flip()

                    self.fin_timer = False

                    # Définir un timer de 60 secondes
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

                            printImage("./image/boogle/vert.png", (250, 200), (10,250), fenetre)
                            if(len(self.joueurs)==2):
                                printText(f"{self.joueurs[0].name} : {self.joueurs[0].score}", 50, pygame.Color("black"), (10, 270), fenetre)
                                printText(f"{self.joueurs[1].name} : {self.joueurs[1].score}", 50, pygame.Color("black"), (10, 330), fenetre)
                                pygame.display.flip()
                            else:
                                printText(f"Score : {self.joueurs[0].score}", 60, pygame.Color("black"), (10, 300), fenetre)
                                pygame.display.flip()
                            

                    timer.cancel()

            # Déterminer et afficher le gagnant
            
            printImage("./image/boogle/vert.png", (900, 100), (5,5), fenetre)
            if(len(self.joueurs)==2):
                gagnant = self.Gagnant()
                printText(f"Victoire de {gagnant.name}", 60, pygame.Color("black"), (500, 10), fenetre, Alignement="Center")
                pygame.display.flip()
            else:
                printText(f"Bravo tu as {joueur.score} points", 60, pygame.Color("black"), (290, 10), fenetre)
                pygame.display.flip()



    fenetre = initScreen((1000,600), "boogle", "#A2B203","./image/boogle/icon.png")

    printImage("./image/boogle/play.png", (700, 428.75), (150,50), fenetre)
    pygame.display.flip()

    nomj1, nomj2 = get_nom()
            

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
            pygame.display.flip()
            printImage("./image/boogle/2joueur.png", (750, 185.7), (150, 350), fenetre)
            pygame.display.flip()

            for event in pygame.event.get():

                if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]
                        if x>150 and x<900 and y>65 and y<250.7:
                            end=1
                            nb_joueur = 1
                        elif x>150 and x<900 and y>350 and y<535.7:
                            end=1
                            nb_joueur = 2


                if (event.type == QUIT): 
                    return 0

        rejouer=0
        while(rejouer==0):
            jeu = Jeu("fr", 4, nb_joueur)
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
                                fin=1
                            if(x>21 and x<51 and y>10 and y<21) or (x>5 and x<20 and y>1 and y<31):
                                fin=1
                                rejouer=1

                        if (event.type == QUIT): 
                            return 0
            else:
                rejouer=1
                restart=1


if __name__ == "__main__":
    boogle()