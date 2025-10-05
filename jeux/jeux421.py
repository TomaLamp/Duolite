from pygame import *
import pygame
from math import *
from time import *
from module.pygameCore import *


def jeux421():

    import random
    from time import sleep

    def tirage(d1, d2, d3):

        l = [0, 0, 0]
        if d1==1:
            l[0] = random.randint(1, 6)
        if d2==1:
            l[1] = random.randint(1, 6)
        if d3==1:
            l[2] = random.randint(1, 6)

        return l

    def affich(l, score):

        if score[0]==0:
            for i in range(10):
                a = random.randint(1,6)
                printImage("./image/421/de"+str(a)+".jpg", (100, 100), [200, 200], fenetre)
                pygame.display.flip()
                sleep(0.1)

            printImage("./image/421/de"+str(l[0])+".jpg", (100, 100), [200, 200], fenetre)
            pygame.display.flip()
        
        if score[1]==0:
            for i in range(10):
                a = random.randint(1,6)
                printImage("./image/421/de"+str(a)+".jpg", (100, 100), [450, 200], fenetre)
                pygame.display.flip()
                sleep(0.1)

            printImage("./image/421/de"+str(l[1])+".jpg", (100, 100), [450, 200], fenetre)
            pygame.display.flip()

        if score[2]==0:
            for i in range(10):
                a = random.randint(1,6)
                printImage("./image/421/de"+str(a)+".jpg", (100, 100), [700, 200], fenetre)
                pygame.display.flip()
                sleep(0.1)


            printImage("./image/421/de"+str(l[2])+".jpg", (100, 100), [700, 200], fenetre)
        
        pygame.display.flip()


    def keep(d, pos, val):
        if d==1:
            l='R'
        else:
            l=''

        p=[200, 450, 700] 
        printImage("./image/421/de"+l+str(val)+".jpg", (100, 100), [p[pos-1], 200], fenetre)
        pygame.display.flip()


    def comptage(l):
        pts = 0
        if l == [4,2,1]:
            pts=10
        elif l == [1,1,1]:
            pts=7
        elif l[0] == l[1] == l[2]:
            pts=l[0]
        elif l[0] == l[1] == 1:
            pts=l[2]
        elif l[0] == l[1]-1 == l[2]-2:
            pts=2
        else:
            pts=1
        return pts


    fenetre = initScreen((1000,600), "421", "#FFFF00", './image/421/icon.jpg')


    printImage("./image/421/play.png", (700, 472.73), [160,36], fenetre)
    pygame.display.flip()

    nomj1, nomj2 = get_nom()
        

    fin = 0
    while fin == 0:
        for event in pygame.event.get():
            if (event.type == MOUSEBUTTONUP):
                x = event.pos[0]
                y = event.pos[1]
                if x > 161 and x < 859 and y > 298 and y < 485:
                    fin = 1 
                    
            if (event.type == KEYDOWN) or (event.type == QUIT): 
                return 0

    printImage("./image/421/jaune.png", (1000, 600), [0, 0], fenetre)

    printImage("./image/421/lancer.jpg", (350, 86.55), [100, 420], fenetre)

    printImage("./image/421/continuer.jpg", (350, 86.55), [550, 420], fenetre)

    printText(nomj1+" :", 33, "black", (950, 55), fenetre, Alignement="Right")

    printText(nomj2+" :", 33, "black", (950, 85), fenetre, Alignement="Right")

    printText("score :", 33, "black", (950, 20), fenetre, underline=True, Alignement="Right")

    pygame.display.flip()


    kijou = 0
    point1 = 0
    point2 = 0
    pot = 21
    end = 0
    while end==0:

        printImage("./image/421/jaune.png", (30, 60), [110, 90], fenetre)

        printImage("./image/421/jaune.png", (25, 25), [65, 10], fenetre)

        printText("Pot :", 33, "black", (10, 10), fenetre)

        printText("Point :", 33, "black", (10, 60), fenetre, underline=True)

        printText(nomj1+" : "+str(point1), 33, "black", (10, 90), fenetre)

        printText(nomj2+" : "+str(point2), 33, "black", (10, 120), fenetre)

        printText(str(pot), 33, "black", (65, 10), fenetre)

        printImage("./image/421/blanc.png", (100, 100), [200, 200], fenetre)

        printImage("./image/421/blanc.png", (100, 100), [450, 200], fenetre)

        printImage("./image/421/blanc.png", (100, 100), [700, 200], fenetre)

        printImage("./image/421/jaune.png", (50, 70), [950, 50], fenetre)

        printImage("./image/421/jaune.png", (520, 70), [250, 70], fenetre)

        printText("Au tour de " + (nomj1 if kijou%2==0 else nomj2), 76, "red", (500, 70), fenetre, Alignement="Center")

        pygame.display.flip()


        coup = 0
        fin=0
        d1 = 1
        d2 = 1
        d3 = 1
        score1 = [0, 0, 0]
        while fin==0:
            for event in pygame.event.get():
                if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]
                        #print(x ,y)
                        if x > 99 and x < 449 and y > 419 and y < 502:
                            lancer = tirage(d1, d2, d3)
                            affich(lancer, score1)
                            coup+=1
                            fin=1
                if (event.type == QUIT): 
                    return 0


        
        fin=0
        while coup<3 and fin==0:
            for event in pygame.event.get():
                if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]
                        #print(x ,y)
                        if x > 99 and x < 449 and y > 419 and y < 502:
                            lancer = tirage(d1, d2, d3)
                            affich(lancer, score1)
                            coup+=1
                        if x > 200 and x < 300 and y > 200 and y < 300:
                            if d1 == 1:
                                keep(d1, 1, lancer[0])
                                score1[0] = lancer[0]
                                lancer[0] = 0
                                d1 = 0
                            else:
                                keep(d1, 1, score1[0])
                                lancer[0] = score1[0]
                                score1[0] = 0
                                d1 = 1
                        if x > 450 and x < 550 and y > 200 and y < 300:
                            if d2 == 1:
                                keep(d2, 2, lancer[1])
                                score1[1] = lancer[1]
                                lancer[1] = 0
                                d2 = 0
                            else:
                                keep(d2, 2, score1[1])
                                lancer[1] = score1[1]
                                score1[1] = 0
                                d2 = 1
                        if x > 700 and x < 800 and y > 200 and y < 300:
                            if d3 == 1:
                                keep(d3, 3, lancer[2])
                                score1[2] = lancer[2]
                                lancer[2] = 0
                                d3 = 0
                            else:
                                keep(d3, 3, score1[2])
                                lancer[2] = score1[2]
                                score1[2] = 0
                                d3 = 1
                        if x > 550 and x < 900 and y > 419 and y < 504:
                            fin=1
                            
                if (event.type == QUIT): 
                    return 0

        coup_max = coup
        if score1[0] == 0:
            score1[0] = lancer[0]
        if score1[1] == 0:
            score1[1] = lancer[1]
        if score1[2] == 0:
            score1[2] = lancer[2]
        score1.sort()
        if score1 == [1, 2, 4]:
            score1.sort(reverse=True)

        if kijou%2 == 0:
            printText(str(score1[0]) + str(score1[1]) + str(score1[2]), 33, "black", (955, 55), fenetre)
            pygame.display.flip()
        else:
            printText(str(score1[0]) + str(score1[1]) + str(score1[2]), 33, "black", (955, 85), fenetre)
            pygame.display.flip()
                    
        kijou+=1

        printImage("./image/421/jaune.png", (600, 70), [500, 70], fenetre, Alignement="Center")

        printText("Au tour de " + (nomj1 if kijou%2==0 else nomj2), 76, "red", (500, 70), fenetre, Alignement="Center")
        pygame.display.flip()

        coup = 0
        fin=0
        d1 = 1
        d2 = 1
        d3 = 1
        score2 = [0, 0, 0]
        while fin==0:
            for event in pygame.event.get():
                if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]
                        #print(x ,y)
                        if x > 99 and x < 449 and y > 419 and y < 502:
                            lancer = tirage(d1, d2, d3)
                            affich(lancer, score2)
                            coup+=1
                            fin=1

                if (event.type == QUIT): 
                    return 0

        
        fin=0
        while coup<coup_max and fin==0:
            for event in pygame.event.get():
                if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]
                        #print(x ,y)
                        if x > 99 and x < 449 and y > 419 and y < 502:
                            lancer = tirage(d1, d2, d3)
                            affich(lancer, score2)
                            coup+=1
                        if x > 200 and x < 300 and y > 200 and y < 300:
                            if d1 == 1:
                                keep(d1, 1, lancer[0])
                                score2[0] = lancer[0]
                                lancer[0] = 0
                                d1 = 0
                            else:
                                keep(d1, 1, score2[0])
                                lancer[0] = score2[0]
                                score2[0] = 0
                                d1 = 1
                        if x > 450 and x < 550 and y > 200 and y < 300:
                            if d2 == 1:
                                keep(d2, 2, lancer[1])
                                score2[1] = lancer[1]
                                lancer[1] = 0
                                d2 = 0
                            else:
                                keep(d2, 2, score2[1])
                                lancer[1] = score2[1]
                                score2[1] = 0
                                d2 = 1
                        if x > 700 and x < 800 and y > 200 and y < 300:
                            if d3 == 1:
                                keep(d3, 3, lancer[2])
                                score2[2] = lancer[2]
                                lancer[2] = 0
                                d3 = 0
                            else:
                                keep(d3, 3, score2[2])
                                lancer[2] = score2[2]
                                score2[2] = 0
                                d3 = 1
                        if x > 550 and x < 900 and y > 419 and y < 504:
                            fin=1
                            
                if (event.type == QUIT): 
                    return 0

        if score2[0] == 0:
            score2[0] = lancer[0]
        if score2[1] == 0:
            score2[1] = lancer[1]
        if score2[2] == 0:
            score2[2] = lancer[2]
        score2.sort()
        if score2 == [1, 2, 4]:
            score2.sort(reverse=True)

        if kijou%2==1:
            printText(str(score2[0]) + str(score2[1]) + str(score2[2]), 33, "black", (955, 85), fenetre)
            pygame.display.flip()
        else:
            printText(str(score2[0]) + str(score2[1]) + str(score2[2]), 33, "black", (955, 55), fenetre)
            pygame.display.flip()


        jeton1 = comptage(score1)
        jeton2 = comptage(score2)

        valscore1 = score1[0] + score1[1] + score1[2]
        valscore2 = score2[0] + score2[1] + score2[2]

        

        if kijou%2==1:
            if score1 == [1,2,2]:
                if pot!=0:
                    if pot>=2:
                        point1+=2
                        pot-=2
                    else:
                        point1+=pot
                        pot=0
                else:
                    if point2>=2:
                        point1+=2
                        point2-=2
                    else:
                        point1+=point2
                        point2=0
            if score2 == [1,2,2]:
                if pot!=0:
                    if pot>=2:
                        point2+=2
                        pot-=2
                    else:
                        point2+=pot
                        pot=0
                else:
                    if point1>=2:
                        point2+=2
                        point1-=2
                    else:
                        point2+=point1
                        point1=0

            if jeton1 > jeton2:
                if pot!=0:
                    if pot>=jeton1:
                        point2 += jeton1
                        pot-=jeton1
                    else:
                        point2 += pot
                        pot=0
                else:
                    if point1>=jeton1:
                        point1-=jeton1
                        point2+=jeton1
                    else:
                        point2+=point1
                        point1=0
                    
                    
            elif jeton1 < jeton2:
                if pot!=0:
                    if pot>=jeton2:
                        point1 += jeton2
                        pot-=jeton2
                    else:
                        point1 += pot
                        pot=0
                else:
                    if point2>=jeton2:
                        point2-=jeton2
                        point1+=jeton2
                    else:
                        point1+=point2
                        point2=0

            else:
                if valscore1>valscore2:
                    if pot!=0:
                        if pot>=jeton1:
                            point2 += jeton1
                            pot-=jeton1
                        else:
                            point2 += pot
                            pot=0
                    else:
                        if point1>=jeton1:
                            point1-=jeton1
                            point2+=jeton1
                        else:
                            point2+=point1
                            point1=0

                elif valscore2>valscore1:
                    if pot!=0:
                        if pot>=jeton2:
                            point1 += jeton2
                            pot-=jeton2
                        else:
                            point1 += pot
                            pot=0
                    else:
                        if point2>=jeton2:
                            point2-=jeton2
                            point1+=jeton2
                        else:
                            point1+=point2
                            point2=0

        else:
            if score2 == [1,2,2]:
                if pot!=0:
                    if pot>=2:
                        point1+=2
                        pot-=2
                    else:
                        point1+=pot
                        pot=0
                else:
                    if point2>=2:
                        point1+=2
                        point2-=2
                    else:
                        point1+=point2
                        point2=0
            if score1 == [1,2,2]:
                if pot!=0:
                    if pot>=2:
                        point2+=2
                        pot-=2
                    else:
                        point2+=pot
                        pot=0
                else:
                    if point1>=2:
                        point2+=2
                        point1-=2
                    else:
                        point2+=point1
                        point1=0

            if jeton1 > jeton2:
                if pot!=0:
                    if pot>=jeton1:
                        point1 += jeton1
                        pot-=jeton1
                    else:
                        point1 += pot
                        pot=0
                else:
                    if point2>=jeton1:
                        point2-=jeton1
                        point1+=jeton1
                    else:
                        point1+=point2
                        point2=0
                    
                    
            elif jeton1 < jeton2:
                if pot!=0:
                    if pot>=jeton2:
                        point2 += jeton2
                        pot-=jeton2
                    else:
                        point2 += pot
                        pot=0
                else:
                    if point1>=jeton2:
                        point1-=jeton2
                        point2+=jeton2
                    else:
                        point2+=point1
                        point2=0

            else:
                if valscore1>valscore2:
                    if pot!=0:
                        if pot>=jeton1:
                            point1 += jeton1
                            pot-=jeton1
                        else:
                            point1 += pot
                            pot=0
                    else:
                        if point2>=jeton1:
                            point2-=jeton1
                            point1+=jeton1
                        else:
                            point1+=point2
                            point1=0

                elif valscore2>valscore1:
                    if pot!=0:
                        if pot>=jeton2:
                            point2 += jeton2
                            pot-=jeton2
                        else:
                            point2 += pot
                            pot=0
                    else:
                        if point1>=jeton2:
                            point1-=jeton2
                            point2+=jeton2
                        else:
                            point2+=point1
                            point1=0




        printImage("./image/421/jaune.png", (150, 60), [10, 90], fenetre)

        printText(nomj1+" : "+str(point1), 33, "black", (10, 90), fenetre)

        printText(nomj2+" : "+str(point2), 33, "black", (10, 120), fenetre)

        printImage("./image/421/jaune.png", (25, 25), [65, 10], fenetre)

        printText(str(pot), 33, "black", (65, 10), fenetre)

        pygame.display.flip()

        fin=0
        if pot==0 and(point1==0 or point2==0):
            if point1==0:
                if kijou%2==1:
                    j=nomj1
                else:
                    j=nomj2
            else:
                if kijou%2==1:
                    j=nomj2
                else:
                    j=nomj1
            point1 = 0
            point2 = 0
            pot = 21

            printImage("./image/421/jaune.png", (500, 70), [270, 70], fenetre)

            printText("Victoire de " + j, 76, "#556B2F", (250, 70), fenetre)

            pygame.display.flip()

        while fin==0:
            for event in pygame.event.get():
                if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]
                        if x > 550 and x < 900 and y > 419 and y < 504:
                            fin=1
                if (event.type == QUIT): 
                    return 0

    
if __name__ == "__main__":
    jeux421()