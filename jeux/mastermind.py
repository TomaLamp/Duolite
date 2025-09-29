from pygame import *
import pygame
from random import *


def mastermind():

    def affich_combi(l, tour):

        yb = [85, 127, 155, 183, 212, 241, 269, 298, 326, 354, 383, 412, 440, 469, 497, 526, 554]
        xb = [447, 475, 503, 531]

        for i in range(len(l)):
            if l[i]=="blanc":
                bille = pygame.image.load("./image/mastermind/p_blanc.png").convert_alpha()
                bille = pygame.transform.scale(bille, (20, 20))
                position_bille = [xb[i]+i,yb[17-tour]+3] 
                fenetre.blit(bille, position_bille)
            else:
                bille = pygame.image.load("./image/mastermind/p_"+l[i]+".png").convert_alpha()
                bille = pygame.transform.scale(bille, (25, 25))
                position_bille = [xb[i],yb[17-tour]] 
                fenetre.blit(bille, position_bille)
            pygame.display.flip()


    pygame.init()
    pygame.font.init()
    fenetre = pygame.display.set_mode((1000,600))
    fenetre.fill("#DD00E4")
    pygame.display.set_caption("mastermind")
    pygame_icon = pygame.image.load('./image/mastermind/icon.jpg')
    pygame.display.set_icon(pygame_icon)

    bille = pygame.image.load("./image/mastermind/play.png").convert_alpha()
    bille = pygame.transform.scale(bille, (700, 426.84))
    fenetre.blit(bille, (150,60))
    pygame.display.flip()
                

    fin = 0
    while fin == 0:
        for event in pygame.event.get():
            if (event.type == MOUSEBUTTONUP):
                x = event.pos[0]
                y = event.pos[1]

                if x > 150 and x < 850 and y > 60 and y < 487:
                    fin = 1 
                            
            if (event.type == KEYDOWN) or (event.type == QUIT): 
                return 0



    start=0
    while start==0:
        fenetre.fill("#DD00E4")
        end = 0
        while end==0:
            bille = pygame.image.load("./image/mastermind/1joueur.png")
            bille = pygame.transform.scale(bille, (750, 185.7))
            position_bille = [125, 65] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip()

            bille = pygame.image.load("./image/mastermind/2joueur.png")
            bille = pygame.transform.scale(bille, (750, 185.7))
            position_bille = [125, 350] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip()

            for event in pygame.event.get():

                if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]
                        if x>125 and x<875 and y>65 and y<250.7:
                            end=1
                            nbjoueur = 1
                        elif x>125 and x<875 and y>350 and y<535.7:
                            end=1
                            nbjoueur = 2


                if (event.type == QUIT): 
                    return 0



        fenetre.fill("#DD00E4")
        bille = pygame.image.load("./image/mastermind/blanc.jpg").convert_alpha()
        bille = pygame.transform.scale(bille, (50, 50))
        position_bille = [30,470] 
        fenetre.blit(bille, position_bille)

        bille = pygame.image.load("./image/mastermind/rouge.png").convert_alpha()
        bille = pygame.transform.scale(bille, (50, 50))
        position_bille = [80,470] 
        fenetre.blit(bille, position_bille)

        bille = pygame.image.load("./image/mastermind/vert.png").convert_alpha()
        bille = pygame.transform.scale(bille, (50, 50))
        position_bille = [130,470] 
        fenetre.blit(bille, position_bille)

        bille = pygame.image.load("./image/mastermind/orange.jpg").convert_alpha()
        bille = pygame.transform.scale(bille, (50, 50))
        position_bille = [30,520] 
        fenetre.blit(bille, position_bille)

        bille = pygame.image.load("./image/mastermind/bleu.jpg").convert_alpha()
        bille = pygame.transform.scale(bille, (50, 50))
        position_bille = [80,520] 
        fenetre.blit(bille, position_bille)

        bille = pygame.image.load("./image/mastermind/jaune.jpg").convert_alpha()
        bille = pygame.transform.scale(bille, (50, 50))
        position_bille = [130,520] 
        fenetre.blit(bille, position_bille)

        bille = pygame.image.load("./image/mastermind/blanc.jpg").convert_alpha()
        bille = pygame.transform.scale(bille, (50, 100))
        position_bille = [180,470] 
        fenetre.blit(bille, position_bille)

        bille = pygame.image.load("./image/mastermind/effacer.png").convert_alpha()
        bille = pygame.transform.scale(bille, (20, 20))
        position_bille = [195,480] 
        fenetre.blit(bille, position_bille)

        police = pygame.font.Font(None, 20)
        texte = police.render("Supp",True, "black")
        fenetre.blit(texte, (188, 520))

        bille = pygame.image.load("./image/mastermind/suivant.png").convert_alpha()
        bille = pygame.transform.scale(bille, (200, 49.33))
        position_bille = [770,495] 
        fenetre.blit(bille, position_bille)


        yc = [128, 156, 184, 213, 242, 270, 299, 327, 355, 384, 413, 442, 470, 499, 527, 555]
        xc = 416

        yb = [84, 127, 155, 183, 212, 241, 269, 298, 326, 354, 383, 412, 440, 469, 497, 526, 554]
        xb = [447, 475, 503, 531]

        kijou_start = 0
        point1=0
        point2=0
        partie = 0
        restart=0
        while restart==0:

            bille = pygame.image.load("./image/mastermind/cache.png").convert_alpha()
            bille = pygame.transform.scale(bille, (70, 60))
            position_bille = [0,0] 
            fenetre.blit(bille, position_bille)

            kijou=kijou_start
            if nbjoueur==1:
                bille = pygame.image.load("./image/mastermind/cache.png").convert_alpha()
                bille = pygame.transform.scale(bille, (800, 55))
                position_bille = [140,10] 
                fenetre.blit(bille, position_bille)

                police = pygame.font.Font(None, 60)
                texte = police.render("Choisissez une combinaison",True, "black")
                fenetre.blit(texte, (235,20))

                police = pygame.font.Font(None, 30)
                police.underline = True
                texte = police.render("Mes points :",True, "black")
                fenetre.blit(texte, (10,180))

                police = pygame.font.Font(None, 30)
                police.underline = True
                texte = police.render("Parties jouées :",True, "black")
                fenetre.blit(texte, (835,180))

                police = pygame.font.Font(None, 30)
                texte = police.render(str(point1),True, "black")
                fenetre.blit(texte, (10,220))

                police = pygame.font.Font(None, 30)
                texte = police.render(str(partie),True, "black")
                fenetre.blit(texte, (970,220))
            else:

                police = pygame.font.Font(None, 30)
                police.underline = True
                texte = police.render("Joueur 1 :",True, "black")
                fenetre.blit(texte, (10,180))

                police = pygame.font.Font(None, 30)
                police.underline = True
                texte = police.render("Joueur 2 :",True, "black")
                fenetre.blit(texte, (890,180))

                police = pygame.font.Font(None, 30)
                texte = police.render(str(point1),True, "black")
                fenetre.blit(texte, (10,220))

                police = pygame.font.Font(None, 30)
                texte = police.render(str(point2),True, "black")
                fenetre.blit(texte, (970,220))

            bille = pygame.image.load("./image/mastermind/cache.png").convert_alpha()
            bille = pygame.transform.scale(bille, (450, 550))
            position_bille = [285,78] 
            fenetre.blit(bille, position_bille)

            bille = pygame.image.load("./image/mastermind/plateau.png").convert_alpha()
            bille = pygame.transform.scale(bille, (182, 506))
            position_bille = [410,80] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip()

            couleur = ["rouge","blanc","vert","orange","bleu","jaune"]
            combinaison = []
            for i in range(4):
                combinaison.append(choice(couleur))

            tour=1
            end=0
            while end==0 and tour<17:

                if nbjoueur==2:
                    bille = pygame.image.load("./image/mastermind/cache.png").convert_alpha()
                    bille = pygame.transform.scale(bille, (800, 55))
                    position_bille = [140,10] 
                    fenetre.blit(bille, position_bille)

                    if kijou%2==0:
                        police = pygame.font.Font(None, 60)
                        texte = police.render("Joueur 1 Choisissez une combinaison",True, "black")
                        fenetre.blit(texte, (150,20))
                    else:
                        police = pygame.font.Font(None, 60)
                        texte = police.render("Joueur 2 Choisissez une combinaison",True, "black")
                        fenetre.blit(texte, (150,20))
                    pygame.display.flip()

                choix=[]
                fin = 0
                while fin == 0:
                    for event in pygame.event.get():
                        if (event.type == MOUSEBUTTONUP):
                            x = event.pos[0]
                            y = event.pos[1]
                            #print(x,y)
                            if x > 30 and x < 180 and y > 470 and y < 570 and len(choix)<4:
                                if y > 470 and y < 520:
                                    if x<80:
                                        choix.append("blanc")
                                    elif x<130:
                                        choix.append("rouge")
                                    elif x<180:
                                        choix.append("vert")
                                elif y > 520 and y < 570:
                                    if x<80:
                                        choix.append("orange")
                                    elif x<130:
                                        choix.append("bleu")
                                    elif x<180:
                                        choix.append("jaune")
                                affich_combi(choix, tour)
                            if x > 180 and x < 230 and y > 470 and y < 570 and len(choix)!=0:
                                del choix[-1]

                                bille = pygame.image.load("./image/mastermind/fond.png").convert_alpha()
                                bille = pygame.transform.scale(bille, (170, 22.58))
                                position_bille = [xc,yc[16-tour]] 
                                fenetre.blit(bille, position_bille)
                                pygame.display.flip()

                                affich_combi(choix, tour)

                            if x>771 and x<970 and y>495 and y<540 and len(choix)==4:
                                verif = list(combinaison)
                                bon=0
                                place=0
                                j=0
                                l_verif = [0,0,0,0]
                                for i in range(4):
                                    if choix[i]==combinaison[i]:
                                        bon+=1
                                        del verif[i-j]
                                        j+=1
                                        l_verif[i]=1
                                
                                if bon!=4:
                                    for i in range(len(choix)):
                                        if l_verif[i]!=1 and choix[i] in verif:
                                            place+=1
                                            del verif[verif.index(choix[i])]
                                    fin=1
                                    kijou+=1
                                else:
                                    print("gagné")
                                    fin=1
                                    end=1

                                bille = pygame.image.load("./image/mastermind/blanc.jpg").convert_alpha()
                                bille = pygame.transform.scale(bille, (30*place, 22.58))
                                position_bille = [592,yc[16-tour]+3] 
                                fenetre.blit(bille, position_bille)

                                bille = pygame.image.load("./image/mastermind/rouge.png").convert_alpha()
                                bille = pygame.transform.scale(bille, (30*bon, 22.58))
                                position_bille = [410-30*bon,yc[16-tour]+3] 
                                fenetre.blit(bille, position_bille)

                                if place!=0:
                                    police = pygame.font.Font(None, 20)
                                    texte = police.render(str(place),True, "black")
                                    fenetre.blit(texte, (595,yc[16-tour]+8))
                                if bon!=0:
                                    police = pygame.font.Font(None, 20)
                                    texte = police.render(str(bon),True, "black")
                                    fenetre.blit(texte, (395,yc[16-tour]+8))

                                pygame.display.flip()
                                tour+=1
                            

                                
                                
                                            
                        if (event.type == KEYDOWN) or (event.type == QUIT): 
                            return 0

            
            affich_combi(combinaison, 17)

            if nbjoueur==1:
                point1+= 17-tour
                partie+=1

                bille = pygame.image.load("./image/mastermind/cache.png").convert_alpha()
                bille = pygame.transform.scale(bille, (800, 55))
                position_bille = [140,10] 
                fenetre.blit(bille, position_bille)

                if end==1:
                    police = pygame.font.Font(None, 60)
                    texte = police.render("Gagné",True, "green")
                    fenetre.blit(texte, (438,20))
                else:
                    police = pygame.font.Font(None, 60)
                    texte = police.render("Perdu",True, "red")
                    fenetre.blit(texte, (438,20))


                bille = pygame.image.load("./image/mastermind/cache.png").convert_alpha()
                bille = pygame.transform.scale(bille, (30, 30))
                position_bille = [10,220] 
                fenetre.blit(bille, position_bille)

                bille = pygame.image.load("./image/mastermind/cache.png").convert_alpha()
                bille = pygame.transform.scale(bille, (30, 30))
                position_bille = [970,220] 
                fenetre.blit(bille, position_bille)

                police = pygame.font.Font(None, 30)
                texte = police.render(str(point1),True, "black")
                fenetre.blit(texte, (10,220))

                police = pygame.font.Font(None, 30)
                texte = police.render(str(partie),True, "black")
                fenetre.blit(texte, (970,220))

                pygame.display.flip()

            else:

                bille = pygame.image.load("./image/mastermind/cache.png").convert_alpha()
                bille = pygame.transform.scale(bille, (800, 55))
                position_bille = [140,10] 
                fenetre.blit(bille, position_bille)

                if kijou%2==0:
                    point1+=17-tour
                    police = pygame.font.Font(None, 60)
                    texte = police.render("Victoire joueur 1",True, "green")
                    fenetre.blit(texte, (350,20))
                else:
                    point2+=17-tour
                    police = pygame.font.Font(None, 60)
                    texte = police.render("Victoire joueur 2",True, "green")
                    fenetre.blit(texte, (350,20))

                bille = pygame.image.load("./image/mastermind/cache.png").convert_alpha()
                bille = pygame.transform.scale(bille, (30, 30))
                position_bille = [10,220] 
                fenetre.blit(bille, position_bille)

                bille = pygame.image.load("./image/mastermind/cache.png").convert_alpha()
                bille = pygame.transform.scale(bille, (30, 30))
                position_bille = [970,220] 
                fenetre.blit(bille, position_bille)

                police = pygame.font.Font(None, 30)
                texte = police.render(str(point1),True, "black")
                fenetre.blit(texte, (10,220))

                police = pygame.font.Font(None, 30)
                texte = police.render(str(point2),True, "black")
                fenetre.blit(texte, (970,220))

                pygame.display.flip()
            
            kijou_start+=1

            bille = pygame.image.load("./image/juste prix/fleche.png").convert_alpha()
            bille = pygame.transform.scale(bille, (50,34.35))
            bille = pygame.transform.rotate(bille, 180)
            position_bille = [5, 10] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip() 

            end=0
            while end==0:
                for event in pygame.event.get():
                    if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]
                        if x>771 and x<970 and y>495 and y<540:
                            end=1
                        if(x>21 and x<51 and y>20 and y<31) or (x>5 and x<20 and y>11 and y<41):
                            restart=1
                            end=1


                    if (event.type == KEYDOWN) or (event.type == QUIT): 
                        return 0

