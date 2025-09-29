from pygame import *

def chifoumi():
    from fileinput import close
    from multiprocessing.connection import wait
    from random import randint
    import sys
    import pygame
    import webbrowser


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

                    if x>100 and x<199 and y>250 and y<349:
                        return 3
                    elif x>300 and x<399 and y>250 and y<349:
                        return 2
                    elif x>500 and x<599 and y>250 and y<349:
                        return 1

    def affiche_image(coup, kijou):
        if kijou==1:
            x=190
        else:
            x=410
        if coup==0:
            bille = pygame.image.load("./image/chifoumi/flou.jpg").convert_alpha()
            bille = pygame.transform.scale(bille, (100, 100))
            position_bille = [x, 85] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip()
        elif coup==1:
            bille = pygame.image.load("./image/chifoumi/pierre .png").convert_alpha()
            bille = pygame.transform.scale(bille, (100, 100))
            position_bille = [x, 85] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip()
        elif coup==2:
            bille = pygame.image.load("./image/chifoumi/feuille .png").convert_alpha()
            bille = pygame.transform.scale(bille, (100, 100))
            position_bille = [x, 85] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip()
        elif coup==3:
            bille = pygame.image.load("./image/chifoumi/ciseaux.png").convert_alpha()
            bille = pygame.transform.scale(bille, (100, 100))
            position_bille = [x, 85] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip()
        




    pygame.init()
    pygame.display.init()
    fenetre = pygame.display.set_mode((700,400))
    fenetre.fill("#F5411A")
    pygame.display.set_caption("Pierre feuille ciseaux")
    pygame_icon = pygame.image.load("./image/chifoumi/icon.jpg")
    pygame.display.set_icon(pygame_icon)
    pygame.display.flip()

    bille = pygame.image.load("./image/chifoumi/jouer.png").convert_alpha()
    bille = pygame.transform.scale(bille, (600, 420))
    fenetre.blit(bille, (50,-55))
    pygame.display.flip()

    fin = 0
    while fin == 0:
        for event in pygame.event.get():
            if (event.type == MOUSEBUTTONUP):
                x = event.pos[0]
                y = event.pos[1]
                if x > 49 and x < 649 and y > 171 and y < 365:
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
                if (event.type == KEYDOWN) or (event.type == QUIT): 
                    return 0

                if (event.type == MOUSEBUTTONDOWN):
                    x = event.pos[0]
                    y = event.pos[1]
                    

                    if x>170 and x<538 and y>49 and y<147:
                        a = 2
                        end = 1
                    elif x>170 and x<537 and y>250 and y<347:
                        a = 1
                        end = 1

            bille = pygame.image.load("./image/chifoumi/joueur1.png").convert_alpha()
            position_bille = [170, 250] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip()

            bille = pygame.image.load("./image/chifoumi/joueur2.png").convert_alpha()
            position_bille = [170, 50] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip()


        restart = 0
        while restart==0:
            fenetre.fill("#F5411A")
            pygame.display.flip()  

            bille = pygame.image.load("./image/chifoumi/ciseaux.png").convert_alpha()
            bille = pygame.transform.scale(bille, (100, 100))
            position_bille = [100, 250] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip()

            bille = pygame.image.load("./image/chifoumi/feuille .png").convert_alpha()
            bille = pygame.transform.scale(bille, (100, 100))
            position_bille = [300, 250] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip()

            bille = pygame.image.load("./image/chifoumi/pierre .png").convert_alpha()
            bille = pygame.transform.scale(bille, (100, 100))
            position_bille = [500, 250] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip()

            police = pygame.font.Font(None, 102)
            texte = police.render("VS",True,pygame.Color("black"))
            rectTexte = texte.get_rect()
            fenetre.blit(texte, (300, 100))
            pygame.display.flip()

            if a==2 :    
                ton_score = 0
                mon_score = 0
                no_manche = 0
                while mon_score < 10 and ton_score < 10:
                    bille = pygame.image.load("./image/chifoumi/fond.png")
                    bille = pygame.transform.scale(bille, (700, 400))
                    position_bille = [0, 0] 
                    fenetre.blit(bille, position_bille)

                    police = pygame.font.Font(None, 42)
                    texte = police.render("Joueur 1:",True,pygame.Color("black"))
                    rectTexte = texte.get_rect()
                    fenetre.blit(texte, (5, 5))

                    police = pygame.font.Font(None, 42)
                    texte = police.render(str(ton_score),True,pygame.Color("black"))
                    rectTexte = texte.get_rect()
                    fenetre.blit(texte, (140, 6))

                    police = pygame.font.Font(None, 42)
                    texte = police.render("Joueur 2:",True,pygame.Color("black"))
                    rectTexte = texte.get_rect()
                    fenetre.blit(texte, (5, 40))

                    police = pygame.font.Font(None, 42)
                    texte = police.render(str(mon_score),True,pygame.Color("black"))
                    rectTexte = texte.get_rect()
                    fenetre.blit(texte, (140, 40))
                    pygame.display.flip()

                    ton_coup = position()
                    if ton_coup=="NULL":
                        return 0
                    affiche_image(0, 1)
                    


                    mon_coup = position()
                    if mon_coup=="NULL":
                        return 0

                    affiche_image(ton_coup, 1)
                    affiche_image(mon_coup, 2)

                    pygame.time.wait(800)
                    
                    
                    ton_score = scores(mon_coup,ton_coup,mon_score, ton_score)[0]
                    mon_score = scores(mon_coup,ton_coup,mon_score, ton_score)[1]
                    
                if ton_score == 10 :
                    bille = pygame.image.load("./image/chifoumi/floue.png")
                    bille = pygame.transform.scale(bille, (700, 400))
                    position_bille = [0, 0] 
                    fenetre.blit(bille, position_bille)

                    bille = pygame.image.load("./image/pendu/fleche.png").convert_alpha()
                    bille = pygame.transform.scale(bille, (50,34.35))
                    bille = pygame.transform.rotate(bille, 180)
                    position_bille = [640, 10] 
                    fenetre.blit(bille, position_bille)

                    bille = pygame.image.load("./image/chifoumi/VJ1.png")
                    bille = pygame.transform.scale(bille, (500, 254.2))
                    position_bille = [101.5, 80] 
                    fenetre.blit(bille, position_bille)
                    pygame.display.flip()

                    end=0
                    while end==0:
                        for event in pygame.event.get():   
                            if (event.type == KEYDOWN) or (event.type == QUIT): 
                                return 0

                            if (event.type == MOUSEBUTTONDOWN):
                                x = event.pos[0]
                                y = event.pos[1]

                                if x>101 and x<600 and y>153 and y<261:
                                    end = 1
                                if(x>656 and x<686 and y>20 and y<31) or (x>640 and x<655 and y>11 and y<41):
                                    end=1
                                    restart=1

                if mon_score == 10 :
                    bille = pygame.image.load("./image/chifoumi/floue.png")
                    bille = pygame.transform.scale(bille, (700, 400))
                    position_bille = [0, 0] 
                    fenetre.blit(bille, position_bille)

                    bille = pygame.image.load("./image/pendu/fleche.png").convert_alpha()
                    bille = pygame.transform.scale(bille, (50,34.35))
                    bille = pygame.transform.rotate(bille, 180)
                    position_bille = [640, 10] 
                    fenetre.blit(bille, position_bille)

                    bille = pygame.image.load("./image/chifoumi/VJ2.png")
                    bille = pygame.transform.scale(bille, (500, 254.2))
                    position_bille = [101.5, 80] 
                    fenetre.blit(bille, position_bille)
                    pygame.display.flip()

                    end=0
                    while end==0:
                        for event in pygame.event.get():   
                            if (event.type == KEYDOWN) or (event.type == QUIT): 
                                return 0

                            if (event.type == MOUSEBUTTONDOWN):
                                x = event.pos[0]
                                y = event.pos[1]

                                if x>101 and x<600 and y>153 and y<261:
                                    end = 1
                                if(x>656 and x<686 and y>20 and y<31) or (x>640 and x<655 and y>11 and y<41):
                                    end=1
                                    restart=1


            if a==1 :
                    
                ton_score = 0
                mon_score = 0
                no_manche = 0
                while mon_score < 10 and ton_score < 10:
                    bille = pygame.image.load("./image/chifoumi/fond.png")
                    bille = pygame.transform.scale(bille, (700, 400))
                    position_bille = [0, 0] 
                    fenetre.blit(bille, position_bille)
                    pygame.display.flip()

                    police = pygame.font.Font(None, 42)
                    texte = police.render("Joueur 1:",True,pygame.Color("black"))
                    rectTexte = texte.get_rect()
                    fenetre.blit(texte, (5, 5))
                    pygame.display.flip()

                    police = pygame.font.Font(None, 42)
                    texte = police.render(str(ton_score),True,pygame.Color("black"))
                    rectTexte = texte.get_rect()
                    fenetre.blit(texte, (140, 6))
                    pygame.display.flip()


                    police = pygame.font.Font(None, 42)
                    texte = police.render("Ordinateur:",True,pygame.Color("black"))
                    rectTexte = texte.get_rect()
                    fenetre.blit(texte, (5, 40))
                    pygame.display.flip()

                    police = pygame.font.Font(None, 42)
                    texte = police.render(str(mon_score),True,pygame.Color("black"))
                    rectTexte = texte.get_rect()
                    fenetre.blit(texte, (170, 40))
                    pygame.display.flip()

                    ton_coup = position()
                    if ton_coup=="NULL":
                        return 0
                    affiche_image(ton_coup, 1)
                    
                
                    
                    mon_coup = randint(1,3)
                    affiche_image(mon_coup, 2)
                
                    ton_score = scores(mon_coup,ton_coup,mon_score, ton_score)[0]
                    mon_score = scores(mon_coup,ton_coup,mon_score, ton_score)[1]
                    
                    pygame.time.wait(800)
                
                if ton_score == 10 :
                    bille = pygame.image.load("./image/chifoumi/floue.png")
                    bille = pygame.transform.scale(bille, (700, 400))
                    position_bille = [0, 0] 
                    fenetre.blit(bille, position_bille)

                    bille = pygame.image.load("./image/pendu/fleche.png").convert_alpha()
                    bille = pygame.transform.scale(bille, (50,34.35))
                    bille = pygame.transform.rotate(bille, 180)
                    position_bille = [640, 10] 
                    fenetre.blit(bille, position_bille)

                    bille = pygame.image.load("./image/chifoumi/victoire.png")
                    bille = pygame.transform.scale(bille, (500, 181.62))
                    position_bille = [101.5, 100] 
                    fenetre.blit(bille, position_bille)
                    pygame.display.flip()

                    end=0
                    while end==0:
                        for event in pygame.event.get():   
                            if (event.type == KEYDOWN) or (event.type == QUIT): 
                                return 0
                            if (event.type == MOUSEBUTTONDOWN):
                                x = event.pos[0]
                                y = event.pos[1]

                                if x>101 and x<600 and y>172 and y<280:
                                    end = 1
                                if(x>656 and x<686 and y>20 and y<31) or (x>640 and x<655 and y>11 and y<41):
                                    end=1
                                    restart=1
                    

                if mon_score == 10 :
                    bille = pygame.image.load("./image/chifoumi/floue.png")
                    bille = pygame.transform.scale(bille, (700, 400))
                    position_bille = [0, 0] 
                    fenetre.blit(bille, position_bille)

                    bille = pygame.image.load("./image/chifoumi/perdu.png")
                    bille = pygame.transform.scale(bille, (500, 207.8))
                    position_bille = [101.5, 75] 
                    fenetre.blit(bille, position_bille)

                    bille = pygame.image.load("./image/pendu/fleche.png").convert_alpha()
                    bille = pygame.transform.scale(bille, (50,34.35))
                    bille = pygame.transform.rotate(bille, 180)
                    position_bille = [640, 10] 
                    fenetre.blit(bille, position_bille)
                    pygame.display.flip()

                    end=0
                    while end==0:
                        for event in pygame.event.get():   
                            if (event.type == KEYDOWN) or (event.type == QUIT): 
                                return 0

                            if (event.type == MOUSEBUTTONDOWN):
                                x = event.pos[0]
                                y = event.pos[1]

                                if x>101 and x<600 and y>174 and y<281:
                                    end = 1
                                if(x>656 and x<686 and y>20 and y<31) or (x>640 and x<655 and y>11 and y<41):
                                    end=1
                                    restart=1
            




            
            


