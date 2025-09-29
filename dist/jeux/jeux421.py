from pygame import *
import pygame
from math import *
import random
from time import *


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
                bille = pygame.image.load("./image/421/de"+str(a)+".jpg").convert_alpha()
                bille = pygame.transform.scale(bille, (100, 100))
                position_bille = [200, 200] 
                fenetre.blit(bille, position_bille)
                pygame.display.flip()
                sleep(0.1)

            bille = pygame.image.load("./image/421/de"+str(l[0])+".jpg").convert_alpha()
            bille = pygame.transform.scale(bille, (100, 100))
            position_bille = [200, 200] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip()
        
        if score[1]==0:
            for i in range(10):
                a = random.randint(1,6)
                bille = pygame.image.load("./image/421/de"+str(a)+".jpg").convert_alpha()
                bille = pygame.transform.scale(bille, (100, 100))
                position_bille = [450, 200] 
                fenetre.blit(bille, position_bille)
                pygame.display.flip()
                sleep(0.1)

            bille = pygame.image.load("./image/421/de"+str(l[1])+".jpg").convert_alpha()
            bille = pygame.transform.scale(bille, (100, 100))
            position_bille = [450, 200] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip()

        if score[2]==0:
            for i in range(10):
                a = random.randint(1,6)
                bille = pygame.image.load("./image/421/de"+str(a)+".jpg").convert_alpha()
                bille = pygame.transform.scale(bille, (100, 100))
                position_bille = [700, 200] 
                fenetre.blit(bille, position_bille)
                pygame.display.flip()
                sleep(0.1)


            bille = pygame.image.load("./image/421/de"+str(l[2])+".jpg").convert_alpha()
            bille = pygame.transform.scale(bille, (100, 100))
            position_bille = [700, 200] 
            fenetre.blit(bille, position_bille)
        
        pygame.display.flip()


    def keep(d, pos, val):
        if d==1:
            l='R'
        else:
            l=''

        p=[200, 450, 700] 
        
        bille = pygame.image.load("./image/421/de"+l+str(val)+".jpg").convert_alpha()
        bille = pygame.transform.scale(bille, (100, 100))
        position_bille = [p[pos-1], 200] 
        fenetre.blit(bille, position_bille)
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


    pygame.init()
    pygame.font.init()
    fenetre = pygame.display.set_mode((1000,600))
    fenetre.fill("#FFFF00")
    pygame.display.set_caption("421")
    pygame_icon = pygame.image.load('./image/421/icon.jpg')
    pygame.display.set_icon(pygame_icon)
    pygame.display.flip()


    bille = pygame.image.load("./image/421/play.png").convert_alpha()
    bille = pygame.transform.scale(bille, (700, 472.73))
    fenetre.blit(bille, (160,36))
    pygame.display.flip()
        

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

    bille = pygame.image.load("./image/421/jaune.png").convert_alpha()
    bille = pygame.transform.scale(bille, (1000, 600))
    position_bille = [0, 0] 
    fenetre.blit(bille, position_bille)


    bille = pygame.image.load("./image/421/lancer.jpg").convert_alpha()
    bille = pygame.transform.scale(bille, (350, 86.55))
    position_bille = [100, 420] 
    fenetre.blit(bille, position_bille)

    bille = pygame.image.load("./image/421/continuer.jpg").convert_alpha()
    bille = pygame.transform.scale(bille, (350, 86.55))
    position_bille = [550, 420] 
    fenetre.blit(bille, position_bille)

    police = pygame.font.Font(None, 33)
    texte = police.render("Joueur 1 :",True, "black")
    fenetre.blit(texte, (840, 55))

    police = pygame.font.Font(None, 33)
    texte = police.render("Joueur 2 :",True, "black")
    fenetre.blit(texte, (840, 85))

    police = pygame.font.Font(None, 33)
    police.underline = True
    texte = police.render("score :",True, "black")
    fenetre.blit(texte, (870, 20))

    pygame.display.flip()


    kijou = 0
    point1 = 0
    point2 = 0
    pot = 21
    end = 0
    while end==0:

        bille = pygame.image.load("./image/421/jaune.png").convert_alpha()
        bille = pygame.transform.scale(bille, (30, 60))
        position_bille = [110, 90] 
        fenetre.blit(bille, position_bille)

        bille = pygame.image.load("./image/421/jaune.png").convert_alpha()
        bille = pygame.transform.scale(bille, (25, 25))
        position_bille = [65, 10] 
        fenetre.blit(bille, position_bille)

        

        police = pygame.font.Font(None, 33)
        texte = police.render("Pot :",True, "black")
        fenetre.blit(texte, (10, 10))

        police = pygame.font.Font(None, 33)
        police.underline = True
        texte = police.render("Point :",True, "black")
        fenetre.blit(texte, (10, 60))

        police = pygame.font.Font(None, 33)
        texte = police.render("Joueur 1:",True, "black")
        fenetre.blit(texte, (10, 90))

        police = pygame.font.Font(None, 33)
        texte = police.render("Joueur 2:",True, "black")
        fenetre.blit(texte, (10, 120))

        police = pygame.font.Font(None, 33)
        texte = police.render(str(point1),True, "black")
        fenetre.blit(texte, (115, 90))

        police = pygame.font.Font(None, 33)
        texte = police.render(str(point2),True, "black")
        fenetre.blit(texte, (115, 120))

        police = pygame.font.Font(None, 33)
        texte = police.render(str(pot),True, "black")
        fenetre.blit(texte, (65, 10))

        bille = pygame.image.load("./image/421/blanc.png").convert_alpha()
        bille = pygame.transform.scale(bille, (100, 100))
        position_bille = [200, 200] 
        fenetre.blit(bille, position_bille)

        bille = pygame.image.load("./image/421/blanc.png").convert_alpha()
        bille = pygame.transform.scale(bille, (100, 100))
        position_bille = [450, 200] 
        fenetre.blit(bille, position_bille)

        bille = pygame.image.load("./image/421/blanc.png").convert_alpha()
        bille = pygame.transform.scale(bille, (100, 100))
        position_bille = [700, 200] 
        fenetre.blit(bille, position_bille)

        bille = pygame.image.load("./image/421/jaune.png").convert_alpha()
        bille = pygame.transform.scale(bille, (50, 70))
        position_bille = [950, 50] 
        fenetre.blit(bille, position_bille)

        bille = pygame.image.load("./image/421/jaune.png").convert_alpha()
        bille = pygame.transform.scale(bille, (520, 70))
        position_bille = [250, 70] 
        fenetre.blit(bille, position_bille)

        police = pygame.font.Font(None, 76)
        texte = police.render("Au tour du joueur " + str(kijou%2+1),True, "red")
        fenetre.blit(texte, (270, 70))

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
            police = pygame.font.Font(None, 33)
            texte = police.render(str(score1[0]) + str(score1[1]) + str(score1[2]),True, "black")
            fenetre.blit(texte, (955, 55))
            pygame.display.flip()
        else:
            police = pygame.font.Font(None, 33)
            texte = police.render(str(score1[0]) + str(score1[1]) + str(score1[2]),True, "black")
            fenetre.blit(texte, (955, 85))
            pygame.display.flip()
                    
        kijou+=1

        bille = pygame.image.load("./image/421/jaune.png").convert_alpha()
        bille = pygame.transform.scale(bille, (500, 70))
        position_bille = [270, 70] 
        fenetre.blit(bille, position_bille)

        police = pygame.font.Font(None, 76)
        texte = police.render("Au tour du joueur " + str(kijou%2+1),True, "red")
        fenetre.blit(texte, (270, 70))
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
            police = pygame.font.Font(None, 33)
            texte = police.render(str(score2[0]) + str(score2[1]) + str(score2[2]),True, "black")
            fenetre.blit(texte, (955, 85))
            pygame.display.flip()
        else:
            police = pygame.font.Font(None, 33)
            texte = police.render(str(score2[0]) + str(score2[1]) + str(score2[2]),True, "black")
            fenetre.blit(texte, (955, 55))
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




        bille = pygame.image.load("./image/421/jaune.png").convert_alpha()
        bille = pygame.transform.scale(bille, (30, 60))
        position_bille = [110, 90] 
        fenetre.blit(bille, position_bille)

        police = pygame.font.Font(None, 33)
        texte = police.render(str(point1),True, "black")
        fenetre.blit(texte, (115, 90))

        police = pygame.font.Font(None, 33)
        texte = police.render(str(point2),True, "black")
        fenetre.blit(texte, (115, 120))

        bille = pygame.image.load("./image/421/jaune.png").convert_alpha()
        bille = pygame.transform.scale(bille, (25, 25))
        position_bille = [65, 10] 
        fenetre.blit(bille, position_bille)

        police = pygame.font.Font(None, 33)
        texte = police.render(str(pot),True, "black")
        fenetre.blit(texte, (65, 10))

        pygame.display.flip()

        fin=0
        if pot==0 and(point1==0 or point2==0):
            if point1==0:
                if kijou%2==1:
                    j='1'
                else:
                    j='2'
            else:
                if kijou%2==1:
                    j='2'
                else:
                    j='1'
            point1 = 0
            point2 = 0
            pot = 21

            bille = pygame.image.load("./image/421/jaune.png").convert_alpha()
            bille = pygame.transform.scale(bille, (500, 70))
            position_bille = [270, 70] 
            fenetre.blit(bille, position_bille)

            police = pygame.font.Font(None, 76)
            texte = police.render("Victoire du joueur " + j,True, "#556B2F")
            fenetre.blit(texte, (250, 70))

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

    
