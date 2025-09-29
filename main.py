from pygame import *
import pygame
from module.pygameCore import *


def main():

    from jeux.chifoumi import chifoumi
    from jeux.morpion import morpion
    from jeux.bataille_naval import bataille_naval
    from jeux.puissance4 import puissance4
    from jeux.penduGame import pendu
    from jeux.Juste_prix import justePrix
    from jeux.jeux421 import jeux421
    from jeux.motus import motus
    from jeux.memorie import memory
    from jeux.mastermind import mastermind
    from jeux.yams import yams
    from jeux.boogle import boogle
    

    def restart(page, jeux):
        fenetre = initScreen((1000,600), "Main", "#001E6D", './image/icon main.jpg')

        printText("Choisissez un jeu", 62, "black", (320,10), fenetre, underline=True)
        printText('"Duolité, le n°1 des jeux seul ou a deux"', 28, "black", (318, 75), fenetre)


        police = pygame.font.Font(None, 14)
        texte = police.render("LAMPURE Thomas",True,"black")
        rectTexte = texte.get_rect()
        fenetre.blit(texte, (900, 10))

        police = pygame.font.Font(None, 14)
        texte = police.render("DUCASSE Léo",True,"black")
        rectTexte = texte.get_rect()
        fenetre.blit(texte, (900, 30))

        printImage("./image/logo.png", (172, 48), (10,10), fenetre)

        if page==1:

            printImage("./image/bataille_naval.jpg", (200, 114), (100,150), fenetre)
            printImage("./image/puissance4.png", (200, 114), (100,400), fenetre)
            printImage("./image/juste prix.jpg", (200, 114), (400,400), fenetre)
            printImage("./image/pendu.jpg", (200, 114), (400,150), fenetre)
            printImage("./image/chifoumi.jpg", (200, 114), (700,150), fenetre)
            printImage("./image/juste prix.jpg", (200, 114), (400,400), fenetre)
            printImage("./image/morpion.jpg", (200, 114), (700,400), fenetre)
            printImage("./image/fleche.png", (50, 50), (940,300), fenetre)
            pygame.display.flip()

        else:

            printImage("./image/4_21.png", (200, 114), (100,150), fenetre)
            printImage("./image/mastermind.jpg", (200, 114), (100,400), fenetre)
            printImage("./image/motus.png", (200, 114), (400,150), fenetre)
            printImage("./image/memory.jpg", (200, 114), (700,150), fenetre)
            printImage("./image/yams.jpg", (200, 114), (400,400), fenetre)
            printImage("./image/boogle.jpg", (200, 114), (700,400), fenetre)
            printImage("./image/fleche.png", (50, 50), (10,300), fenetre, 180)
            pygame.display.flip()
        

        c = 0
        for i in range(2):
            for j in range(3):

                rectWidth = printImage("./image/fond.jpg", (200, 30), (100+300*j,264+250*i), fenetre).width
                printText(jeux[c], 33, "white", (100+300*j + rectWidth/2, 269+250*i), fenetre, Alignement="Center")

                c += 1


        pygame.display.flip()


    jeux1 = ["Bataille navale", "Pendu", "Chifoumi", "Puissance 4", "Juste prix", "Morpion"]
    jeux2 = ["421", "Motus", "Mémorie", "Mastermind", "Yams", "Boogle"]
    page = 1

    restart(page, jeux1)

    fin = 0
    while fin == 0:
        for event in pygame.event.get():
            if (event.type == MOUSEBUTTONUP):
                    x = event.pos[0]
                    y = event.pos[1]
                    if y > 149 and y < 293:
                        if x<298 and x>99:
                            if page==1:
                                bataille_naval()
                                restart(page, jeux1) 
                            if page==2:
                                jeux421()
                                restart(page, jeux2)  
                        elif x<598 and x>400:
                            if page==1:
                                pendu()
                                restart(page, jeux1)
                            if page==2:
                                motus()
                                restart(page, jeux2) 
                        elif x<899 and x>700:
                            if page==1:
                                chifoumi()
                                restart(page, jeux1)
                            if page==2:
                                memory()
                                restart(page, jeux2) 
                    if y > 400 and y < 543:
                        if x<298 and x>99:
                            if page==1:
                                puissance4()
                                restart(page, jeux1)
                            if page==2:
                                mastermind()
                                restart(page, jeux2)
                        elif x<598 and x>400:
                            if page==1:
                                justePrix()
                                restart(page, jeux1)
                            if page==2:
                                yams()
                                restart(page, jeux2)
                        elif x<899 and x>700:
                            if page==1:
                                morpion()
                                restart(page, jeux1)
                            if page==2:
                                boogle()
                                restart(page, jeux2)
                    if page==1:
                        if x>940 and x<990 and y>300 and y<350:
                            page=2
                            restart(page, jeux2)
                    if page==2:
                        if x>10 and x<60 and y>300 and y<350:
                            page=1
                            restart(page, jeux1)
                    
            if (event.type == QUIT): 
                return 0

if __name__ == '__main__':
    main()