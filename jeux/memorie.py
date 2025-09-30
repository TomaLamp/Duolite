from pygame import *
import pygame
from random import *
from module.pygameCore import *


def memory():

    fenetre = initScreen((1000,600), "memorie", "red", './image/memorie/icon.png')


    printImage("./image/memorie/play.png", (700, 350.315), (150,110), fenetre)
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
                printImage("./image/memorie/dos.png", (80, 80), [200+100*j,85+85*i], fenetre)
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

            printImage("./image/memorie/suivant.png", (200, 53.678), [790,530], fenetre)
            printImage("./image/memorie/rouge.png", (500, 50), [300,20], fenetre)
            printText("Au tour du "+joueur, 62, couleur, (300, 20), fenetre)
            printText("joueur 1 :", 40, "black", (10, 200), fenetre, underline=True)
            printText("joueur 2 :", 40, "black", (860, 200), fenetre, underline=True)
            printImage("./image/memorie/rouge.png", (50, 50), [20,250], fenetre)
            printImage("./image/memorie/rouge.png", (50, 50), [960,250], fenetre)
            printText(str(point1), 40, "black", (20, 250), fenetre)
            printText(str(point2), 40, "black", (960, 250), fenetre)
                                
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
                                printImage(f"./image/memorie/cartes/mem{k}.jpg", (80, 80), [200+100*i,85+85*j], fenetre)
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

                                        printImage("./image/memorie/rouge.png", (50, 50), [20,250], fenetre)
                                        printImage("./image/memorie/rouge.png", (50, 50), [960,250], fenetre)
                                        printText(str(point1), 40, "black", (20, 250), fenetre)
                                        printText(str(point2), 40, "black", (960, 250), fenetre)
                                        
                                        
                                        printImage("./image/memorie/rouge.png", (500, 50), [300,20], fenetre)

                                        if point1!=point2:
                                            printText("Victoire du "+vic, 62, "#4E8102", (300, 20), fenetre)
                                        else:
                                            printText("Egalité", 62, "#4E8102", (430, 20), fenetre)

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

                                    printImage("./image/memorie/dos.png", (80, 80), [200+100*i,85+85*j], fenetre)
                                    printImage("./image/memorie/dos.png", (80, 80), [200+100*i1,85+85*j1], fenetre)

        

                                

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
                
if __name__ == "__main__":
    memory()