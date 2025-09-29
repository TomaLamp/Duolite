from pygame import *
import pygame

def morpion():
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

        bille = pygame.image.load(pion).convert_alpha()
        bille = pygame.transform.scale(bille, (120, 120))
        bille = pygame.transform.rotate(bille, 90)
        position_bille = [x, y] 
        fenetre.blit(bille, position_bille)
        pygame.display.flip()


    pygame.init()
    pygame.font.init()
    fenetre = pygame.display.set_mode((1000,600))
    fenetre.fill("#FAF723")
    pygame.display.set_caption("Morpion")
    pygame_icon = pygame.image.load("./image/morpion/icon.jpg")
    pygame.display.set_icon(pygame_icon)
    pygame.display.flip()


    bille = pygame.image.load("./image/morpion/play.png").convert_alpha()
    bille = pygame.transform.scale(bille, (600, 522.97))
    fenetre.blit(bille, (220,20))
    pygame.display.flip()

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

        bille = pygame.image.load("./image/morpion/grille.png").convert_alpha()
        bille = pygame.transform.scale(bille, (350, 350))
        bille = pygame.transform.rotate(bille, 90)
        position_bille = [320, 220] 
        fenetre.blit(bille, position_bille)
        pygame.display.flip()

        grille = [['F', 'F', 'F', 'F', 'F'], ['F', 0, 0, 0, 'F'], ['F', 0, 0, 0, 'F'], 
        ['F', 0, 0, 0, 'F'], ['F', 'F', 'F', 'F', 'F']]

        
        
        end = 0
        while end==0:

            if kijou%2 == 1:
                couleur = "O"  
            else: 
                couleur = "X"
            
            police = pygame.font.Font("./police/Lemon Tea.ttf", 64)
            texte = police.render("Au tour de " + couleur,True, "black")
            fenetre.blit(texte, (300, 10))

            police = pygame.font.Font("./police/Lemon Tea.ttf", 64)
            texte = police.render("Rond : ",True, "black")
            fenetre.blit(texte, (10, 300))

            police = pygame.font.Font("./police/Lemon Tea.ttf", 64)
            texte = police.render(str(point_rouge) ,True, "black")
            fenetre.blit(texte, (10, 370))


            police = pygame.font.Font("./police/Lemon Tea.ttf", 64)
            texte = police.render("Croix : ",True, "black")
            fenetre.blit(texte, (805, 300))

            police = pygame.font.Font("./police/Lemon Tea.ttf", 64)
            texte = police.render(str(point_jaune) ,True, "black")
            fenetre.blit(texte, (945, 370))
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



            bille = pygame.image.load("./image/morpion/fond.png").convert_alpha()
            bille = pygame.transform.scale(bille, (500, 100))
            position_bille = [300, 0] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip()
            

            if hautDroite + basGauche > 2 or hautGauche + basDroite > 2 or droite+gauche > 2 or haut+bas > 2:
                if kijou%2 == 1:
                    point_rouge += 1
                else: 
                    point_jaune += 1

                police = pygame.font.Font("./police/Lemon Tea.ttf", 78)
                texte = police.render("Gagné " + couleur,True,pygame.Color("#288300"))
                rectTexte = texte.get_rect()
                fenetre.blit(texte, (390, 10))
                pygame.display.flip()
                
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
                police = pygame.font.Font("./police/Lemon Tea.ttf", 78)
                texte = police.render("Egalité",True,pygame.Color("red"))
                rectTexte = texte.get_rect()
                fenetre.blit(texte, (390, 10))
                pygame.display.flip()
                

            
            kijou += 1

        bille = pygame.image.load("./image/morpion/rejouer.png").convert_alpha()
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