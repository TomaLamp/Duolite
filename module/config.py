import pygame
from pygame import *
from module.pygameCore import *
import time

def configScreen(fenetre):
    pygame.draw.rect(fenetre, "#272728", (205,105,600,400), border_radius=50)
    pygame.draw.rect(fenetre, "#001751", (200,100,600,400), border_radius=50)

    pygame.draw.rect(fenetre, "#334676", (250,215,500,50), border_radius=50)
    pygame.draw.rect(fenetre, "#334676", (250,335,500,50), border_radius=50)
    pygame.draw.rect(fenetre, "#000000", (400,425,200,50))

    printImage("./image/close.png", (30, 30), (750, 120), fenetre)
    printText("Nom joueur 1 :", 32, "black", (265, 190), fenetre)
    printText("Nom joueur 2 :", 32, "black", (265, 310), fenetre)
    printText("Sauvegarder", 32, "white", (500, 450), fenetre, Alignement="Center", Alignementy="Center")
    printText("Configuration", 50, "black", (500, 110), fenetre, Alignement="Center")

    fichier = open("./annexes/log.txt", "r")
    log = fichier.read()   
    fichier.close()
    nom = log.split(';')

    nomj1 = nom[0]
    nomj2 = nom[1]
    choose = 0
    x=0
    y=0

    printText(nomj1, 60, "#535353", (260, 240), fenetre, Alignementy="Center")
    printText(nomj2, 60, "#535353", (260, 360), fenetre, Alignementy="Center")
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            letter=""
            if (event.type == pygame.MOUSEBUTTONUP):
                x = event.pos[0]
                y = event.pos[1]

                if x>750 and x<780 and y>120 and y<150:
                    return 0
                elif x>250 and x<750 and y>215 and y<275:
                    choose=1
                elif x>250 and x<750 and y>335 and y<385:
                    choose=2
                elif x>400 and x<600 and y>425 and y<475:
                    nom = nomj1+";"+nomj2
                    fichier = open("./annexes/log.txt", "w")
                    log = fichier.write(nom)   
                    fichier.close()
                    return 0
                elif x!=0 and y!=0:
                    choose=0

            if event.type == KEYDOWN:
                if pygame.key.get_pressed()[K_LSHIFT] and event.key<=122 and event.key>=97:
                    letter = chr(event.key).upper()
                elif event.key<=122 and event.key>=97:
                    letter = chr(event.key)
                elif event.key==K_BACKSPACE:
                    letter = "<"
                elif event.key==K_SPACE:
                    letter=" "
                elif event.key>1073741912 and event.key<1073741922:
                    letter = str(event.key-1073741912)
                elif event.key == 1073741922:
                    letter = "0"
                elif event.key==13:
                    if choose==0:
                        nom = nomj1+";"+nomj2
                        fichier = open("./annexes/log.txt", "w")
                        log = fichier.write(nom)   
                        fichier.close()
                        return 0
                    else:
                        choose=0
            
                if choose==1:
                    if letter == "<":
                        nomj1 = nomj1[:len(nomj1)-1]
                    elif len(nomj1)<9:
                        nomj1 += letter
                if choose==2:
                    if letter == "<":
                        nomj2 = nomj2[:len(nomj2)-1]
                    elif len(nomj2)<9:
                        nomj2 += letter

            if (event.type == pygame.QUIT): 
                    sys.exit()
        
        
        if choose==1:
            pygame.draw.rect(fenetre, "#334676", (250,215,500,50), border_radius=50)
            pygame.draw.rect(fenetre, "#334676", (250,335,500,50), border_radius=50)
            printText(nomj2, 60, "#535353", (260, 360), fenetre, Alignementy="Center")
                
            rectText = printText(nomj1, 60, "#959595", (260, 240), fenetre, Alignementy="Center").width
                
            if time.time() % 1 > 0.5:
                pygame.draw.rect(fenetre, "black", (rectText+260, 220, 2, 40))
            pygame.display.update()

        if choose==2:
            pygame.draw.rect(fenetre, "#334676", (250,215,500,50), border_radius=50)
            printText(nomj1, 60, "#535353", (260, 240), fenetre, Alignementy="Center")
            pygame.draw.rect(fenetre, "#334676", (250,335,500,50), border_radius=50)

            rectText = printText(nomj2, 60, "#959595", (260, 360), fenetre, Alignementy="Center").width

            if time.time() % 1 > 0.5:
                pygame.draw.rect(fenetre, "black", (rectText+260, 340, 2, 40))
            pygame.display.update()

        if choose==0:
            pygame.draw.rect(fenetre, "#334676", (250,215,500,50), border_radius=50)
            pygame.draw.rect(fenetre, "#334676", (250,335,500,50), border_radius=50)
            printText(nomj1, 60, "#535353", (260, 240), fenetre, Alignementy="Center")
            printText(nomj2, 60, "#535353", (260, 360), fenetre, Alignementy="Center")
            
        pygame.display.flip()
