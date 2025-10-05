from pygame import *
import pygame
from module.pygameCore import *

def morpion():

    # %% fonctions

    def get_case():
        end = 0
        while end==0:
            for event in pygame.event.get():
                if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]
                        if x>322 and x<439 and y>220 and y<332:
                            return 0
                        elif x>439 and x<555 and y>220 and y<332:
                            return 1
                        elif x>555 and x<669 and y>220 and y<332:
                            return 2
                        elif x>322 and x<439 and y>332 and y<450:
                            return 3
                        elif x>439 and x<555 and y>332 and y<450:
                            return 4
                        elif x>555 and x<669 and y>332 and y<450:
                            return 5
                        elif x>322 and x<439 and y>450 and y<566:
                            return 6
                        elif x>439 and x<555 and y>450 and y<566:
                            return 7
                        elif x>555 and x<669 and y>450 and y<566:
                            return 8
                            
                        
                if (event.type == KEYDOWN) or (event.type == QUIT): 
                    return "NULL"

    def place_point(kijou, ligne, case):
        if kijou%2 == 1:
            pion = "./image/morpion/rond.png"
        else:
            pion = "./image/morpion/croix.png"
    
        x = 200 + (case)*120
        y = 110 + (ligne)*110

        printImage(pion, (120, 120), [x, y], fenetre, rotation=90)


    # %% main

    fenetre = initScreen((1000,600), "Morpion", "#FAF723", "./image/morpion/icon.jpg")
    printImage("./image/morpion/play.png", (600, 522.97), [220, 20], fenetre)
    pygame.display.flip()

    nomj1, nomj2 = get_nom()
    
    fin = 0
    while fin == 0:
        for event in pygame.event.get():
            if (event.type == MOUSEBUTTONUP):
                    x = event.pos[0]
                    y = event.pos[1]
                    if x > 220 and x < 809 and y > 337 and y < 521:
                        fin = 1 
            
            if (event.type == KEYDOWN) or (event.type == QUIT): 
                    return 0




    kijou=1
    point_rouge = 0
    point_jaune = 0

    fin = 0
    while fin== 0:
        fenetre.fill("#FAF723")
        printImage("./image/morpion/grille.png", (350, 350), [320, 220], fenetre, rotation=90)
        pygame.display.flip()

        grille = [['F', 'F', 'F', 'F', 'F'], ['F', 0, 0, 0, 'F'], ['F', 0, 0, 0, 'F'], 
        ['F', 0, 0, 0, 'F'], ['F', 'F', 'F', 'F', 'F']]

        
        
        end = 0
        while end==0:

            if kijou%2 == 1:
                couleur = nomj1  
            else: 
                couleur = nomj2
            
            printText("Au tour de " + couleur, 64, "black", (500, 10), fenetre, police="./police/Lemon Tea.ttf", Alignement="Center")
            printText(nomj1 + " : ", 44, "black", (10, 300), fenetre, police="./police/Lemon Tea.ttf")
            printText(str(point_rouge), 64, "black", (10, 370), fenetre, police="./police/Lemon Tea.ttf")
            printText(nomj2+" : ", 44, "black", (995, 300), fenetre, police="./police/Lemon Tea.ttf", Alignement="Right")
            printText(str(point_jaune), 64, "black", (945, 370), fenetre, police="./police/Lemon Tea.ttf")
            pygame.display.flip()

            choix = False
            while not choix:
                prop = get_case()
                if prop=="NULL":
                    return 0

                if grille[prop//3+1][prop%3+1] == 0:
                    grille[prop//3+1][prop%3+1] = couleur
                    choix = True

            
            place_point(kijou, prop//3+1, prop%3+1)    

            j=prop%3+1
            nbr = 0
            haut = 0
            bas = 0
            droite = 0
            gauche = 0
            hautGauche = 0
            basDroite = 0
            basGauche = 0
            hautDroite = 0
            
            while grille[prop//3+1][j+nbr] == couleur and nbr < 3:
                droite += 1
                nbr += 1
            
            nbr = 1
            while grille[prop//3+1][j-nbr] == couleur and nbr < 3:
                gauche += 1
                nbr += 1

                

            nbr = 0
            while  grille[prop//3+1+nbr][j] == couleur and nbr < 3:
                haut += 1
                nbr += 1
            
            nbr = 1    
            while grille[prop//3+1-nbr][j] == couleur and nbr < 3:
                bas += 1
                nbr += 1

                

            nbr = 0
            while  grille[prop//3+1-nbr][j+nbr] == couleur and nbr < 3:
                basDroite += 1
                nbr += 1
            
            nbr = 1
            while grille[prop//3+1+nbr][j-nbr] == couleur and nbr < 3:
                hautGauche += 1
                nbr += 1



            nbr = 0
            while grille[prop//3+1+nbr][j+nbr] == couleur and nbr < 3:
                hautDroite += 1
                nbr += 1
            
            nbr = 1   
            while grille[prop//3+1-nbr][j-nbr] == couleur and nbr < 3:
                basGauche += 1
                nbr += 1



            printImage("./image/morpion/fond.png", (1000, 100), [0, 0], fenetre)
            

            if hautDroite + basGauche > 2 or hautGauche + basDroite > 2 or droite+gauche > 2 or haut+bas > 2:
                if kijou%2 == 1:
                    point_rouge += 1
                else: 
                    point_jaune += 1

                printText(couleur + " a gagné ", 78, "#288300", (500, 10), fenetre, police="./police/Lemon Tea.ttf", Alignement="Center")
                
                end = 1
                

            c = 0
            for i in range(len(grille)):
                for j in range(len(grille[i])):
                    if grille[i][j] == 0:
                        break
                    else:
                        c += 1

            
            if c==len(grille)*len(grille[1]) and (hautDroite + basGauche < 3 and hautGauche + basDroite < 3 and droite+gauche < 3 and haut+bas < 3):
                end=1
                printText("Egalité", 78, "red", (390, 10), fenetre, police="./police/Lemon Tea.ttf")
                

            
            kijou += 1

        printImage("./image/morpion/rejouer.png", (300, 80.71), [10, 500], fenetre)
        pygame.display.flip()

        end = 0
        while end==0:
            for event in pygame.event.get():
                if (event.type == MOUSEBUTTONUP):
                    x = event.pos[0]
                    y = event.pos[1]
                    if x>10 and x<309 and y>500 and y<589:
                        end = 1
                if(event.type == QUIT): 
                    return 0
            
if __name__ == "__main__":
    morpion()