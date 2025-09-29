from pygame import *
import pygame
from random import *
from time import *

def yams():

    def affich(l, score):

            if score[0]==0:
                for i in range(10):
                    a = randint(1,6)
                    bille = pygame.image.load("./image/421/de"+str(a)+".jpg").convert_alpha()
                    bille = pygame.transform.scale(bille, (100, 100))
                    position_bille = [83, 250] 
                    fenetre.blit(bille, position_bille)
                    pygame.display.flip()
                    sleep(0.1)

                bille = pygame.image.load("./image/421/de"+str(l[0])+".jpg").convert_alpha()
                bille = pygame.transform.scale(bille, (100, 100))
                position_bille = [83, 250] 
                fenetre.blit(bille, position_bille)
                pygame.display.flip()
            
            if score[1]==0:
                for i in range(10):
                    a = randint(1,6)
                    bille = pygame.image.load("./image/421/de"+str(a)+".jpg").convert_alpha()
                    bille = pygame.transform.scale(bille, (100, 100))
                    position_bille = [266, 250] 
                    fenetre.blit(bille, position_bille)
                    pygame.display.flip()
                    sleep(0.1)

                bille = pygame.image.load("./image/421/de"+str(l[1])+".jpg").convert_alpha()
                bille = pygame.transform.scale(bille, (100, 100))
                position_bille = [266, 250] 
                fenetre.blit(bille, position_bille)
                pygame.display.flip()

            if score[2]==0:
                for i in range(10):
                    a = randint(1,6)
                    bille = pygame.image.load("./image/421/de"+str(a)+".jpg").convert_alpha()
                    bille = pygame.transform.scale(bille, (100, 100))
                    position_bille = [449, 250] 
                    fenetre.blit(bille, position_bille)
                    pygame.display.flip()
                    sleep(0.1)


                bille = pygame.image.load("./image/421/de"+str(l[2])+".jpg").convert_alpha()
                bille = pygame.transform.scale(bille, (100, 100))
                position_bille = [449, 250] 
                fenetre.blit(bille, position_bille)

            if score[3]==0:
                for i in range(10):
                    a = randint(1,6)
                    bille = pygame.image.load("./image/421/de"+str(a)+".jpg").convert_alpha()
                    bille = pygame.transform.scale(bille, (100, 100))
                    position_bille = [632, 250] 
                    fenetre.blit(bille, position_bille)
                    pygame.display.flip()
                    sleep(0.1)


                bille = pygame.image.load("./image/421/de"+str(l[3])+".jpg").convert_alpha()
                bille = pygame.transform.scale(bille, (100, 100))
                position_bille = [632, 250] 
                fenetre.blit(bille, position_bille)

            if score[4]==0:
                for i in range(10):
                    a = randint(1,6)
                    bille = pygame.image.load("./image/421/de"+str(a)+".jpg").convert_alpha()
                    bille = pygame.transform.scale(bille, (100, 100))
                    position_bille = [817, 250] 
                    fenetre.blit(bille, position_bille)
                    pygame.display.flip()
                    sleep(0.1)


                bille = pygame.image.load("./image/421/de"+str(l[4])+".jpg").convert_alpha()
                bille = pygame.transform.scale(bille, (100, 100))
                position_bille = [817, 250] 
                fenetre.blit(bille, position_bille)
            
            pygame.display.flip()


    def keep(d, pos, val):
            if d==1:
                l='R'
            else:
                l=''

            p=[83, 266, 449, 632, 817] 
            
            bille = pygame.image.load("./image/421/de"+l+str(val)+".jpg").convert_alpha()
            bille = pygame.transform.scale(bille, (100, 100))
            position_bille = [p[pos-1], 250] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip()

    def tirage(d1, d2, d3, d4, d5):

            l = [0, 0, 0, 0, 0]
            if d1==1:
                l[0] = randint(1, 6)
            if d2==1:
                l[1] = randint(1, 6)
            if d3==1:
                l[2] = randint(1, 6)
            if d4==1:
                l[3] = randint(1, 6)
            if d5==1:
                l[4] = randint(1, 6)

            return l


    pygame.init()
    pygame.font.init()
    fenetre = pygame.display.set_mode((1000,600))
    fenetre.fill("orange")
    pygame.display.set_caption("Yams")
    pygame_icon = pygame.image.load('./image/yams/icon.jpg')
    pygame.display.set_icon(pygame_icon)
    pygame.display.flip()



    bille = pygame.image.load("./image/yams/play.png").convert_alpha()
    bille = pygame.transform.scale(bille, (700, 356.84))
    fenetre.blit(bille, (150,110))
    pygame.display.flip()
            

    fin = 0
    while fin == 0:
        for event in pygame.event.get():
            if (event.type == MOUSEBUTTONUP):
                x = event.pos[0]
                y = event.pos[1]
                if x > 150 and x < 850 and y > 110 and y < 467:
                    fin = 1 
                        
            if (event.type == KEYDOWN) or (event.type == QUIT): 
                return 0

    fenetre.fill("orange")
    restart=0
    while restart==0:


        bille = pygame.image.load("./image/yams/relancer.png").convert_alpha()
        bille = pygame.transform.scale(bille, (350, 86.55))
        position_bille = [100, 460] 
        fenetre.blit(bille, position_bille)

        bille = pygame.image.load("./image/yams/suivant.png").convert_alpha()
        bille = pygame.transform.scale(bille, (350, 86.55))
        position_bille = [550, 460] 
        fenetre.blit(bille, position_bille)

        bille = pygame.image.load("./image/yams/point.png")
        bille = pygame.transform.scale(bille, (950, 88.197))
        position_bille = [50, 0] 
        fenetre.blit(bille, position_bille)

        police = pygame.font.Font(None, 18)
        texte = police.render("Joueur 1",True, "black")
        fenetre.blit(texte, (1, 35))

        police = pygame.font.Font(None, 18)
        texte = police.render("Joueur 2",True, "black")
        fenetre.blit(texte, (1, 68))


        kijou = 0

        point_rempli1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        point_rempli2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        tot1j1 = 0
        tot2j1 = 0
        totj1 = 0
        bonus1 = 0
        tot1j2 = 0
        tot2j2 = 0
        totj2 = 0
        bonus2 = 0


        end=0
        while end==0:

            if kijou%2==0:
                joueur = "joueur 1"
            else:
                joueur = "joueur 2"

            bille = pygame.image.load("./image/421/blanc.png").convert_alpha()
            bille = pygame.transform.scale(bille, (100, 100))
            position_bille = [83, 250] 
            fenetre.blit(bille, position_bille)

            bille = pygame.image.load("./image/421/blanc.png").convert_alpha()
            bille = pygame.transform.scale(bille, (100, 100))
            position_bille = [266, 250] 
            fenetre.blit(bille, position_bille)

            bille = pygame.image.load("./image/421/blanc.png").convert_alpha()
            bille = pygame.transform.scale(bille, (100, 100))
            position_bille = [449, 250] 
            fenetre.blit(bille, position_bille)

            bille = pygame.image.load("./image/421/blanc.png").convert_alpha()
            bille = pygame.transform.scale(bille, (100, 100))
            position_bille = [632, 250] 
            fenetre.blit(bille, position_bille)

            bille = pygame.image.load("./image/421/blanc.png").convert_alpha()
            bille = pygame.transform.scale(bille, (100, 100))
            position_bille = [817, 250] 
            fenetre.blit(bille, position_bille)

            bille = pygame.image.load("./image/yams/cache.png").convert_alpha()
            bille = pygame.transform.scale(bille, (1000, 100))
            position_bille = [0, 140] 
            fenetre.blit(bille, position_bille)

            police = pygame.font.Font(None, 76)
            texte = police.render(joueur+ ", lancez les dés",True, "black")
            rectText = texte.get_rect().width 
            fenetre.blit(texte, (500-rectText/2, 150))

            pygame.display.flip()


            coup = 0
            fin=0
            d1 = 1
            d2 = 1
            d3 = 1
            d4 = 1
            d5 = 1
            score1 = [0, 0, 0, 0, 0]
            while fin==0:
                for event in pygame.event.get():
                    if (event.type == MOUSEBUTTONUP):
                            x = event.pos[0]
                            y = event.pos[1]
                            print(x ,y)
                            if x > 99 and x < 449 and y > 460 and y < 540:
                                lancer = tirage(d1, d2, d3, d4, d5)
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
                            if x > 99 and x < 449 and y > 460 and y < 540:
                                lancer = tirage(d1, d2, d3, d4, d5)
                                affich(lancer, score1)
                                coup+=1
                            if x > 83 and x < 183 and y > 250 and y < 350:
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
                            if x > 266 and x < 366 and y > 250 and y < 350:
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
                            if x > 449 and x < 549 and y > 250 and y < 350:
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
                            if x > 632 and x < 732 and y > 250 and y < 350:
                                if d4 == 1:
                                    keep(d4, 4, lancer[3])
                                    score1[3] = lancer[3]
                                    lancer[3] = 0
                                    d4 = 0
                                else:
                                    keep(d4, 4, score1[3])
                                    lancer[3] = score1[3]
                                    score1[3] = 0
                                    d4 = 1
                            if x > 817 and x < 917 and y > 250 and y < 350:
                                if d5 == 1:
                                    keep(d5, 5, lancer[4])
                                    score1[4] = lancer[4]
                                    lancer[4] = 0
                                    d5 = 0
                                else:
                                    keep(d5, 5, score1[4])
                                    lancer[4] = score1[4]
                                    score1[4] = 0
                                    d5 = 1

                            if x > 550 and x < 900 and y > 460 and y < 540:
                                fin=1
                                        
                    if (event.type == QUIT): 
                        return 0

            if score1[0] == 0:
                score1[0] = lancer[0]
            if score1[1] == 0:
                score1[1] = lancer[1]
            if score1[2] == 0:
                score1[2] = lancer[2]
            if score1[3] == 0:
                score1[3] = lancer[3]
            if score1[4] == 0:
                score1[4] = lancer[4]
            score1.sort()
            print(score1)


            t1 = 0
            t2 = 0
            t3 = 0
            t4 = 0
            t5 = 0
            t6 = 0
            plus = 0
            moins = 0
            suite = 0
            full = 0
            carre = 0
            yams = 0
            test = 0


            if kijou%2==0:
                if 1 in score1 and point_rempli1[0]==0:
                    test=1
                    t1=1
                if 2 in score1 and point_rempli1[1]==0:
                    test=1
                    t2=1
                if 3 in score1 and point_rempli1[2]==0:
                    test=1
                    t3=1
                if 4 in score1 and point_rempli1[3]==0:
                    test=1
                    t4=1
                if 5 in score1 and point_rempli1[4]==0:
                    test=1
                    t5=1
                if 6 in score1 and point_rempli1[5]==0:
                    test=1
                    t6=1
                if point_rempli1[6]==0:
                    test=1
                    plus=1
                if point_rempli1[7]==0:
                    test=1
                    moins=1
                if score1[0] == score1[1]-1 ==  score1[2]-2 == score1[3]-3 ==score1[4]-4 and point_rempli1[8]==0:
                    test=1
                    suite=1
                if (score1[0] == score1[1] ==  score1[2] == score1[3] or score1[1] == score1[2] ==  score1[3] == score1[4]) and point_rempli1[10]==0:
                    test = 1
                    carre=1
                if score1[0] == score1[1] ==  score1[2] == score1[3] == score1[4] and point_rempli1[11]==0:
                    test = 1
                    yams = 1
                elif ((score1[0] == score1[1] == score1[2] and score1[3] == score1[4]) or (score1[0] == score1[1] and score1[2] == score1[3] == score1[4])) and point_rempli1[9]==0:
                    test=1
                    full=1
            else:
                if 1 in score1 and point_rempli2[0]==0:
                    test=1
                    t1=1
                if 2 in score1 and point_rempli2[1]==0:
                    test=1
                    t2=1
                if 3 in score1 and point_rempli2[2]==0:
                    test=1
                    t3=1
                if 4 in score1 and point_rempli2[3]==0:
                    test=1
                    t4=1
                if 5 in score1 and point_rempli2[4]==0:
                    test=1
                    t5=1
                if 6 in score1 and point_rempli2[5]==0:
                    test=1
                    t6=1
                if point_rempli2[6]==0:
                    test=1
                    plus=1
                if point_rempli2[7]==0:
                    test=1
                    moins=1
                if score1[0] == score1[1]-1 ==  score1[2]-2 == score1[3]-3 ==score1[4]-4 and point_rempli2[8]==0:
                    test=1
                    suite=1
                if (score1[0] == score1[1] ==  score1[2] == score1[3] or score1[1] == score1[2] ==  score1[3] == score1[4]) and point_rempli2[10]==0:
                    test = 1
                    carre=1
                if score1[0] == score1[1] ==  score1[2] == score1[3] == score1[4] and point_rempli2[11]==0:
                    test = 1
                    yams = 1
                elif ((score1[0] == score1[1] == score1[2] and score1[3] == score1[4]) or (score1[0] == score1[1] and score1[2] == score1[3] == score1[4])) and point_rempli2[9]==0:
                    test=1
                    full=1


            bille = pygame.image.load("./image/yams/cache.png").convert_alpha()
            bille = pygame.transform.scale(bille, (1000, 100))
            position_bille = [0, 140] 
            fenetre.blit(bille, position_bille)

            if test!=0:
                police = pygame.font.Font(None, 76)
                texte = police.render(joueur +", mettez vos points",True, "black")
                rectText = texte.get_rect().width 
                fenetre.blit(texte, (500-rectText/2, 150))
                pygame.display.flip()
            else:
                police = pygame.font.Font(None, 76)
                texte = police.render(joueur +", enlevez une case",True, "black")
                rectText = texte.get_rect().width 
                fenetre.blit(texte, (500-rectText/2, 150))
                pygame.display.flip()

            if kijou%2==0:
                yp = 35
                yc = 30
            else:
                yp = 65
                yc = 60

            bon = 0
            fin = 0
            while fin == 0:
                for event in pygame.event.get():
                    if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]

                        xp = 0
                        c = 0
                        if y>27 and y<87:
                            if kijou%2==0:
                                if x>54 and x<104 and bon==0 and (t1==1 or test==0 and point_rempli1[0]==0):
                                    if test!=0:
                                        xp = 77
                                        c = str(score1.count(1))
                                        tot1j1 += score1.count(1)
                                        totj1 += score1.count(1)
                                    else:
                                        xp=67
                                    point_rempli1[0] = 1
                                    bon=1
                                    
                                    
                                        
                                if x>104 and x<154 and bon==0 and(t2==1 or test==0 and point_rempli1[1]==0):
                                    if test!=0:
                                        xp = 127
                                        c = str(score1.count(2)*2)
                                        tot1j1 += score1.count(2)*2
                                        totj1 += score1.count(2)*2
                                    else:
                                        xp=117
                                    point_rempli1[1] = 1
                                    bon=1
                                        
                                if x>154 and x<204 and bon==0 and (t3==1 or test==0 and point_rempli1[2]==0):
                                    if test!=0:
                                        xp = 177
                                        c = str(score1.count(3)*3)
                                        tot1j1 += score1.count(3)*3
                                        totj1 += score1.count(3)*3
                                    else:
                                        xp=167
                                    point_rempli1[2] = 1
                                    bon=1
                                        
                                if x>204 and x<254 and bon==0 and (t4==1 or test==0 and point_rempli1[3]==0):
                                    if test!=0:
                                        xp = 225
                                        c = str(score1.count(4)*4)
                                        tot1j1 += score1.count(4)*4
                                        totj1 += score1.count(4)*4
                                    else:
                                        xp=217
                                    point_rempli1[3] = 1
                                    bon=1
                                        
                                if x>254 and x<304 and bon==0 and (t5==1 or test==0 and point_rempli1[4]==0):
                                    if test!=0:
                                        xp = 275
                                        c = str(score1.count(5)*5)
                                        tot1j1 += score1.count(5)*5
                                        totj1 += score1.count(5)*5
                                    else:
                                        xp=267
                                    point_rempli1[4] = 1
                                    bon=1
                                        
                                if x>304 and x<354 and bon==0 and (t6==1 or test==0 and point_rempli1[5]==0):
                                    if test!=0:
                                        xp = 325
                                        c = str(score1.count(6)*6)
                                        tot1j1 += score1.count(6)*6
                                        totj1 += score1.count(6)*6
                                    else:
                                        xp=317
                                    point_rempli1[5] = 1
                                    bon=1
                                        
                                if x>491 and x<549 and bon==0 and (plus==1 or test==0 and point_rempli1[6]==0):
                                    if test!=0:
                                        xp = 515
                                        c = str(score1[0]+score1[1]+score1[2]+score1[3]+score1[4])
                                        tot2j1 += score1[0]+score1[1]+score1[2]+score1[3]+score1[4]
                                        totj1 += score1[0]+score1[1]+score1[2]+score1[3]+score1[4]
                                    else:
                                        xp=507
                                    point_rempli1[6] = 1
                                    bon=1
                                        
                                if x>549 and x<618 and bon==0 and (moins==1 or test==0 and point_rempli1[7]==0):
                                    if test!=0:
                                        xp = 578
                                        c = str(score1[0]+score1[1]+score1[2]+score1[3]+score1[4])
                                        tot2j1 -= score1[0]+score1[1]+score1[2]+score1[3]+score1[4]
                                        totj1 -= score1[0]+score1[1]+score1[2]+score1[3]+score1[4]
                                    else:
                                        xp=572
                                    point_rempli1[7] = 1
                                    bon=1
                                        
                                if x>698 and x<759 and bon==0 and (suite==1 or test==0 and point_rempli1[8]==0):
                                    if test!=0:
                                        xp = 722
                                        c = str(20)
                                        totj1 += 20
                                    else:
                                        xp=715
                                    point_rempli1[8] = 1
                                    bon=1
                                        
                                if x>759 and x<812 and bon==0 and (full==1 or test==0 and point_rempli1[9]==0):
                                    if test!=0:
                                        xp = 775
                                        c = str(30)
                                        totj1 += 30
                                    else:
                                        xp=770
                                    point_rempli1[9] = 1
                                    bon=1
                                        
                                if x>812 and x<874 and bon==0 and (carre==1 or test==0 and point_rempli1[10]==0):
                                    if test!=0:
                                        xp = 835
                                        c = str(40)
                                        totj1 += 40
                                    else:
                                        xp=830
                                    point_rempli1[10] = 1
                                    bon=1
                                        
                                if x>874 and x<938 and bon==0 and (yams==1 or test==0 and point_rempli1[11]==0):
                                    if test!=0:
                                        xp = 900
                                        c = str(50)
                                        totj1 += 50
                                    else:
                                        xp = 892
                                    point_rempli1[11] = 1
                                    bon=1
                            else:
                                    if x>54 and x<104 and bon==0 and (t1==1 or test==0 and point_rempli2[0]==0):
                                        if test!=0:
                                            xp = 77
                                            c = str(score1.count(1))
                                            tot1j2 += score1.count(1)
                                            totj2 += score1.count(1)
                                        else:
                                            xp=67
                                        point_rempli2[0] = 1
                                        bon=1
                                        
                                        
                                            
                                    if x>104 and x<154 and bon==0 and(t2==1 or test==0 and point_rempli2[1]==0):
                                        if test!=0:
                                            xp = 127
                                            c = str(score1.count(2)*2)
                                            tot1j2 += score1.count(2)*2
                                            totj2 += score1.count(2)*2
                                        else:
                                            xp=117
                                        point_rempli2[1] = 1
                                        bon=1
                                            
                                    if x>154 and x<204 and bon==0 and (t3==1 or test==0 and point_rempli2[2]==0):
                                        if test!=0:
                                            xp = 177
                                            c = str(score1.count(3)*3)
                                            tot1j2 += score1.count(3)*3
                                            totj2 += score1.count(3)*3
                                        else:
                                            xp=167
                                        point_rempli2[2] = 1
                                        bon=1
                                            
                                    if x>204 and x<254 and bon==0 and (t4==1 or test==0 and point_rempli2[3]==0):
                                        if test!=0:
                                            xp = 225
                                            c = str(score1.count(4)*4)
                                            tot1j2 += score1.count(4)*4
                                            totj2 += score1.count(4)*4
                                        else:
                                            xp=217
                                        point_rempli2[3] = 1
                                        bon=1
                                            
                                    if x>254 and x<304 and bon==0 and (t5==1 or test==0 and point_rempli2[4]==0):
                                        if test!=0:
                                            xp = 275
                                            c = str(score1.count(5)*5)
                                            tot1j2 += score1.count(5)*5
                                            totj2 += score1.count(5)*5
                                        else:
                                            xp=267
                                        point_rempli2[4] = 1
                                        bon=1
                                            
                                    if x>304 and x<354 and bon==0 and (t6==1 or test==0 and point_rempli2[5]==0):
                                        if test!=0:
                                            xp = 325
                                            c = str(score1.count(6)*6)
                                            tot1j2 += score1.count(6)*6
                                            totj2 += score1.count(6)*6
                                        else:
                                            xp=317
                                        point_rempli2[5] = 1
                                        bon=1
                                            
                                    if x>491 and x<549 and bon==0 and (plus==1 or test==0 and point_rempli2[6]==0):
                                        if test!=0:
                                            xp = 515
                                            c = str(score1[0]+score1[1]+score1[2]+score1[3]+score1[4])
                                            tot2j2 += score1[0]+score1[1]+score1[2]+score1[3]+score1[4]
                                            totj2 += score1[0]+score1[1]+score1[2]+score1[3]+score1[4]
                                        else:
                                            xp=507
                                        point_rempli2[6] = 1
                                        bon=1
                                            
                                    if x>549 and x<618 and bon==0 and (moins==1 or test==0 and point_rempli2[7]==0):
                                        if test!=0:
                                            xp = 578
                                            c = str(score1[0]+score1[1]+score1[2]+score1[3]+score1[4])
                                            tot2j2 -= score1[0]+score1[1]+score1[2]+score1[3]+score1[4]
                                            totj2 -= score1[0]+score1[1]+score1[2]+score1[3]+score1[4]
                                        else:
                                            xp=572
                                        point_rempli2[7] = 1
                                        bon=1
                                            
                                    if x>698 and x<759 and bon==0 and (suite==1 or test==0 and point_rempli2[8]==0):
                                        if test!=0:
                                            xp = 722
                                            c = str(20)
                                            totj2 += 20
                                        else:
                                            xp=715
                                        point_rempli2[8] = 1
                                        bon=1
                                            
                                    if x>759 and x<812 and bon==0 and (full==1 or test==0 and point_rempli2[9]==0):
                                        if test!=0:
                                            xp = 775
                                            c = str(30)
                                            totj2 += 30
                                        else:
                                            xp=770
                                        point_rempli2[9] = 1
                                        bon=1
                                            
                                    if x>812 and x<874 and bon==0 and (carre==1 or test==0 and point_rempli2[10]==0):
                                        if test!=0:
                                            xp = 835
                                            c = str(40)
                                            totj2 += 40
                                        else:
                                            xp=830
                                        point_rempli2[10] = 1
                                        bon=1
                                            
                                    if x>874 and x<938 and bon==0 and (yams==1 or test==0 and point_rempli2[11]==0):
                                        if test!=0:
                                            xp = 900
                                            c = str(50)
                                            totj2 += 50
                                        else:
                                            xp = 892
                                        point_rempli2[11] = 1
                                        bon=1
                                    

                            if c!=0 and xp!=0 and test!=0:
                                police = pygame.font.Font(None, 20)
                                texte = police.render(c,True, "black")
                                fenetre.blit(texte, (xp, yp))
                                pygame.display.flip()
                            elif test==0 and xp!=0:
                                bille = pygame.image.load("./image/yams/croix.png").convert_alpha()
                                bille = pygame.transform.scale(bille, (25, 25))
                                position_bille = [xp, yc] 
                                fenetre.blit(bille, position_bille)
                                pygame.display.flip()

                            
                            if kijou%2==0:
                                if tot1j1>=63 and bonus1==0:
                                    bonus1 = 1
                                    totj1 += 30
                                    police = pygame.font.Font(None, 20)
                                    texte = police.render(str(30),True, "red")
                                    rectText = texte.get_rect().width
                                    fenetre.blit(texte, (450, yp))
                                    pygame.display.flip()
                                elif point_rempli1[0] == point_rempli1[1] == point_rempli1[2] == point_rempli1[3] == point_rempli1[4] == point_rempli1[5] == 1 and bonus1==0:
                                    bonus1 = 1
                                    bille = pygame.image.load("./image/yams/croix.png").convert_alpha()
                                    bille = pygame.transform.scale(bille, (25, 25))
                                    position_bille = [445, yc] 
                                    fenetre.blit(bille, position_bille)
                                    pygame.display.flip()
                            else:
                                    if tot1j2>=63 and bonus2==0:
                                        bonus2 = 1
                                        totj2 += 30
                                        police = pygame.font.Font(None, 20)
                                        texte = police.render(str(30),True, "red")
                                        rectText = texte.get_rect().width
                                        fenetre.blit(texte, (450, yp))
                                        pygame.display.flip()
                                    elif point_rempli2[0] == point_rempli2[1] == point_rempli2[2] == point_rempli2[3] == point_rempli2[4] == point_rempli2[5] == 1 and bonus2==0:
                                        bonus2 = 1
                                        bille = pygame.image.load("./image/yams/croix.png").convert_alpha()
                                        bille = pygame.transform.scale(bille, (25, 25))
                                        position_bille = [445, yc] 
                                        fenetre.blit(bille, position_bille)
                                        pygame.display.flip()

                            
                            if kijou%2==0:
                                if tot1j1!=0:
                                    bille = pygame.image.load("./image/yams/cache.png").convert_alpha()
                                    bille = pygame.transform.scale(bille, (25, 25))
                                    position_bille = [370, yc] 
                                    fenetre.blit(bille, position_bille)

                                    police = pygame.font.Font(None, 20)
                                    texte = police.render(str(tot1j1),True, "red")
                                    rectText = texte.get_rect().width
                                    fenetre.blit(texte, (387-rectText/2, yp))
                                    pygame.display.flip()
                                if tot2j1!=0:
                                    bille = pygame.image.load("./image/yams/cache.png").convert_alpha()
                                    bille = pygame.transform.scale(bille, (25, 25))
                                    position_bille = [650, yc] 
                                    fenetre.blit(bille, position_bille)

                                    police = pygame.font.Font(None, 20)
                                    texte = police.render(str(tot2j1),True, "red")
                                    rectText = texte.get_rect().width
                                    fenetre.blit(texte, (659-rectText/2, yp))
                                    pygame.display.flip()

                                
                                bille = pygame.image.load("./image/yams/cache.png").convert_alpha()
                                bille = pygame.transform.scale(bille, (40, 25))
                                position_bille = [950, yc] 
                                fenetre.blit(bille, position_bille)

                                police = pygame.font.Font(None, 30)
                                texte = police.render(str(totj1),True, "green")
                                rectText = texte.get_rect().width
                                fenetre.blit(texte, (967-rectText/2, yp))
                                pygame.display.flip()
                            else:
                                    if tot1j2!=0:
                                        bille = pygame.image.load("./image/yams/cache.png").convert_alpha()
                                        bille = pygame.transform.scale(bille, (25, 25))
                                        position_bille = [370, yc] 
                                        fenetre.blit(bille, position_bille)

                                        police = pygame.font.Font(None, 20)
                                        texte = police.render(str(tot1j2),True, "red")
                                        rectText = texte.get_rect().width
                                        fenetre.blit(texte, (387-rectText/2, yp))
                                        pygame.display.flip()
                                    if tot2j2!=0:
                                        bille = pygame.image.load("./image/yams/cache.png").convert_alpha()
                                        bille = pygame.transform.scale(bille, (25, 25))
                                        position_bille = [650, yc] 
                                        fenetre.blit(bille, position_bille)

                                        police = pygame.font.Font(None, 20)
                                        texte = police.render(str(tot2j2),True, "red")
                                        rectText = texte.get_rect().width
                                        fenetre.blit(texte, (659-rectText/2, yp))
                                        pygame.display.flip()

                                    
                                    bille = pygame.image.load("./image/yams/cache.png").convert_alpha()
                                    bille = pygame.transform.scale(bille, (40, 25))
                                    position_bille = [950, yc] 
                                    fenetre.blit(bille, position_bille)

                                    police = pygame.font.Font(None, 30)
                                    texte = police.render(str(totj2),True, "green")
                                    rectText = texte.get_rect().width
                                    fenetre.blit(texte, (967-rectText/2, yp))
                                    pygame.display.flip()

                        

                        if point_rempli1 == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] and point_rempli2 == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]:
                            end=1
                            if totj1>totj2:   
                                bille = pygame.image.load("./image/yams/cache.png").convert_alpha()
                                bille = pygame.transform.scale(bille, (1000, 100))
                                position_bille = [0, 140] 
                                fenetre.blit(bille, position_bille)

                                police = pygame.font.Font(None, 76)
                                texte = police.render("Victoire du joueur 1",True, "green")
                                rectText = texte.get_rect().width 
                                fenetre.blit(texte, (500-rectText/2, 150))
                                pygame.display.flip()
                            else:
                                bille = pygame.image.load("./image/yams/cache.png").convert_alpha()
                                bille = pygame.transform.scale(bille, (1000, 100))
                                position_bille = [0, 140] 
                                fenetre.blit(bille, position_bille)

                                police = pygame.font.Font(None, 76)
                                texte = police.render("Victoire du joueur 2",True, "green")
                                rectText = texte.get_rect().width 
                                fenetre.blit(texte, (500-rectText/2, 150))
                                pygame.display.flip()

                        
                        
                        if x > 550 and x < 900 and y > 460 and y < 540 and bon==1:
                            fin=1
                            kijou+=1
                            
                            
                                        
                    if (event.type == KEYDOWN) or (event.type == QUIT): 
                        return 0
                    
if __name__ == '__main__':
    yams()