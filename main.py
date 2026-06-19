import pygame
from module.pygameCore import *
from module.config import *
from module.LANscreen import *


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
    

    def restart(page, jeux, fenetre):
        
        fenetre.fill("#001E6D")
        pygame.display.set_caption("Main")
        pygame_icon = pygame.image.load('./image/icon main.jpg')
        pygame.display.set_icon(pygame_icon)
        printText("Choisissez un jeu", 62, "black", (320,10), fenetre, underline=True)
        printText('"Duolité, le n°1 des jeux seul ou a deux"', 28, "black", (318, 75), fenetre)
        printImage("./image/reglage.png", (30, 30), (960, 50), fenetre)
        pygame.draw.rect(fenetre, "black", (735, 10, 130, 40), 2)
        printImage("./image/connLAN.png", (30, 30), (740, 15), fenetre)
        printText("Connexion LAN", 17, "black", (775, 30),fenetre, Alignementy="Center")

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
    jeux = list(jeux1)
    page = 1

    connexion = [None, None, None]
    fenetre = initScreen((1000,600), "Main", "#001E6D", './image/icon main.jpg')
    restart(page, jeux1, fenetre)

    fin = 0
    while fin == 0:
        if connexion[0]!=None:
            if isConnClose(connexion[0]):
                connexion[0].close()
                decoScreen(fenetre, connexion)
                connexion = [None, None, None]
                restart(page, jeux, fenetre)

        for event in pygame.event.get():
            if (event.type == pygame.MOUSEBUTTONUP):
                    x = event.pos[0]
                    y = event.pos[1]
                    if y > 149 and y < 293:
                        if x<298 and x>99:
                            if page==1:
                                bataille_naval(connexion)
                                restart(page, jeux1, fenetre) 
                            if page==2:
                                jeux421(connexion)
                                restart(page, jeux2, fenetre)  
                        elif x<598 and x>400:
                            if page==1:
                                pendu(connexion)
                                restart(page, jeux1, fenetre)
                            if page==2:
                                motus(connexion)
                                restart(page, jeux2, fenetre) 
                        elif x<899 and x>700:
                            if page==1:
                                chifoumi(connexion)
                                restart(page, jeux1, fenetre)
                            if page==2:
                                memory(connexion)
                                restart(page, jeux2, fenetre) 
                    if y > 400 and y < 543:
                        if x<298 and x>99:
                            if page==1:
                                puissance4(connexion)
                                restart(page, jeux1, fenetre)
                            if page==2:
                                mastermind(connexion)
                                restart(page, jeux2, fenetre)
                        elif x<598 and x>400:
                            if page==1:
                                justePrix(connexion)
                                restart(page, jeux1, fenetre)
                            if page==2:
                                yams(connexion)
                                restart(page, jeux2, fenetre)
                        elif x<899 and x>700:
                            if page==1:
                                morpion(connexion)
                                restart(page, jeux1, fenetre)
                            if page==2:
                                boogle(connexion)
                                restart(page, jeux2, fenetre)
                    if page==1:
                        if x>940 and x<990 and y>300 and y<350:
                            page=2
                            jeux = list(jeux2)
                            restart(page, jeux2, fenetre)
                    if page==2:
                        if x>10 and x<60 and y>300 and y<350:
                            page=1
                            jeux = list(jeux1)
                            restart(page, jeux1, fenetre)
                    if x>960 and x<990 and y>50 and y<80:
                        configScreen(fenetre)
                        restart(page, jeux, fenetre)
                    if x>735 and x<865 and y>10 and y<50:
                        LANscreen(fenetre, connexion)
                        restart(page, jeux, fenetre)
                    
            if (event.type == pygame.QUIT): 
                if connexion[0]!=None:
                    connexion[0].close()
                return 0

if __name__ == '__main__':
    main()