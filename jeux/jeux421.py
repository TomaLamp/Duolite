import sys
from pathlib import Path

# Ajouter le répertoire parent au sys.path pour permettre les imports quand le script est lancé individuellement
sys.path.insert(0, str(Path(__file__).parent.parent))

import pygame
import random
import pickle
from module.pygameCore import *
from module.LANscreen import *


def tirage(d1 : int, d2 : int, d3 : int) -> list:
    """Créé une liste de 3 dés avec des valeurs aleatoires"""

    l = [0, 0, 0]
    if d1==1:
        l[0] = random.randint(1, 6)
    if d2==1:
        l[1] = random.randint(1, 6)
    if d3==1:
        l[2] = random.randint(1, 6)

    return l

def affich(l : list, score : list, fenetre : pygame.Surface):
    """
    Affiche les 3 dés tiré par le joueur
    - l : la liste des valeurs de dés à afficher
    - score : la liste des dés à afficher
    - fenetre : la fenetre sur laquelle afficher l'image
    """

    if score[0]==0:
        for i in range(10):
            a = random.randint(1,6)
            printImage("./image/421/de"+str(a)+".jpg", (100, 100), [200, 200], fenetre)
            pygame.display.flip()
            pygame.time.wait(100)

        printImage("./image/421/de"+str(l[0])+".jpg", (100, 100), [200, 200], fenetre)
        pygame.display.flip()
    
    if score[1]==0:
        for i in range(10):
            a = random.randint(1,6)
            printImage("./image/421/de"+str(a)+".jpg", (100, 100), [450, 200], fenetre)
            pygame.display.flip()
            pygame.time.wait(100)

        printImage("./image/421/de"+str(l[1])+".jpg", (100, 100), [450, 200], fenetre)
        pygame.display.flip()

    if score[2]==0:
        for i in range(10):
            a = random.randint(1,6)
            printImage("./image/421/de"+str(a)+".jpg", (100, 100), [700, 200], fenetre)
            pygame.display.flip()
            pygame.time.wait(100)


        printImage("./image/421/de"+str(l[2])+".jpg", (100, 100), [700, 200], fenetre)
    
    pygame.display.flip()


def keep(d : int, pos : int, val : int, fenetre : pygame.Surface):
    """
    Permet de choisir les dés à garder et ceux à relancer
    - d : si le dé était gardé
    - pos : le position du dé (1, 2 ou 3)
    - val : la valeur du dé
    - fenetre : la fenetre sur laquelle afficher
    """

    if d==1:
        l='R'
    else:
        l=''

    p=[200, 450, 700] 
    printImage("./image/421/de"+l+str(val)+".jpg", (100, 100), [p[pos-1], 200], fenetre)
    pygame.display.flip()


def comptage(l : list) -> int:
    """retourne le nombre de points des dés presents dans la liste l"""

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


def jeux421(connexion=[None, None, None]):

    fenetre = initScreen((1000,600), "421", "#FFFF00", './image/421/icon.jpg')

    printImage("./image/421/play.png", (700, 472.73), [160,36], fenetre)
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
            if (event.type == pygame.MOUSEBUTTONUP):
                x = event.pos[0]
                y = event.pos[1]
                if x > 161 and x < 859 and y > 298 and y < 485:
                    if connexion[0]!=None:
                        quit = waitScreen(fenetre, connexion, "#E3C400", "#BE9F02", "421")
                        fenetre.fill("#FFFF00")
                        printImage("./image/421/play.png", (700, 472.73), [160,36], fenetre)
                        pygame.display.flip()
                        if quit=="NULL":
                            return 0
                        elif quit==1:
                            fin = 1 
                            conn = connexion[0]
                    else:
                        fin=1
                    
            if (event.type == pygame.QUIT): 
                return 0

    printImage("./image/421/jaune.png", (1000, 600), [0, 0], fenetre)

    printImage("./image/421/lancer.jpg", (350, 86.55), [100, 420], fenetre)

    printImage("./image/421/continuer.jpg", (350, 86.55), [550, 420], fenetre)

    printText(nomj1+" :", 33, "black", (950, 55), fenetre, Alignement="Right")

    printText(nomj2+" :", 33, "black", (950, 85), fenetre, Alignement="Right")

    printText("score :", 33, "black", (950, 20), fenetre, underline=True, Alignement="Right")

    printText(nomj1+" : "+str(0), 33, "black", (10, 90), fenetre)

    printText(nomj2+" : "+str(0), 33, "black", (10, 120), fenetre)

    printText("Pot :", 33, "black", (10, 10), fenetre)

    printText(str(21), 33, "black", (65, 10), fenetre)

    printText("Point :", 33, "black", (10, 60), fenetre, underline=True)

    pygame.display.flip()

    tour = 0
    coup_max=3
    score = [[],[]]
    kijou = 0
    point1 = 0
    point2 = 0
    pot = 21
    end = 0
    while end==0:
        
        if tour%2==0:
            printImage("./image/421/jaune.png", (50, 70), [950, 50], fenetre)
  
        printImage("./image/421/blanc.png", (100, 100), [200, 200], fenetre)

        printImage("./image/421/blanc.png", (100, 100), [450, 200], fenetre)

        printImage("./image/421/blanc.png", (100, 100), [700, 200], fenetre)

        printImage("./image/421/jaune.png", (520, 70), [250, 70], fenetre)

        printText("Au tour de " + (nomj1 if kijou%2==0 else nomj2), 76, "red", (500, 70), fenetre, Alignement="Center")

        pygame.display.flip()


        coup = 0
        fin=0
        d1 = 1
        d2 = 1
        d3 = 1
        score[kijou%2] = [0, 0, 0]

        while coup<coup_max and fin==0:
            x=0
            y=0
            for event in pygame.event.get():
                if (event.type == pygame.MOUSEBUTTONUP):
                        if conn==None or connexion[2]==True and kijou%2==0 or connexion[2]==False and kijou%2==1:
                            x = event.pos[0]
                            y = event.pos[1]
                            if conn!=None:
                                conn.send(pickle.dumps([x,y]))
                            
                if (event.type == pygame.QUIT): 
                    if conn!=None:
                        conn.send(pickle.dumps(["404"]))
                    return 0
            

            if conn!=None and connexion[2]==True and kijou%2==1 or connexion[2]==False and kijou%2==0:
                while True:
                    try:
                        data = pickle.loads(conn.recv(1024))
                        if len(data)!=0 and data[0]=="404":
                            result = quitScreen(fenetre, connexion, "#E3C400", "#BE9F02")
                            if result=="NULL":
                                return 0
                        else:
                            x=data[0]
                            y=data[1]
                            break
                    except BlockingIOError:
                        pass 

                    for event in pygame.event.get():
                        if (event.type == pygame.QUIT): 
                            conn.send(pickle.dumps(["404"]))
                            return 0


            if x > 99 and x < 449 and y > 419 and y < 502:
                if conn==None or connexion[2]==True and kijou%2==0 or connexion[2]==False and kijou%2==1:
                    lancer = tirage(d1, d2, d3)
                    if conn!=None:
                        conn.send(pickle.dumps(lancer))
                else:
                    while True:
                        try:
                            lancer = pickle.loads(conn.recv(1024))
                            break
                        except BlockingIOError:
                            pass 

                affich(lancer, score[kijou%2], fenetre)
                coup+=1
            if x > 200 and x < 300 and y > 200 and y < 300 and coup!=0:
                if d1 == 1:
                    keep(d1, 1, lancer[0], fenetre)
                    score[kijou%2][0] = lancer[0]
                    lancer[0] = 0
                    d1 = 0
                else:
                    keep(d1, 1, score[kijou%2][0], fenetre)
                    lancer[0] = score[kijou%2][0]
                    score[kijou%2][0] = 0
                    d1 = 1
            if x > 450 and x < 550 and y > 200 and y < 300 and coup!=0:
                if d2 == 1:
                    keep(d2, 2, lancer[1], fenetre)
                    score[kijou%2][1] = lancer[1]
                    lancer[1] = 0
                    d2 = 0
                else:
                    keep(d2, 2, score[kijou%2][1], fenetre)
                    lancer[1] = score[kijou%2][1]
                    score[kijou%2][1] = 0
                    d2 = 1
            if x > 700 and x < 800 and y > 200 and y < 300 and coup!=0:
                if d3 == 1:
                    keep(d3, 3, lancer[2], fenetre)
                    score[kijou%2][2] = lancer[2]
                    lancer[2] = 0
                    d3 = 0
                else:
                    keep(d3, 3, score[kijou%2][2], fenetre)
                    lancer[2] = score[kijou%2][2]
                    score[kijou%2][2] = 0
                    d3 = 1
            if x > 550 and x < 900 and y > 419 and y < 504 and coup!=0:
                fin=1

        
        if score[kijou%2][0] == 0:
            score[kijou%2][0] = lancer[0]
        if score[kijou%2][1] == 0:
            score[kijou%2][1] = lancer[1]
        if score[kijou%2][2] == 0:
            score[kijou%2][2] = lancer[2]
        score[kijou%2].sort()
        if score[kijou%2] == [1, 2, 4]:
            score[kijou%2].sort(reverse=True)

        if kijou%2 == 0:
            printText(str(score[kijou%2][0]) + str(score[kijou%2][1]) + str(score[kijou%2][2]), 33, "black", (955, 55), fenetre)
            pygame.display.flip()
        else:
            printText(str(score[kijou%2][0]) + str(score[kijou%2][1]) + str(score[kijou%2][2]), 33, "black", (955, 85), fenetre)
            pygame.display.flip()

        tour+=1
        if tour%2==0:
            jeton1 = comptage(score[0])
            jeton2 = comptage(score[1])

            valscore1 = score[0][0] + score[0][1] + score[0][2]
            valscore2 = score[1][0] + score[1][1] + score[1][2]

            
            coup_max = 3
            if score[0] == [1,2,2]:
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
            if score[1] == [1,2,2]:
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
        


        if tour%2==0:

            printImage("./image/421/jaune.png", (150, 60), [10, 90], fenetre)

            printText(nomj1+" : "+str(point1), 33, "black", (10, 90), fenetre)

            printText(nomj2+" : "+str(point2), 33, "black", (10, 120), fenetre)

            printImage("./image/421/jaune.png", (25, 25), [65, 10], fenetre)

            printText(str(pot), 33, "black", (65, 10), fenetre)

            pygame.display.flip()

        fin=0
        if pot==0 and(point1==0 or point2==0):
            if point1==0:
                winner = nomj1
            else:
                winner = nomj2
            point1 = 0
            point2 = 0
            pot = 21

            printImage("./image/421/jaune.png", (520, 70), [250, 70], fenetre)

            printText("Victoire de " + winner, 76, "#556B2F", (250, 70), fenetre)

            pygame.display.flip()

        if conn==None or connexion[2]==True and kijou%2==0 or connexion[2]==False and kijou%2==1:
            while fin==0:
                for event in pygame.event.get(): 
                    if (event.type == pygame.MOUSEBUTTONUP):
                    
                        x = event.pos[0]
                        y = event.pos[1]
                        if x > 550 and x < 900 and y > 419 and y < 504:
                            fin=1
                            if conn!=None:
                                conn.send(pickle.dumps(["next"]))

                    if (event.type == pygame.KEYDOWN):
                        if event.key==pygame.K_RETURN:
                            fin=1
                            if conn!=None:
                                    conn.send(pickle.dumps(["next"]))
                    
                    if (event.type == pygame.QUIT): 
                        if conn!=None:
                            conn.send(pickle.dumps(["404"]))
                        return 0
        else:
            while True:
                try:
                    data = pickle.loads(conn.recv(1024))
                    if len(data)!=0 and data[0]=="404":
                        result = quitScreen(fenetre, connexion, "#E3C400", "#BE9F02")
                        if result=="NULL":
                            return 0
                    else:
                        break
                except BlockingIOError:
                    pass 

                for event in pygame.event.get():
                    if (event.type == pygame.QUIT): 
                        conn.send(pickle.dumps(["404"]))
                        return 0
            
        if tour%2==1:
            kijou+=1
            coup_max = coup
    
if __name__ == "__main__":
    jeux421()