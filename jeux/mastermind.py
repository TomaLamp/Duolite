from pygame import *
import pygame
from random import *
from module.pygameCore import *


def mastermind():

    def affich_combi(l, tour):

        yb = [85, 127, 155, 183, 212, 241, 269, 298, 326, 354, 383, 412, 440, 469, 497, 526, 554]
        xb = [447, 475, 503, 531]

        for i in range(len(l)):
            if l[i]=="blanc":
                printImage("./image/mastermind/p_blanc.png", (20, 20), [xb[i]+i,yb[17-tour]+3], fenetre)
            else:
                printImage(f"./image/mastermind/p_{l[i]}.png", (25, 25), [xb[i],yb[17-tour]], fenetre)
            pygame.display.flip()

    fenetre = initScreen((1000,600), "mastermind", "#DD00E4", './image/mastermind/icon.jpg')

    printImage("./image/mastermind/play.png", (700, 426.84), (150,60), fenetre)
    pygame.display.flip()

    nomj1, nomj2 = get_nom()
                

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
            printImage("./image/mastermind/1joueur.png", (750, 185.7), [125, 65], fenetre)
            pygame.display.flip()
            printImage("./image/mastermind/2joueur.png", (750, 185.7), [125, 350], fenetre)
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
        printImage("./image/mastermind/blanc.jpg", (50, 50), [30,470], fenetre)
        printImage("./image/mastermind/rouge.png", (50, 50), [80,470], fenetre)
        printImage("./image/mastermind/vert.png", (50, 50), [130,470], fenetre)
        printImage("./image/mastermind/orange.jpg", (50, 50), [30,520], fenetre)
        printImage("./image/mastermind/bleu.jpg", (50, 50), [80,520], fenetre)
        printImage("./image/mastermind/jaune.jpg", (50, 50), [130,520], fenetre)
        printImage("./image/mastermind/blanc.jpg", (50, 100), [180,470], fenetre)
        printImage("./image/mastermind/effacer.png", (20, 20), [195,480], fenetre)
        printText("Supp", 20, "black", (188, 520), fenetre)
        printImage("./image/mastermind/suivant.png", (200, 49.33), [770,495], fenetre)

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

            printImage("./image/mastermind/cache.png", (70, 60), [0,0], fenetre)

            kijou=kijou_start
            if nbjoueur==1:
                printImage("./image/mastermind/cache.png", (800, 55), [140,10], fenetre)
                printText("Choisissez une combinaison", 60, "black", (235,20), fenetre)
                printText("Mes points :", 30, "black", (10,180), fenetre, underline=True)
                printText("Parties jouées :", 30, "black", (835,180), fenetre, underline=True)
                printText(str(point1), 30, "black", (10,220), fenetre)
                printText(str(partie), 30, "black", (970,220), fenetre)
            else:

                printText(nomj1+" :", 30, "black", (10,180), fenetre, underline=True)
                printText(nomj2+" :", 30, "black", (990,180), fenetre, underline=True, Alignement="Right")
                printText(str(point1), 30, "black", (10,220), fenetre)
                printText(str(point2), 30, "black", (970,220), fenetre)

            printImage("./image/mastermind/cache.png", (450, 550), [285,78], fenetre)
            printImage("./image/mastermind/plateau.png", (182, 506), [410,80], fenetre)
            pygame.display.flip()

            couleur = ["rouge","blanc","vert","orange","bleu","jaune"]
            combinaison = []
            for i in range(4):
                combinaison.append(choice(couleur))

            tour=1
            end=0
            while end==0 and tour<17:

                if nbjoueur==2:
                    printImage("./image/mastermind/cache.png", (800, 55), [140,10], fenetre)
                    if kijou%2==0:
                        printText(nomj1+" choisissez une combinaison", 60, "black", (500,20), fenetre, Alignement="Center")
                    else:
                        printText(nomj2+" choisissez une combinaison", 60, "black", (500,20), fenetre, Alignement="Center")
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

                                printImage("./image/mastermind/fond.png", (170, 22.58), [xc,yc[16-tour]], fenetre)
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

                                printImage("./image/mastermind/blanc.jpg", (30*place, 22.58), [592,yc[16-tour]+3], fenetre)
                                printImage("./image/mastermind/rouge.png", (30*bon, 22.58), [410-30*bon,yc[16-tour]+3], fenetre)
                                if place!=0:
                                    printText(str(place), 20, "black", (595,yc[16-tour]+8), fenetre)
                                if bon!=0:
                                    printText(str(bon), 20, "black", (395,yc[16-tour]+8), fenetre)
                                
                                pygame.display.flip()
                                tour+=1
                            

                                
                                
                                            
                        if (event.type == KEYDOWN) or (event.type == QUIT): 
                            return 0

            
            affich_combi(combinaison, 17)

            if nbjoueur==1:
                point1+= 17-tour
                partie+=1

                printImage("./image/mastermind/cache.png", (800, 55), [140,10], fenetre)
                if end==1:
                    printText("Gagné", 60, "green", (438,20), fenetre)
                else:
                    printText("Perdu", 60, "red", (438,20), fenetre)
                
                printImage("./image/mastermind/cache.png", (30, 30), [10,220], fenetre)
                printImage("./image/mastermind/cache.png", (30, 30), [970,220], fenetre)
                printText(str(point1), 30, "black", (10,220), fenetre)
                printText(str(partie), 30, "black", (970,220), fenetre)
                pygame.display.flip()

            else:

                printImage("./image/mastermind/cache.png", (800, 55), [140,10], fenetre)
                if kijou%2==0:
                    point1+=17-tour
                    printText("Victoire de "+nomj1, 60, "green", (500,20), fenetre, Alignement="Center")
                else:
                    point2+=17-tour
                    printText("Victoire de "+nomj2, 60, "green", (500,20), fenetre, Alignement="Center")
                
                printImage("./image/mastermind/cache.png", (30, 30), [10,220], fenetre)
                printImage("./image/mastermind/cache.png", (30, 30), [970,220], fenetre)
                printText(str(point1), 30, "black", (10,220), fenetre)
                printText(str(point2), 30, "black", (970,220), fenetre)
                pygame.display.flip()
            
            kijou_start+=1

            printImage("./image/juste prix/fleche.png", (50,34.35), [5, 10], fenetre, rotation=180)
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

if __name__ == "__main__":
    mastermind()