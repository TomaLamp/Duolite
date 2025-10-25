from pygame import *
from random import randint
from module.pygameCore import *
import pygame
from module.LANscreen import *

def chifoumi(connexion=[None,None,None]):

    # --- Nouvelle taille ---
    NEW_WIDTH = 1000
    NEW_HEIGHT = 600


    # --- Ancienne taille (base du jeu) ---
    BASE_WIDTH = 700
    BASE_HEIGHT = 400


    # Facteurs d'échelle
    scale_x = NEW_WIDTH / BASE_WIDTH
    scale_y = NEW_HEIGHT / BASE_HEIGHT


    def scores(mon_coup,ton_coup,mon_score,ton_score):
        if mon_coup == 1 and ton_coup == 2:
            ton_score += 1
        elif mon_coup == 2 and ton_coup == 1:
            mon_score += 1
        elif mon_coup == 1 and ton_coup == 3:
            mon_score += 1
        elif mon_coup == 3 and ton_coup == 1:
            ton_score += 1
        elif mon_coup == 3 and ton_coup == 2:
            mon_score += 1
        elif mon_coup == 2 and ton_coup == 3:
            ton_score += 1
        return ton_score, mon_score

    def position():
        end = 0
        while end==0:
            for event in pygame.event.get():   
                if (event.type == QUIT): 
                    return "NULL"

                if (event.type == MOUSEBUTTONDOWN):
                    x = event.pos[0]
                    y = event.pos[1]

                    if x>100*scale_x and x<199*scale_x and y>250*scale_y and y<349*scale_y:
                        return 3
                    elif x>300*scale_x and x<399*scale_x and y>250*scale_y and y<349*scale_y:
                        return 2
                    elif x>500*scale_x and x<599*scale_x and y>250*scale_y and y<349*scale_y:
                        return 1

    def affiche_image(coup, kijou):
        if kijou==1:
            x=190*scale_x
        else:
            x=410*scale_x
        if coup==0:
            printImage("./image/chifoumi/flou.jpg", (100*scale_x, 100*scale_y), (x, 85*scale_y), fenetre)
        elif coup==1:
            printImage("./image/chifoumi/pierre.png", (100*scale_x, 100*scale_y), (x, 85*scale_y), fenetre)
        elif coup==2:
            printImage("./image/chifoumi/feuille.png", (100*scale_x, 100*scale_y), (x, 85*scale_y), fenetre)
        elif coup==3:
            printImage("./image/chifoumi/ciseaux.png", (100*scale_x, 100*scale_y), (x, 85*scale_y), fenetre)
        pygame.display.flip()
        
    fenetre =initScreen((NEW_WIDTH,NEW_HEIGHT), "Pierre feuille ciseaux", "#F5411A", "./image/chifoumi/icon.jpg")

    printImage("./image/chifoumi/jouer.png", (600*scale_x, 420*scale_y), (50*scale_x,-55*scale_y), fenetre)
    pygame.display.flip()

    nomj1, nomj2 = get_nom()

    conn = None
    if connexion[0]!=None and connexion[2]==True:
        nomj2=connexion[1]
    elif connexion[0]!=None and connexion[2]==False:
        nomj2=nomj1
        nomj1=connexion[1]

    fin = 0
    while fin == 0:
        for event in pygame.event.get():
            if (event.type == MOUSEBUTTONUP):
                x = event.pos[0]
                y = event.pos[1]
                if x > 49*scale_x and x < 649*scale_x and y > 171*scale_y and y < 365*scale_y:
                    fin = 1 
            
            if (event.type == KEYDOWN) or (event.type == QUIT):
                return 0 



    start = 0
    while start==0:
        fenetre.fill("#F5411A")
        pygame.display.flip()
        end=0
        while end==0:
            for event in pygame.event.get():   
                if(event.type == QUIT): 
                    return 0

                if (event.type == MOUSEBUTTONDOWN):
                    x = event.pos[0]
                    y = event.pos[1]
                    

                    if x>170*scale_x and x<538*scale_x and y>49*scale_y and y<147*scale_y:
                        if connexion[0]!=None:
                            quit = waitScreen(fenetre, connexion, "#D82A03", "#6F1E00", "chifoumi")
                            fenetre.fill("#F5411A")
                            printImage("./image/chifoumi/joueur1.png", (371*scale_x, 99*scale_y), (170*scale_x, 250*scale_y), fenetre)
                            printImage("./image/chifoumi/joueur2.png", (371*scale_x, 99*scale_y), (170*scale_x, 50*scale_y), fenetre)
                            pygame.display.flip()
                            if quit=="NULL":
                                return 0
                            elif quit==1:
                                end=1
                                a=2
                                conn = connexion[0]
                        else:
                            end=1
                            a=2
                    elif x>170*scale_x and x<537*scale_x and y>250*scale_y and y<347*scale_y:
                        a = 1
                        end = 1
        
            printImage("./image/chifoumi/joueur1.png", (371*scale_x, 99*scale_y), (170*scale_x, 250*scale_y), fenetre)
            printImage("./image/chifoumi/joueur2.png", (371*scale_x, 99*scale_y), (170*scale_x, 50*scale_y), fenetre)
            pygame.display.flip()


        restart = 0
        while restart==0:
            fenetre.fill("#F5411A")

            printImage("./image/chifoumi/ciseaux.png", (100*scale_x, 100*scale_y), (100*scale_x, 250*scale_y), fenetre)
            printImage("./image/chifoumi/feuille.png", (100*scale_x, 100*scale_y), (300*scale_x, 250*scale_y), fenetre)
            printImage("./image/chifoumi/pierre.png", (100*scale_x, 100*scale_y), (500*scale_x, 250*scale_y), fenetre)
            printText("VS", int(102*scale_y), "black", (300*scale_x, 100*scale_y), fenetre)
            pygame.display.flip()

            if a==2 or a==1:    
                ton_score = 0
                mon_score = 0
                while mon_score < 10 and ton_score < 10:

                    printImage("./image/chifoumi/fond.png", (1000, 600), (0, 0), fenetre)
                    printText(nomj1+" : " + str(ton_score), int(42*scale_y), "black", (5*scale_x, 5*scale_y), fenetre)
                    if a==2:
                        printText(nomj2+" : " + str(mon_score), int(42*scale_y), "black", (5*scale_x, 40*scale_y), fenetre)
                    elif a==1:
                        printText("Ordinateur : " + str(mon_score), int(42*scale_y), "black", (5*scale_x, 40*scale_y), fenetre)

                    pygame.display.flip()

                    
                    ton_coup = position()
                    if ton_coup=="NULL":
                        return 0

                    if a==2:
                        if conn == None:
                            affiche_image(0, 1)
                            ton_coup = position()
                        else:
                            affiche_image(ton_coup, 1)
                            conn.send(ton_coup.to_bytes(1))
                            mon_coup = recv_int_data(connexion, fenetre, "#D82A03", "#6F1E00")
                        
                        if mon_coup=="NULL":
                            return 0
                    elif a==1:
                        mon_coup = randint(1,3)


                    affiche_image(ton_coup, 1)
                    affiche_image(mon_coup, 2)

                    pygame.time.wait(800)
                    
                    ton_score = scores(mon_coup,ton_coup,mon_score, ton_score)[0]
                    mon_score = scores(mon_coup,ton_coup,mon_score, ton_score)[1]

                if mon_score == 10 or ton_score==10:
                    printImage("./image/chifoumi/floue.png", (700*scale_x, 400*scale_y), (0*scale_x, 0*scale_y), fenetre)
                    printImage("./image/pendu/fleche.png", (50*scale_x, 34.35*scale_y), (640*scale_x, 10*scale_y), fenetre, rotation=180)

                    if mon_score==10 and (conn!=None or a==1):
                        printImage("./image/chifoumi/perdu.png", (500*scale_x, 207.8*scale_y), (101.5*scale_x, 75*scale_y), fenetre)
                    elif ton_score==10 and (conn!=None or a==1):
                        printImage("./image/chifoumi/victoire.png", (500*scale_x, 181.62*scale_y), (101.5*scale_x, 100*scale_y), fenetre)
                    elif(a==2 and mon_score==10):
                        printImage("./image/chifoumi/VJ2.png", (500*scale_x, 254.2*scale_y), (101.5*scale_x, 80*scale_y), fenetre)
                    elif(a==2 and ton_score==10):
                        printImage("./image/chifoumi/VJ1.png", (500*scale_x, 254.2*scale_y), (101.5*scale_x, 80*scale_y), fenetre)
                    
                    pygame.display.flip()

                    end=0
                    while end==0:
                        for event in pygame.event.get():   
                            if(event.type == QUIT): 
                                if conn!=None:
                                    conn.send((404).to_bytes(2))
                                return 0

                            if (event.type == MOUSEBUTTONDOWN):
                                x = event.pos[0]
                                y = event.pos[1]

                                if x>101*scale_x and x<600*scale_x and y>153*scale_y and y<261*scale_y:
                                    end = 1
                                if(x>656*scale_x and x<686*scale_x and y>20*scale_y and y<31*scale_y) or (x>640*scale_x and x<655*scale_x and y>11*scale_y and y<41*scale_y):
                                    end=1
                                    restart=1
                                    if conn!=None:
                                        conn.send((404).to_bytes(2))
                            
                            if(event.type == KEYDOWN): 
                                if event.key==K_RETURN:
                                    end = 1

if __name__ == "__main__":
    chifoumi()
    



            
            


