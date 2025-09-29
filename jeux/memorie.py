from pygame import *
import pygame
from random import *


def memory():

    pygame.init()
    pygame.font.init()
    fenetre = pygame.display.set_mode((1000,600))
    fenetre.fill("red")
    pygame.display.set_caption("memorie")
    pygame_icon = pygame.image.load('./image/memorie/icon.png')
    pygame.display.set_icon(pygame_icon)



    bille = pygame.image.load("./image/memorie/play.png").convert_alpha()
    bille = pygame.transform.scale(bille, (700, 350.315))
    fenetre.blit(bille, (150,110))
    pygame.display.flip()
                

    fin = 0
    while fin == 0:
        for event in pygame.event.get():
            if (event.type == MOUSEBUTTONUP):
                x = event.pos[0]
                y = event.pos[1]
                if x > 150 and x < 850 and y > 110 and y < 461:
                    fin = 1 
                            
            if (event.type == KEYDOWN) or (event.type == QUIT): 
                return 0




    fenetre.fill("red")
    restart=0
    while restart==0:

        carte = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10, 11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 18]
        placement = [[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]

        for j in range(6):
            for i in range(6):
                r = randint(0, len(carte)-1)
                placement[j][i] = carte[r]
                del(carte[r])

        print(placement)

        c=0
        for j in range(6):
            for i in range(6):
                k = placement[j][i]
                bille = pygame.image.load("./image/memorie/dos.png").convert_alpha()
                bille = pygame.transform.scale(bille, (80, 80))
                position_bille = [200+100*j,85+85*i] 
                fenetre.blit(bille, position_bille)
                pygame.display.flip()

                c+=1


        count=0
        fin = 0
        kijou=0
        point1 = 0
        point2 = 0
        while fin == 0:

            if kijou%2==0:
                joueur = "joueur 1"
                couleur = "green"
            else:
                joueur = "joueur 2"
                couleur = "yellow"

            bille = pygame.image.load("./image/memorie/suivant.png").convert_alpha()
            bille = pygame.transform.scale(bille, (200, 53.678))
            position_bille = [790,530] 
            fenetre.blit(bille, position_bille)

            bille = pygame.image.load("./image/memorie/rouge.png").convert_alpha()
            bille = pygame.transform.scale(bille, (500, 50))
            position_bille = [300,20] 
            fenetre.blit(bille, position_bille)

            police = pygame.font.Font(None, 62)
            texte = police.render("Au tour du "+joueur,True, couleur)
            fenetre.blit(texte, (300, 20))

            police = pygame.font.Font(None, 40)
            police.underline = True
            texte = police.render("joueur 1 :",True, "black")
            fenetre.blit(texte, (10, 200))

            police = pygame.font.Font(None, 40)
            police.underline = True
            texte = police.render("joueur 2 :",True, "black")
            fenetre.blit(texte, (860, 200))

            bille = pygame.image.load("./image/memorie/rouge.png").convert_alpha()
            bille = pygame.transform.scale(bille, (50, 50))
            position_bille = [20,250] 
            fenetre.blit(bille, position_bille)

            bille = pygame.image.load("./image/memorie/rouge.png").convert_alpha()
            bille = pygame.transform.scale(bille, (50, 50))
            position_bille = [960,250] 
            fenetre.blit(bille, position_bille)

            police = pygame.font.Font(None, 40)
            texte = police.render(str(point1),True, "black")
            fenetre.blit(texte, (20, 250))

            police = pygame.font.Font(None, 40)
            texte = police.render(str(point2),True, "black")
            fenetre.blit(texte, (960, 250))
                                
            pygame.display.flip()
            i=-1
            j=-1

            for event in pygame.event.get():
                if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]
                        if y>85 and y<162:
                            j=0
                        if y>170 and y<248:
                            j=1
                        if y>254 and y<333:
                            j=2
                        if y>340 and y<418:
                            j=3
                        if y>426 and y<503:
                            j=4
                        if y>512 and y<588:
                            j=5
                        
                        if x>200 and x<278:
                            i=0
                        if x>298 and x<380:
                            i=1
                        if x>398 and x<480:
                            i=2
                        if x>500 and x<579:
                            i=3
                        if x>600 and x<679:
                            i=4
                        if x>702 and x<780:
                            i=5

                        
                        if i!=-1 and j!=-1:
                            k = placement[i][j]
                            if k!= 0:
                                bille = pygame.image.load("./image/memorie/cartes/mem"+str(k)+".jpg").convert_alpha()
                                bille = pygame.transform.scale(bille, (80, 80))
                                position_bille = [200+100*i,85+85*j] 
                                fenetre.blit(bille, position_bille)
                                pygame.display.flip()


                            count+=1

                            if count%2 == 1:
                                i1 = i
                                j1 = j 
                            
                            if count%2 == 0:
                                if placement[i1][j1] == placement[i][j]:
                                    placement[i1][j1] = 0
                                    placement[i][j] = 0

                                    if kijou%2==0:
                                        point1+=1
                                    else:
                                        point2+=1

                                    if placement ==  [[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0]]:
                                        
                                        if point1>point2:
                                            vic = "joueur 1"
                                        elif point1<point2:
                                            vic = "joueur 2"

                                        bille = pygame.image.load("./image/memorie/rouge.png").convert_alpha()
                                        bille = pygame.transform.scale(bille, (50, 50))
                                        position_bille = [20,250] 
                                        fenetre.blit(bille, position_bille)

                                        bille = pygame.image.load("./image/memorie/rouge.png").convert_alpha()
                                        bille = pygame.transform.scale(bille, (50, 50))
                                        position_bille = [960,250] 
                                        fenetre.blit(bille, position_bille)

                                        police = pygame.font.Font(None, 40)
                                        texte = police.render(str(point1),True, "black")
                                        fenetre.blit(texte, (20, 250))

                                        police = pygame.font.Font(None, 40)
                                        texte = police.render(str(point2),True, "black")
                                        fenetre.blit(texte, (960, 250))
                                        
                                        
                                        bille = pygame.image.load("./image/memorie/rouge.png").convert_alpha()
                                        bille = pygame.transform.scale(bille, (500, 50))
                                        position_bille = [300,20] 
                                        fenetre.blit(bille, position_bille)

                                        if point1!=point2:
                                            police = pygame.font.Font(None, 62)
                                            texte = police.render("Victoire du "+vic,True, "#4E8102")
                                            fenetre.blit(texte, (300, 20))
                                        else:
                                            police = pygame.font.Font(None, 62)
                                            texte = police.render("Egalité",True, "#4E8102")
                                            fenetre.blit(texte, (430, 20))

                                        pygame.display.flip()

                                        end=0
                                        while end==0:
                                            for event in pygame.event.get():
                                                if (event.type == MOUSEBUTTONUP):
                                                        x = event.pos[0]
                                                        y = event.pos[1]
                                                        if x<990 and x>790 and y>530 and y<583:
                                                            end=1
                                                            fin=1

                                                if (event.type == QUIT): 
                                                    return 0

                                else:
                                    kijou+=1

                                    bille = pygame.image.load("./image/memorie/dos.png").convert_alpha()
                                    bille = pygame.transform.scale(bille, (80, 80))
                                    position_bille = [200+100*i,85+85*j] 
                                    fenetre.blit(bille, position_bille)

                                    bille = pygame.image.load("./image/memorie/dos.png").convert_alpha()
                                    bille = pygame.transform.scale(bille, (80, 80))
                                    position_bille = [200+100*i1,85+85*j1] 
                                    fenetre.blit(bille, position_bille)

        

                                

                                    end=0
                                    while end==0:
                                        for event in pygame.event.get():
                                            if (event.type == MOUSEBUTTONUP):
                                                    x = event.pos[0]
                                                    y = event.pos[1]
                                                    if x<990 and x>790 and y>530 and y<583:
                                                        end=1

                                            if (event.type == QUIT): 
                                                return 0
                            
                if (event.type == QUIT): 
                    return 0