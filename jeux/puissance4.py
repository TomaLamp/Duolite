from pygame import *
from module.pygameCore import *
import pygame

def puissance4():
    def get_ligne():
        pygame.init()
        end = 0
        while end==0:
            for event in pygame.event.get():
                if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]
                        if y>124 and y<571:
                            if x>236 and x<310:
                                return 1
                            elif x>310 and x<385:
                                return 2
                            elif x>385 and x<461:
                                return 3
                            elif x>461 and x<535:
                                return 4
                            elif x>535 and x<611:
                                return 5
                            elif x>611 and x<686:
                                return 6
                            elif x>686 and x<761:
                                return 7
                            
                        
                if (event.type == KEYDOWN) or (event.type == QUIT): 
                    return "NULL"
                    
                        

    def place_point(kijou, ligne, case):
        if kijou%2 == 1:
            pion = "./image/puissance4/rouge.png"
        else:
            pion = "./image/puissance4/jaune.png"

    
        x = 250 + (ligne-1)*75
        y = 510 - (case-1)*75

        printImage(pion, (50, 50), (x, y), fenetre, 90)
        pygame.display.flip()


    fenetre = initScreen((1000,600), "Puissance 4", "#A2B203", "./image/puissance4/icon.png")
    printImage("./image/puissance4/play.png", (600, 442.5), (200,80), fenetre)
    pygame.display.flip()

    nomj1, nomj2 = get_nom()

    fin = 0
    while fin == 0:
        for event in pygame.event.get():
            if (event.type == MOUSEBUTTONUP):
                    x = event.pos[0]
                    y = event.pos[1]
                    if x > 200 and x < 789 and y > 337 and y < 521:
                        fin = 1 
            
            if (event.type == KEYDOWN) or (event.type == QUIT): 
                    return 0


    kijou=1
    point_rouge = 0
    point_jaune = 0

    fin = 0
    while fin== 0:
        grille = [['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F'], ['F', 0, 0, 0, 0, 0, 0, 'F'], ['F', 0, 0, 0, 0, 0, 0, 'F'], 
        ['F', 0, 0, 0, 0, 0, 0, 'F'], ['F', 0, 0, 0, 0, 0, 0, 'F'], ['F', 0, 0, 0, 0, 0, 0, 'F'], ['F', 0, 0, 0, 0, 0, 0, 'F'], ['F', 0, 0, 0, 0, 0, 0, 'F'], ['F', 'F', 'F', 'F', 'F', 'F', 'F', 'F']]
        
        

        fenetre.fill("#A2B203")
        printImage("./image/puissance4/grille.png", (462, 540), (230, 120), fenetre, 90)
        pygame.display.flip()
        end = 0
        while end==0:

            if kijou%2 == 1:
                colors = "red"
                couleur = nomj1  
            else: 
                colors = "yellow"
                couleur = nomj2
            
            printText("Au tour de " + couleur, 64, colors, (500, 10), fenetre, police="./police/adventure.otf", Alignement="Center")
            printText(nomj1+" : ", 44, "red", (10, 300), fenetre, police="./police/adventure.otf")
            printText(str(point_rouge), 54, "black", (10, 350), fenetre, police="./police/adventure.otf")
            printText(nomj2+" :", 44, "yellow", (990, 300), fenetre, police="./police/adventure.otf", Alignement="Right")
            printText(str(point_jaune), 54, "black", (955, 350), fenetre, police="./police/adventure.otf")
            pygame.display.flip()

            choix = False
            while not choix:

                prop = get_ligne()
                if prop=="NULL":
                    return 0

                for i in range(1, len(grille[prop])):
                    if grille[prop][i] == 0:
                        if kijou%2 == 1:
                            grille[prop][i] = nomj1
                            choix = True
                            j = i
                            break
                        else:
                            grille[prop][i] = nomj2
                            choix = True
                            j = i
                            break

            
                
            place_point(kijou, prop, i)

            nbr = 0
            haut = 0
            bas = 0
            droite = 0
            gauche = 0
            hautGauche = 0
            basDroite = 0
            basGauche = 0
            hautDroite = 0
            
            while grille[prop][j+nbr] == couleur and nbr < 4:
                haut += 1
                nbr += 1
            
            nbr = 1
            while grille[prop][j-nbr] == couleur and nbr < 4:
                bas += 1
                nbr += 1

                

            nbr = 0
            while  grille[prop+nbr][j] == couleur and nbr < 4:
                droite += 1
                nbr += 1
            
            nbr = 1    
            while grille[prop-nbr][j] == couleur and nbr < 4 :
                gauche += 1
                nbr += 1

                

            nbr = 0
            while  grille[prop-nbr][j+nbr] == couleur and nbr < 4:
                hautGauche += 1
                nbr += 1
            
            nbr = 1
            while grille[prop+nbr][j-nbr] == couleur and nbr < 4 :
                basDroite += 1
                nbr += 1



            nbr = 0
            while grille[prop+nbr][j+nbr] == couleur and nbr < 4:
                hautDroite += 1
                nbr += 1
            
            nbr = 1   
            while grille[prop-nbr][j-nbr] == couleur and nbr < 4:
                basGauche += 1
                nbr += 1

            printImage("./image/puissance4/fond.png", (1000, 100), (0, 0), fenetre)
            pygame.display.flip()

            if hautDroite + basGauche > 3 or hautGauche + basDroite > 3 or droite+gauche > 3 or haut+bas > 3:
                if kijou%2 == 1:
                    point_rouge += 1
                else: 
                    point_jaune += 1
                
                printText(couleur +" a gagné ", 64, colors, (500, 10), fenetre, police="./police/adventure.otf", Alignement="Center")
                pygame.display.flip()

                end = 1
                nbr = 0
                nbr2 = 0
                rot = 0
                longueur = 0
                if hautDroite + basGauche > 3:
                    while grille[prop+nbr][j+nbr2] == couleur:
                        nbr+=1
                        nbr2+=1
                        rot = 45
                        longueur = 75
                    nbr -= 5
                    nbr2 -= 0.9
                
                if hautGauche + basDroite > 3:
                    nbr = 0
                    nbr2 = 0
                    while grille[prop+nbr][j+nbr2] == couleur:
                        nbr-=1
                        nbr2+=1
                        rot = -45
                        longueur = 75
                    nbr -= 0
                    nbr2 -= 1
                
                if droite+gauche > 3:
                    nbr = 0
                    nbr2 = 0
                    while grille[prop+nbr][j+nbr2] == couleur:
                        nbr-=1
                        rot = 0
                
                if haut+bas > 3:
                    nbr = 0
                    nbr2 = 0
                    while grille[prop+nbr][j+nbr2] == couleur:
                        nbr2+=1
                        rot = 90
                    nbr -= 1
                    nbr2 -= 1

                x = 250 + (prop+nbr)*75
                y = 510 - (j+nbr2-1)*75

                printImage("./image/puissance4/red line.png", (4*75-25+longueur, 50), (x, y), fenetre, rot)
                pygame.display.flip()

            c = 0
            for i in range(len(grille)):
                for j in range(len(grille[i])):
                    if grille[i][j] == 0:
                        break
                    else:
                        c += 1

            
            if c==len(grille)*len(grille[1]) and (hautDroite + basGauche < 4 and hautGauche + basDroite < 4 and droite+gauche < 4 and haut+bas < 4):
                printText("Egalité", 84, "black", (500, 10), fenetre, police="./police/adventure.otf", Alignement="Center")
                end=1

            
            kijou += 1    

        printImage("./image/puissance4/rejouer.png", (200, 53.8), (10, 500), fenetre)
        pygame.display.flip()

        end = 0
        while end==0:
            for event in pygame.event.get():
                if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]
                        if x>10 and x<2001 and y>500 and y<554:
                            end = 1

                if (event.type == KEYDOWN):
                    if event.key == K_RETURN:
                        end = 1
                                
                if(event.type == QUIT): 
                        return 0
                
if __name__ == "__main__":
    puissance4()