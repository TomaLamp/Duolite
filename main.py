from pygame import *
import pygame


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
        pygame.init()
        pygame.font.init()
        fenetre = pygame.display.set_mode((1000,600))
        fenetre.fill("#001E6D")
        pygame.display.set_caption("Main")
        pygame_icon = pygame.image.load('./image/icon main.jpg')
        pygame.display.set_icon(pygame_icon)

        police = pygame.font.Font(None, 62)
        police.underline = True
        texte = police.render("Choisissez un jeu",True,"black")
        rectTexte = texte.get_rect()
        fenetre.blit(texte, (320, 10))

        police = pygame.font.Font(None, 28)
        texte = police.render('"Duolité, le n°1 des jeux seul ou a deux"',True,"black")
        rectTexte = texte.get_rect()
        fenetre.blit(texte, (318, 75))

        police = pygame.font.Font(None, 14)
        texte = police.render("LAMPURE Thomas",True,"black")
        rectTexte = texte.get_rect()
        fenetre.blit(texte, (900, 10))

        police = pygame.font.Font(None, 14)
        texte = police.render("DUCASSE Léo",True,"black")
        rectTexte = texte.get_rect()
        fenetre.blit(texte, (900, 30))

        bille = pygame.image.load("./image/logo.png").convert_alpha()
        bille = pygame.transform.scale(bille, (172, 48))
        position_bille = [10,10] 
        fenetre.blit(bille, position_bille)

        if page==1:

            bille = pygame.image.load("./image/bataille_naval.jpg").convert_alpha()
            bille = pygame.transform.scale(bille, (200, 114))
            position_bille = [100,150] 
            fenetre.blit(bille, position_bille)

            bille = pygame.image.load("./image/puissance4.png").convert_alpha()
            bille = pygame.transform.scale(bille, (200, 114))
            position_bille = [100,400] 
            fenetre.blit(bille, position_bille)

            bille = pygame.image.load("./image/pendu.jpg").convert_alpha()
            bille = pygame.transform.scale(bille, (200, 114))
            position_bille = [400,150] 
            fenetre.blit(bille, position_bille)

            bille = pygame.image.load("./image/chifoumi.jpg").convert_alpha()
            bille = pygame.transform.scale(bille, (200, 114))
            position_bille = [700,150] 
            fenetre.blit(bille, position_bille)

            bille = pygame.image.load("./image/juste prix.jpg").convert_alpha()
            bille = pygame.transform.scale(bille, (200, 114))
            position_bille = [400,400] 
            fenetre.blit(bille, position_bille)

            bille = pygame.image.load("./image/morpion.jpg").convert_alpha()
            bille = pygame.transform.scale(bille, (200, 114))
            position_bille = [700,400] 
            fenetre.blit(bille, position_bille)

            bille = pygame.image.load("./image/fleche.png").convert_alpha()
            bille = pygame.transform.scale(bille, (50, 50))
            position_bille = [940,300] 
            fenetre.blit(bille, position_bille)

            pygame.display.flip()

        else:

            bille = pygame.image.load("./image/4_21.png").convert_alpha()
            bille = pygame.transform.scale(bille, (200, 114))
            position_bille = [100,150] 
            fenetre.blit(bille, position_bille)

            bille = pygame.image.load("./image/mastermind.jpg").convert_alpha()
            bille = pygame.transform.scale(bille, (200, 114))
            position_bille = [100,400] 
            fenetre.blit(bille, position_bille)

            bille = pygame.image.load("./image/motus.png").convert_alpha()
            bille = pygame.transform.scale(bille, (200, 114))
            position_bille = [400,150] 
            fenetre.blit(bille, position_bille)

            bille = pygame.image.load("./image/memory.jpg").convert_alpha()
            bille = pygame.transform.scale(bille, (200, 114))
            position_bille = [700,150] 
            fenetre.blit(bille, position_bille)

            bille = pygame.image.load("./image/yams.jpg").convert_alpha()
            bille = pygame.transform.scale(bille, (200, 114))
            position_bille = [400,400] 
            fenetre.blit(bille, position_bille)

            bille = pygame.image.load("./image/boogle.jpg").convert_alpha()
            bille = pygame.transform.scale(bille, (200, 114))
            position_bille = [700,400] 
            fenetre.blit(bille, position_bille)

            bille = pygame.image.load("./image/fleche.png").convert_alpha()
            bille = pygame.transform.scale(bille, (50, 50))
            bille = pygame.transform.rotate(bille, 180)
            position_bille = [10,300] 
            fenetre.blit(bille, position_bille)
            

            pygame.display.flip()
        

        c = 0
        for i in range(2):
            for j in range(3):
                bille = pygame.image.load("./image/fond.jpg").convert_alpha()
                bille = pygame.transform.scale(bille, (200, 30))
                position_bille = [100+300*j,264+250*i] 
                rectWidth = bille.get_rect().width 
                fenetre.blit(bille, position_bille)

                police = pygame.font.Font(None, 33)
                texte = police.render(jeux[c],True, "white")
                rectTexte = texte.get_rect().width
                fenetre.blit(texte, (100+300*j + rectWidth/2 - rectTexte/2, 269+250*i))

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