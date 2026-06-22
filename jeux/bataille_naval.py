import sys
from pathlib import Path

# Ajouter le répertoire parent au sys.path pour permettre les imports quand le script est lancé individuellement
sys.path.insert(0, str(Path(__file__).parent.parent))

from module.pygameCore import *
from module.LANscreen import *

# %% initialisation

A1=["A2","B1"]
A2=["A1","A3","B2"]
A3=["A2","A4","B3"]
A4=["A3","A5","B4"]
A5=["A4","A6","B5"]
A6=["A5","A7","B6"]
A7=["A6","A8","B7"]
A8=["A7","A9","B8"]
A9=["A8","A10","B9"]
A10=["A9","B10"]
B1=["A1","B2","C1"]
B2=["A2","B1","B3","C2"]
B3=["A3","B2","B4","C3"]
B4=["A4","C4","B5","B3"]
B5=["A5","C5","B4","B6"]
B6=["A6","C6","B7","B5"]
B7=["A7","C7","B6","B8"]
B8=["A8","C8","B7","B9"]
B9=["A9","C9","B8","B10"]
B10=["A10","B9","C10"]
C1=["B1","C2","D1"]
C2=["D2","B2","C1","C3"]
C3=["B3","D3","C2","C4"]
C4=["B4","D4","C3","C5"]
C5=["B5","D5","C4","C6"]
C6=["D6","B6","C5","C7"]
C7=["D7","B7","C6","C8"]
C8=["C7","C9","B8","D8"]
C9=["C8","C10","B9","D9"]
C10=["C9","B10","D10"]
D1=["D2","C1","E1"]
D2=["D1","C2","E2","D3"]
D3=["D2","D4","C3","E3"]
D4=["D3","D5","E4","C4"]
D5=["D4","D5","C5","E5"]
D6=["D5","D7","C6","E6"]
D7=["D6","D8","C7","E7"]
D8=["D7","D9","C8","E8"]
D9=["D8","D10","C9","E9"]
D10=["D9","C10","E10"]
E1=["E2","D1","F1"]
E2=["E1","E3","D2","C2"]
E3=["E2","E4","D3","F3"]
E4=["E3","E5","D4","F4"]
E5=["E4","E6","F5","D5"]
E6=["E5","E7","D6","F6"]
E7=["E6","E8","D7","F7"]
E8=["E7","E9","D8","F8"]
E9=["E8","E10","F9","D9"]
E10=["F10","D10","E9"]
F1=["F2","E1","G1"]
F2=["F1","F3","G2","E2"]
F3=["F2","F4","G3","E3"]
F4=["F3","F5","G4","E4"]
F5=["F4","F6","G5","E5"]
F6=["F5","F7","G6","E6"]
F7=["F6","F8","G7","E7"]
F8=["F7","F9","G8","E8"]
F9=["F8","F10","G9","E9"]
F10=["F9","G10","E10"]
G1=["G2","F1","H1"]
G2=["G1","G3","F2","H2"]
G3=["G2","G4","F3","H3"]
G4=["G3","G5","F4","H4"]
G5=["G4","G6","F5","H5"]
G6=["G5","G7","F6","H6"]
G7=["G6","F8","F7","H7"]
G8=["G7","G9","F8","H8"]
G9=["G8","G10","F9","H9"]
G10=["G9","F10","H10"]
H1=["H2","G1","I1"]
H2=["H1","H3","G2","I2"]
H3=["H2","H4","G3","I3"]
H4=["H3","H5","G4","I4"]
H5=["H4","H6","G5","I5"]
H6=["H5","H7","G6","I6"]
H7=["H6","H8","G7","I7"]
H8=["H7","H9","G8","I8"]
H9=["H8","H10","G9","I9"]
H10=["H9","G10","I10"]
I1=["I2","H1","J1"]
I2=["I3","I1","H2","J2"]
I3=["I2","I4","H3","J3"]
I4=["I3","I5","H4","J4"]
I5=["I4","I6","H5","J5"]
I6=["I5","I7","H6","J6"]
I7=["I6","I8","H7","J7"]
I8=["I7","I9","H8","J8"]
I9=["I8","I10","H9","J9"]
I10=["I9","H10","J10"]
J1=["J2","I1"]
J2=["J1","J3","I2"]
J3=["J2","J4","I3"]
J4=["J3","J5","I4"]
J5=["J4","J6","I5"]
J6=["J5","J7","I6"]
J7=["J6","J8","I7"]
J8=["J7","J9","I8"]
J9=["J8","J10","I9"]
J10=["J9","I10"]
total=[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,H1,H2,H3,H4,H5,H6,H7,H8,H9,H10,I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,J1,J2,J3,J4,J5,J6,J7,J8,J9,J10] 

# %% fonctions

def get_coordonee(case : str) -> int:
    """Retourne les coordonnées de la case en paramètre"""

    if case[1:3] == "10":
        x = 418
    
    elif case[1] == "1":
        x = 70

    elif case[1] == "2":
        x = 110

    elif case[1] == "3":
        x = 148

    elif case[1] == "4":
        x = 185

    elif case[1] == "5":
        x = 225

    elif case[1] == "6":
        x = 263

    elif case[1] == "7":
        x = 302

    elif case[1] == "8":
        x = 340

    elif case[1] == "9":
        x = 380

    if case[0:1] == "A":
        y = 177

    elif case[0:1] == "B":
        y = 217

    elif case[0:1] == "C":
        y = 262

    elif case[0:1] == "D":
        y = 302

    elif case[0:1] == "E":
        y = 342

    elif case[0:1] == "F":
        y = 382

    elif case[0:1] == "G":
        y = 427

    elif case[0:1] == "H":
        y = 465

    elif case[0:1] == "I":
        y = 507

    elif case[0:1] == "J":
        y = 550
    
    return x,y


def get_nbr_case(lettre : str) -> int:
    """Retourne la position de la case passé en paramètre"""

    if lettre[0:1] == "A":
        case = 0
    
    if lettre[0:1] == "B":
        case = 1

    if lettre[0:1] == "C":
        case = 2

    if lettre[0:1] == "D":
        case = 3

    if lettre[0:1] == "E":
        case = 4

    if lettre[0:1] == "F":
        case = 5

    if lettre[0:1] == "G":
        case = 6

    if lettre[0:1] == "H":
        case = 7

    if lettre[0:1] == "I":
        case = 8

    if lettre[0:1] == "J":
        case = 9
    
    return case


def get_case(kijou : int) -> str:
    """Choisis une case de la grille en fonction de qui est la personne qui joue"""

    end=0
    while end==0:
        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONUP):
                x = event.pos[0]
                y = event.pos[1]
                casey = (y - 175)//41
                if kijou == 1:
                    casex = (x-70)//39
                else:
                    casex = (x-570)//39
                lettres = ['A','B','C','D','E','F','G','H',"I",'J']
                if kijou==1 and x > 72 and x < 455 and y > 173 and y < 576:
                    case = str(lettres[casey]) + str(casex+1)
                    return case 
                elif kijou==2 and x > 572 and x < 955 and y > 173 and y < 576:
                    case = str(lettres[casey]) + str(casex+1)
                    return case

            if(event.type == pygame.QUIT): 
                return "NULL"


def place_point(kijou : int, case : str, fenetre : pygame.Surface, image : str):
    """
    Place une image sur la case choisis
    - kijou : la personne qui est en train de jouer, 1 / 2
    - case : la case oû il faut afficher l'image
    - fenetre : la fenetre sur laquelle afficher le bateau
    - image : le chemin de l'image à afficher
    """
    x,y = get_coordonee(case)

    if kijou == 2:
        x = x + 500
    
    printImage(image, (40, 40), (x, y), fenetre)
    pygame.display.flip()


def printt(textes : str, fenetre : pygame.Surface, color : str):
    """Affiche le texte sur l'ecran du jeux de la couleur shouaitée"""

    printImage("./image/bataille_naval/fond texte.JPG", (1005, 100), (0,0), fenetre)
    printText(textes, 64, color, (502, 20), fenetre, Alignement="Center", police="./police/Modusa.ttf", underline=False)
    pygame.display.flip()


def place_ship(kijou : int, bateau : list, fenetre : pygame.Surface, end : bool = False):
    """
    Place l\'image du bateau voulu sur la fenetre de jeux
    - kijou : la personne qui est en train de jouer, 1 / 2
    - bateau : la liste contenant les cases du bateaux
    - fenetre : la fenetre sur laquelle afficher le bateau
    - end : si le bateau à afficher est à la fin du jeux 
    """

    if end:
        extension="R.png"
    else:
        extension=".png"
    image = "./image/bataille_naval/bateau" + str(len(bateau)) + extension
    case = bateau[0]

    x,y = get_coordonee(case)

    if kijou == 2:
        x = x + 500

    if len(bateau) == 1:
        printImage(image, (40, 40), (x, y), fenetre)
    elif bateau[0][0] == bateau[1][0]:
        printImage(image, (40*len(bateau), 40), (x, y), fenetre)
    else:
        printImage(image, (40*len(bateau), 40), (x, y), fenetre, 90)
    
    pygame.display.flip()


def place_line(kijou : int, bateau : int, fenetre : pygame.Surface):
    """
    Place une ligne sur la selection des bateaux
    - kijou : la personne qui est en train de jouer, 1 / 2
    - bateau : la liste contenant les cases du bateaux
    """

    image = "./image/bataille_naval/red line.png"
    case = bateau[0]

    x,y = get_coordonee(case)

    if kijou == 2:
        x = x + 500

    if len(bateau) == 1:
        printImage(image, (40-2, 40), (x+2, y), fenetre)
    elif bateau[0][0] == bateau[1][0]:
        printImage(image, (40*len(bateau)-10, 40), (x+2, y), fenetre)
    else:
        printImage(image, (40*len(bateau)-2, 40), (x, y), fenetre, 90)
    
    pygame.display.flip()


def copie_bateau(bateau : list) -> list:
    """retourne la copie du bateau passé en paramètre"""

    copie = []
    lettre = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    if bateau[0][0] == bateau[1][0]:
        for i in range(len(bateau)):
            place = 0
            for j in range(len(copie)):
                if int(bateau[i][1:len(bateau[i])]) > int(copie[j][1:len(copie[j])]):
                    place += 1
            copie.insert(place, bateau[i])
        return copie

    else:
        for i in range(len(bateau)):
            place = 0
            for j in range(len(copie)):
                if lettre.index(bateau[i][0]) > lettre.index(copie[j][0]):
                    place += 1
            copie.insert(place, bateau[i])
        return copie


def acote(lettre : str, choix : str) -> bool:
    """Teste si le choix est à coté de la case passé en paramètre dans lettre"""
    
    case = 0
    end = 0

    case = get_nbr_case(lettre)*10 

    chiffre = int(lettre[1:2])
    
    d10 = ["A10","B10","C10","D10","E10","F10","G10","H10","I10","J10"]
    
    if lettre in d10 :
        while(end==0): 
            if choix not in total[(chiffre + case) + 8]:
                return False
            else:
                end += 1
                return True
    else:
        while(end==0): 
            if choix not in total[(chiffre + case) - 1]:
                return False
            else:
                end += 1
                return True


def suite(case1 : str, case2 : str, choix : str, nbrcase : int) -> bool:
    """
    Teste si le choix est aligné avec 2 autres cases
    - case1 : la 1er case aligné
    - case2 : la 2e case aligné
    - choix : la case à tester
    - nbrcase : le nombre de case qui composen l'alignement
    """

    end = 0
    verifinverse = 0
    verif = 0
    result1 = 0
    result2 = 0
    lettres = ['A','B','C','D','E','F','G','H',"I",'J']
    
    case = get_nbr_case(case2)

    ret = 0
    if nbrcase == 3:
        ret = 1
    if nbrcase == 4:
        ret = 2

    d10 = ["A10","B10","C10","D10","E10","F10","G10","H10","I10","J10"]
    if case1[0:1] == choix[0:1] and case2[0:1] == choix[0:1] :
        verif = case2[0:1]
        if int(case1[1:2]) < int(case2[1:2]):
            if int(case2[1:2]) + 1 <= 10: #lui il marche 
                verifinverse = int(case2[1:2]) + 1
                result1 = verif + str(verifinverse)
            if int(case2[1:2]) - nbrcase > 0: #lui il marche
                result2 = verif + str(int(case2[1:2]) - nbrcase)
            if case1 in d10:
                verifinverse = int(case2[1:2]) + 1
                result2 = verif + str(8 - ret)
                result1 = 0
        else:
            if int(case2[1:2]) - nbrcase + 1 + ret > 0: #lui il marche
                verifinverse = int(case2[1:2]) - nbrcase + 1 + ret
                result1 = verif + str(verifinverse)
            if int(case2[1:2]) + 1 < 10: #lui il marche
                verifinverse = int(case2[1:2]) + 1 + ret
                result2 = verif + str(verifinverse+1)
            if case2 in d10:
                verifinverse = int(case2[1:2]) + 6 - ret
                result2 = verif + str(verifinverse+1)
    

    if case1[1:2] == choix[1:2] and case2[1:2] == choix[1:2] :
        verif = case2[1:2]
        if case1 < case2:
            if case + 1  < 10:
                verifinverse = lettres[case+1]
                result1 = verifinverse + verif
            if case - nbrcase > -1:
                verifinverse = lettres[case-nbrcase]
                result2 = verifinverse + verif
            if case2 in d10 and case1 in d10:
                result2 = 0
                result1 = 0
                if case-nbrcase > -1:
                    verifinverse = lettres[case-nbrcase]
                    result1 = verifinverse + str(10)
                if case+1 < 10:
                    verif = lettres[case+1]
                    result2 = verif + str(10)

        else:
            if case > 0:
                verifinverse = lettres[case-1]
                result1 =  verifinverse + verif
            if case + nbrcase < 10:
                verifinverse = lettres[case+nbrcase]
                result2 = verifinverse + verif
            if case2 in d10 and case1 in d10:
                result2 = 0
                result1 = 0
                if case-nbrcase+1 > -1:
                    if nbrcase == 2:
                        verifinverse = lettres[case-nbrcase+1]
                if case-nbrcase+2 > -1:
                    if nbrcase == 3:
                        verifinverse = lettres[case-nbrcase+2]
                if case-nbrcase+3 > -1:
                    if nbrcase == 4:
                        verifinverse = lettres[case-nbrcase+3]
                    result1 = verifinverse + str(10)
                if case+nbrcase < 10:
                    verif = lettres[case+nbrcase]
                    result2 = verif + str(10)                  

    while(end==0): 
        if choix != result1 and choix != result2: 
            
            return False
            
        else:
            end += 1
            return True


def previsual(case2 : str, case3 : str, nbrcase : int, bateau : list) -> bool:
    """
    Teste si la taille du bateau va rentrer dans la grille
    - case2 : la 1er case du bateau
    - case3 : la 2e case du bateau
    - nbrcase : la taille du bateau
    - bateau : la liste definissant le bateau
    """

    end = 0
    while (end==0):
        droite = 0
        gauche = 0
        haut = 0
        bas = 0
        lettres = ['A','B','C','D','E','F','G','H',"I",'J']
        case = get_nbr_case(case2)


        if case3 != 0:
            case1 = get_nbr_case(case3)

        droite = [20, 20, 20, 20, 20]
        gauche = [20, 20, 20, 20, 20]
        haut = [20, 20, 20, 20, 20]
        bas = [20, 20, 20, 20, 20]
        verifdroite = 0
        verifgauche = 0
        verifhaut = 0
        verifbas = 0
        ordre = 0
        ordreinverse = 0


        if case3 == 0 or case2[0] == case3[0]:
            if case3 != 0:
                if int(case2[1:len(case2)]) < int(case3[1:len(case2)]):
                    ordre = 1
                    ordreinverse = 0
                if int(case2[1:len(case2)]) > int(case3[1:len(case2)]):
                    ordre = 0
                    ordreinverse = 1
            for i in range(nbrcase):
                if case3 == 0:
                    if (int(case2[1:len(case2)]) + 1 + i + ordre < 11):
                        droite[i] = int(case2[1:len(case2)]) + 1 + i + ordre
                else:
                    if (int(case2[1:len(case2)]) + 1 + i + ordre < 11):
                        droite[i] = int(case2[1:len(case2)]) + 1 + i + ordre 
            for i in range(nbrcase):
                if case3 == 0:
                    if (int(case2[1:len(case2)]) - 1 - i - ordreinverse > 0):
                        gauche[i] = int(case2[1:len(case2)]) - 1 - i - ordreinverse   
                else:
                    if (int(case2[1:len(case2)]) - 1 - i - ordreinverse + 1 > 0):
                        gauche[i] = int(case2[1:len(case2)]) - 1 - i - ordreinverse +1

        
        if case3 == 0 or case2[1] == case3[1]:
            if case3 != 0:
                if case < case1:
                    ordre = 1
                    ordreinverse = 0
                if case > case1:
                    ordre = 0
                    ordreinverse = 1
            for i in range(nbrcase):
                if case3 == 0:
                    if (case - 1 - i - ordreinverse> -1):
                        haut[i] = case - 1 - i - ordreinverse 
                else:
                    if (case - 1 - i - ordreinverse > -1):
                        haut[i] = case - 1 - i - ordreinverse + 1
            for i in range(nbrcase):
                if case3 == 0 :
                    if (case + 1 + i + ordre < 10):
                        bas[i] = case + i + 1 + ordre 
                else:
                    if (case + 1 + i + ordre < 10):
                        bas[i] = case + i + 1 + ordre -1

        
        for i in range(nbrcase):
            if (droite[i] == 20 or str(case2[0]) + str(droite[i]) in bateau) and (droite[i] == 20 or str(case2[0]) + str(droite[i]) != case2):
                break
            verifdroite += 1
        for i in range(nbrcase):
            if (gauche[i] == 20 or str(case2[0]) + str(gauche[i]) in bateau) and (gauche[i] == 20 or str(case2[0]) + str(gauche[i]) != case2):
                break
            verifgauche += 1
            
            
            
        for i in range(nbrcase):
            if (haut[i] == 20 or (str(lettres[haut[i]]) + str(case2[1:len(case2)])) in bateau) and (haut[i] == 20 or str(lettres[haut[i]]) + str(case2[1:len(case2)]) != case2):
                break
            verifhaut += 1
        for i in range(nbrcase):
            if (bas[i] == 20 or (str(lettres[bas[i]]) + str(case2[1:len(case2)])) in bateau) and (bas[i] == 20 or str(lettres[bas[i]]) + str(case2[1:len(case2)]) != case2):
                break
            verifbas += 1
            
                
        
        ligne = verifdroite + verifgauche
        colonne = verifhaut + verifbas

    
        if ligne < nbrcase and colonne < nbrcase:
            if case3 == 0:
                return False
            else:
                
                return False
            
        elif ligne >= nbrcase or colonne >= nbrcase:
            return True

            

def notdouble(case : str, bateau : list) -> bool:
    """Teste si la case est deja utilisé dans la liste de tous les bateaux"""
    
    end = 0
    grille=["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","E1","E2","E3","E4","E5","E6","E7","E8","E9","E10","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","H1","H2","H3","H4","H5","H6","H7","H8","H9","H10","I1","I2","I3","I4","I5","I6","I7","I8","I9","I10","J1","J2","J3","J4","J5","J6","J7","J8","J9","J10"]
    while (end==0):
        if case in bateau or case not in grille:
            
            return False
        else:
            end += 1
            return True


def bataille_naval(connexion=[None, None, None]):        
    # %% main

    pygame.init()
    pygame.font.init()
    fenetre = pygame.display.set_mode((1000,600))
    fond = pygame.image.load("./image/bataille_naval/fond.jpg").convert()
    fenetre.blit(fond, (0,0))
    pygame.display.flip()
    pygame.display.set_caption("bataille navale")
    pygame_icon = pygame.image.load("./image/bataille_naval/bateau1.png")
    pygame.display.set_icon(pygame_icon)

    printImage("./image/bataille_naval/play.png", (700, 420), (160,66), fenetre)
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
            if (event.type == pygame.MOUSEBUTTONUP):
                x = event.pos[0]
                y = event.pos[1]
                if x > 161 and x < 859 and y > 298 and y < 485:
                    if connexion[0]!=None:
                        quit = waitScreen(fenetre, connexion, "#013EB0BA", "#013087B9", "bataille naval")
                        fenetre.blit(fond, (0,0))
                        printImage("./image/bataille_naval/play.png", (700, 420), (160,66), fenetre)
                        pygame.display.flip()
                        if quit=="NULL":
                            return 0
                        elif quit==1:
                            fin=1
                            conn = connexion[0]
                    else:
                        fin=1
                
            if (event.type == pygame.KEYDOWN) or (event.type == pygame.QUIT): 
                return 0

    start = 0
    while start==0:  
        end=0

        bateau=[[],[]]
        coule = [[[0], [1], [2, 2], [3], [4]], [[0], [1], [2, 2], [3], [4]]]
        bateauAll = [[[[]], [[]], [[], []], [[]], [[]]], [[[]], [[]], [[], []], [[]], [[]]]]
        copybateauAll = [[[[]], [[]], [[], []], [[]], [[]]], [[[]], [[]], [[], []], [[]], [[]]]]
        tailleBateau = [1,2,3,3,4,5]

        isbateau3 = 0
        for i in range(2):
            if conn==None or connexion[2]==True and i==0 or connexion[2]==False and i==1:
                printImage("./image/bataille_naval/grille4.png", (1000, 600), (0,0), fenetre)
                if i==0:
                    printText(nomj1, 44, "yellow", (10, 100), fenetre)
                else:
                    printText(nomj2, 44, "orange", (980, 100), fenetre, Alignement="Right")
                pygame.display.flip()
                for j in tailleBateau:
                    if j==3 and bateauAll[i][j-1][0]!=[]:
                        isbateau3=1
                        printt("2e BATEAU DE "+str(j), fenetre, "black")
                    else:
                        isbateau3=0
                        printt("BATEAU DE "+str(j), fenetre, "black")
                    for k in range(j):
                        case=get_case(i+1)
                        if case=="NULL":
                            if conn!=None:
                                conn.send(pickle.dumps(["404"]))
                            return 0
                        
                        while True:
                            if isbateau3==1:
                                printt("2e BATEAU DE "+str(j), fenetre, "black")
                            else:
                                printt("BATEAU DE "+str(j), fenetre, "black")
                            
                            if notdouble(case, bateau[i]) == False:
                                printt("case deja prise", fenetre, "red")
                                case=get_case(i+1)
                                if case=="NULL":
                                    if conn!=None:
                                        conn.send(pickle.dumps(["404"]))
                                    return 0  
                                continue
                            if k==1 and acote(bateauAll[i][j-1][isbateau3][k-1], case) == False:
                                printt("choisissez a coté", fenetre, "red")
                                case=get_case(i+1)
                                if case=="NULL":
                                    if conn!=None:
                                        conn.send(pickle.dumps(["404"]))
                                    return 0
                                continue
                            if j>2 and k==0 and previsual(case, 0, j-1, bateau[i]) == False:
                                printt("vous ne pouvez pas placer ici", fenetre, "red")
                                case=get_case(i+1)
                                if case=="NULL":
                                    if conn!=None:
                                        conn.send(pickle.dumps(["404"]))
                                    return 0
                                continue
                            if j>2 and k==1 and previsual(bateauAll[i][j-1][isbateau3][k-1], case, j-1, bateau[i]) == False:
                                printt("vous ne pouvez pas placer ici", fenetre, "red")
                                case=get_case(i+1)
                                if case=="NULL":
                                    if conn!=None:
                                        conn.send(pickle.dumps(["404"]))
                                    return 0
                                continue
                            if k>1 and suite(bateauAll[i][j-1][isbateau3][0], bateauAll[i][j-1][isbateau3][k-1], case, k) == False:
                                printt("choisissez a coté", fenetre, "red")
                                case=get_case(i+1)
                                if case=="NULL":
                                    if conn!=None:
                                        conn.send(pickle.dumps(["404"]))
                                    return 0
                                continue
                            break
                    
                        bateau[i].append(case)
                        bateauAll[i][j-1][isbateau3].append(case)
                        place_point(i+1, case, fenetre, "./image/bataille_naval/point.png")
                    if j!=1:
                        copybateauAll[i][j-1][isbateau3] = copie_bateau(bateauAll[i][j-1][isbateau3])
                        place_line(i+1, copybateauAll[i][j-1][isbateau3], fenetre)
                    else:
                        copybateauAll[i][j-1][isbateau3] = list(bateauAll[i][j-1][isbateau3])
        

        if conn!=None:
            printt("En attente de l'adversaire", fenetre, "red")
            if connexion[2]==True:
                i=1
            else:
                i=0
            send_data(connexion, pickle.dumps(bateau[(i+1)%2]), fenetre, "#013EB0BA", "#013087B9")
            liste = recv_list_data(connexion, fenetre, "#013EB0BA", "#013087B9")
            send_data(connexion, pickle.dumps(bateau[(i+1)%2]), fenetre, "#013EB0BA", "#013087B9")

            compteur=0
            for j in tailleBateau:
                if j==3 and bateauAll[i][j-1][0]!=[]:
                    isbateau3=1
                else:
                    isbateau3=0
                for k in range(j):
                    case = liste[compteur]
                    compteur +=1
                    bateau[i].append(case)
                    bateauAll[i][j-1][isbateau3].append(case)
                
                if j!=1:
                    copybateauAll[i][j-1][isbateau3] = copie_bateau(bateauAll[i][j-1][isbateau3])
                else:
                    copybateauAll[i][j-1][isbateau3] = list(bateauAll[i][j-1][isbateau3])
                    

        printImage("./image/bataille_naval/grille4.png", (1000, 600), (0,0), fenetre)
        printText(nomj1, 44, "yellow", (10, 100), fenetre)
        printText(nomj2, 44, "orange", (980, 100), fenetre, Alignement="Right")
        pygame.display.flip()

        dejaTire = [[],[]]

        kijou=1
        notkijou=2
        end=0
        while end==0:
            if kijou==1:
                printt("A "+nomj2+" de tirer", fenetre, "gold")
            else:
                printt("A "+nomj1+" de tirer", fenetre, "gold")
            if conn==None or connexion[2]==True and kijou%2 == 0 or connexion[2]==False and kijou%2 == 1:
                tir = get_case(kijou)
                if conn!=None:
                    send_data(connexion, bytes(tir, "utf-8"), fenetre, "#013EB0BA", "#013087B9")
            else:
                tir = recv_str_data(connexion, fenetre, "#013EB0BA", "#013087B9")
            if tir == "NULL":
                if conn!=None:
                    conn.send(b"404")
                return 0
            
            if tir in bateau[kijou-1] or tir in dejaTire[kijou-1]:
                for j in tailleBateau:
                    if j==3 and isbateau3==0:
                        isbateau3=1
                    else:
                        isbateau3=0


                    if tir in bateauAll[kijou-1][j-1][isbateau3] and coule[kijou-1][j-1][isbateau3] > 0:
                        coule[kijou-1][j-1][isbateau3] -= 1
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        del bateauAll[kijou-1][j-1][isbateau3][bateauAll[kijou-1][j-1][isbateau3].index(tir)]
                    elif tir in bateauAll[kijou-1][j-1][isbateau3] and coule[kijou-1][j-1][isbateau3]==0:
                        del bateauAll[kijou-1][j-1][isbateau3][bateauAll[kijou-1][j-1][isbateau3].index(tir)]
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        place_ship(kijou, copybateauAll[kijou-1][j-1][isbateau3], fenetre)
                    
                    pygame.display.flip()
                    
                    if len(bateauAll[kijou-1][0][0]) == 0 and len(bateauAll[kijou-1][1][0]) == 0 and len(bateauAll[kijou-1][2][0]) == 0 and len(bateauAll[kijou-1][2][1]) == 0 and len(bateauAll[kijou-1][3][0]) == 0 and len(bateauAll[kijou-1][4][0]) == 0:
                        if kijou==1:
                            printt("Victoire de "+nomj2, fenetre, "green")
                        else: 
                            printt("Victoire de "+nomj1, fenetre, "green")
                        end += 1
                        if len(bateauAll[notkijou-1][0][0]) !=0:
                            place_ship(notkijou, copybateauAll[notkijou-1][0][0], fenetre, True)
                        if len(bateauAll[notkijou-1][1][0]) !=0:
                            place_ship(notkijou, copybateauAll[notkijou-1][1][0], fenetre, True)
                        if len(bateauAll[notkijou-1][2][0]) !=0:
                            place_ship(notkijou, copybateauAll[notkijou-1][2][0], fenetre, True)
                        if len(bateauAll[notkijou-1][2][1]) !=0:
                            place_ship(notkijou, copybateauAll[notkijou-1][2][1], fenetre, True)
                        if len(bateauAll[notkijou-1][3][0]) !=0:
                            place_ship(notkijou, copybateauAll[notkijou-1][3][0], fenetre, True)
                        if len(bateauAll[notkijou-1][4][0]) !=0:
                            place_ship(notkijou, copybateauAll[notkijou-1][4][0], fenetre, True)


                        bille = pygame.image.load("./image/bataille_naval/rejouer.png").convert_alpha()
                        bille = pygame.transform.scale(bille, (40, 40))
                        position_bille = [10,10] 
                        fenetre.blit(bille, position_bille)
                        pygame.display.flip()

                        break

            else:
                dejaTire[kijou-1].append(tir)
                place_point(kijou, tir, fenetre, "./image/bataille_naval/cross.png")
                if kijou==1:
                    kijou = 2
                    notkijou=1
                else:
                    notkijou = 2
                    kijou=1
                
        
        end = 0
        while end==0:
            for event in pygame.event.get():
                if(event.type == pygame.QUIT): 
                    if conn!=None:
                        conn.send(pickle.dumps(["404"]))
                    return 0
                
                if (event.type == pygame.MOUSEBUTTONUP):
                    x = event.pos[0]
                    y = event.pos[1]
                    if y > 10 and y < 50 and x > 10 and x < 50:
                        end = 1


if __name__ == "__main__":
    bataille_naval()



            
    