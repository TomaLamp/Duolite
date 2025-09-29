from pickle import TRUE
from pygame import *
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

        bille = pygame.image.load(pion).convert_alpha()
        bille = pygame.transform.scale(bille, (50, 50))
        bille = pygame.transform.rotate(bille, 90)
        position_bille = [x, y] 
        fenetre.blit(bille, position_bille)
        pygame.display.flip()



    pygame.init()
    pygame.font.init()
    fenetre = pygame.display.set_mode((1000,600))
    fenetre.fill("#A2B203")
    pygame.display.set_caption("Puissance 4")
    pygame_icon = pygame.image.load("./image/puissance4/icon.png")
    pygame.display.set_icon(pygame_icon)
    pygame.display.flip()

    bille = pygame.image.load("./image/puissance4/play.png").convert_alpha()
    bille = pygame.transform.scale(bille, (600, 442.5))
    fenetre.blit(bille, (200,80))
    pygame.display.flip()

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
        pygame.display.flip()

        bille = pygame.image.load("./image/puissance4/grille.png").convert_alpha()
        bille = pygame.transform.scale(bille, (462, 540))
        bille = pygame.transform.rotate(bille, 90)
        position_bille = [230, 120] 
        fenetre.blit(bille, position_bille)
        pygame.display.flip()
        end = 0
        while end==0:

            if kijou%2 == 1:
                colors = "red"
                couleur = "rouge"  
            else: 
                colors = "yellow"
                couleur = "jaune"
            
            police = pygame.font.Font("./police/adventure.otf", 64)
            texte = police.render("Au tour du " + couleur,True, colors)
            fenetre.blit(texte, (280, 10))
            pygame.display.flip()

            police = pygame.font.Font("./police/adventure.otf", 44)
            texte = police.render("Rouge : ",True, "red")
            fenetre.blit(texte, (10, 300))
            pygame.display.flip()

            police = pygame.font.Font("./police/adventure.otf", 54)
            texte = police.render(str(point_rouge) ,True, "black")
            fenetre.blit(texte, (10, 350))
            pygame.display.flip()


            police = pygame.font.Font("./police/adventure.otf", 44)
            texte = police.render("Jaune : ",True, "yellow")
            fenetre.blit(texte, (860, 300))
            pygame.display.flip()

            police = pygame.font.Font("./police/adventure.otf", 54)
            texte = police.render(str(point_jaune) ,True, "black")
            fenetre.blit(texte, (955, 350))
            pygame.display.flip()

            


            choix = False
            while not choix:

                prop = get_ligne()
                if prop=="NULL":
                    return 0

                for i in range(1, len(grille[prop])):
                    if grille[prop][i] == 0:
                        if kijou%2 == 1:
                            grille[prop][i] = "rouge"
                            choix = TRUE
                            j = i
                            break
                        else:
                            grille[prop][i] = "jaune"
                            choix = TRUE
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

            
            bille = pygame.image.load("./image/puissance4/fond.png").convert_alpha()
            bille = pygame.transform.scale(bille, (500, 100))
            position_bille = [300, 0] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip()

            

            if hautDroite + basGauche > 3 or hautGauche + basDroite > 3 or droite+gauche > 3 or haut+bas > 3:
                if kijou%2 == 1:
                    point_rouge += 1
                else: 
                    point_jaune += 1
                police = pygame.font.Font("./police/adventure.otf", 64)
                texte = police.render("Gagné " + couleur,True, colors)
                fenetre.blit(texte, (370, 10))
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

                bille = pygame.image.load("./image/puissance4/red line.png").convert_alpha()
                bille = pygame.transform.scale(bille, (4*75-25+longueur, 50))
                bille = pygame.transform.rotate(bille, rot)
                position_bille = [x, y] 
                fenetre.blit(bille, position_bille)
                pygame.display.flip()

            c = 0
            for i in range(len(grille)):
                for j in range(len(grille[i])):
                    if grille[i][j] == 0:
                        break
                    else:
                        c += 1

            
            if c==len(grille)*len(grille[1]) and (hautDroite + basGauche < 4 and hautGauche + basDroite < 4 and droite+gauche < 4 and haut+bas < 4):
                police = pygame.font.Font("./police/adventure.otf", 84)
                texte = police.render("Egalité",True, "black")
                fenetre.blit(texte, (390, 10))
                pygame.display.flip()
                end=1

            
            kijou += 1    

        bille = pygame.image.load("./image/puissance4/rejouer.png").convert_alpha()
        bille = pygame.transform.scale(bille, (300, 80.71))
        position_bille = [10, 10] 
        fenetre.blit(bille, position_bille)
        pygame.display.flip()

        end = 0
        while end==0:
            for event in pygame.event.get():
                if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]
                        if x>10 and x<309 and y>10 and y<89:
                            end = 1
                            
                                
                if(event.type == QUIT): 
                        return 0