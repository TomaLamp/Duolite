from pygame import *
import pygame

def justePrix():
    from random import randint

    def choix_nombre():
        nombre = ""
        fin = 0
        while fin == 0:
            for event in pygame.event.get():
                if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]
                        if x > 400 and x < 450 and y > 340 and y < 390:
                            if len(nombre)<3:
                                nombre += "7"   
                        if x > 470 and x < 520 and y > 400 and y < 450:
                            if len(nombre)<3:
                                nombre += "5" 
                        if x > 540 and x < 590 and y > 460 and y < 510:
                            if len(nombre)<3:
                                nombre += "3" 
                        if x > 470 and x < 520 and y > 340 and y < 390:
                            if len(nombre)<3:
                                nombre += "8" 
                        if x > 400 and x < 450 and y > 400 and y < 450:
                            if len(nombre)<3:
                                nombre += "4" 
                        if x > 400 and x < 450 and y > 460 and y < 510:
                            if len(nombre)<3:
                                nombre += "1" 
                        if x > 470 and x < 520 and y > 460 and y < 510:
                            if len(nombre)<3:
                                nombre += "2" 
                        if x > 540 and x < 590 and y > 340 and y < 390:
                            if len(nombre)<3:
                                nombre += "9" 
                        if x > 540 and x < 590 and y > 400 and y < 450:
                            if len(nombre)<3:
                                nombre += "6" 
                        if x > 400 and x < 450 and y > 520 and y < 570:
                            nombre = nombre[0:len(nombre)-1]
                        if x > 470 and x < 520 and y > 520 and y < 570:
                            if len(nombre)<3:
                                nombre += "0"
                        if x > 540 and x < 590 and y > 520 and y < 570:
                            if len(nombre) != 0:
                                return int(nombre)
                        

                
                if event.type == KEYDOWN:
                    if len(nombre)<3:
                        if event.key>1073741912 and event.key<1073741922:
                            nombre += str(event.key-1073741912)
                        elif event.key == 1073741922:
                            nombre += "0"
                    if event.key == 8:
                        nombre = nombre[0:len(nombre)-1]
                    elif event.key == 13:
                        if len(nombre) != 0:
                            return int(nombre)

                if event.type == KEYDOWN or event.type == MOUSEBUTTONUP:
                    bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                    bille = pygame.transform.scale(bille, (90, 50))
                    position_bille = [445, 270]
                    rectWidth = bille.get_rect().width 
                    fenetre.blit(bille, position_bille) 

                    police = pygame.font.Font(None, 72)
                    texte = police.render(nombre,True, "black")
                    rectTexte = texte.get_rect().width
                    fenetre.blit(texte, (rectWidth/2 - rectTexte/2 +445, 270))
                    pygame.display.flip()  

                if (event.type == QUIT): 
                    return "NULL"

                
                


    pygame.init()
    pygame.font.init()
    fenetre = pygame.display.set_mode((1000,600))
    fenetre.fill("#B707C6")
    pygame.display.set_caption("Juste prix")
    pygame_icon = pygame.image.load('./image/juste prix/icon.png')
    pygame.display.set_icon(pygame_icon)
    pygame.display.flip()


    bille = pygame.image.load("./image/juste prix/play.png").convert_alpha()
    bille = pygame.transform.scale(bille, (700, 549.5))
    position_bille = [150,-10] 
    fenetre.blit(bille, position_bille)
    pygame.display.flip()

    fin = 0
    while fin == 0:
        for event in pygame.event.get():
            if (event.type == MOUSEBUTTONUP):
                    x = event.pos[0]
                    y = event.pos[1]
                    if y > 324 and y < 539 and x > 150 and x < 850:
                        fin=1
            
            if (event.type == QUIT): 
                    return 0



    start = 0
    while start == 0:

        fenetre.fill("#B707C6")

        bille = pygame.image.load("./image/juste prix/joueur1.png").convert_alpha()
        bille = pygame.transform.scale(bille, (700, 173.1))
        position_bille = [160, 70] 
        fenetre.blit(bille, position_bille)

        bille = pygame.image.load("./image/juste prix/joueur2.png").convert_alpha()
        bille = pygame.transform.scale(bille, (700, 173.1))
        position_bille = [160, 370] 
        fenetre.blit(bille, position_bille)
        pygame.display.flip()




        fin = 0
        while fin == 0:
            for event in pygame.event.get():
                if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]
                        if x > 159 and x < 858 and y > 69 and y < 236:
                            nbrj = 1 
                            fin=1
                        if x > 159 and x < 858 and y > 369 and y < 536:
                            nbrj = 2 
                            fin=1
                
                if (event.type == QUIT): 
                    return 0
                
                

        nbr_essais = 13
        kijou = -1
        borne_sup = 1000
        borne_min = 1


        fenetre.fill("#B707C6")
        c = 12
        for i in range(4):
            c -= 5
            for j in range(3):
                bille = pygame.image.load("./image/juste prix/nbr.png").convert_alpha()
                bille = pygame.transform.scale(bille, (50, 50))
                position_bille = [400+70*j, 340+60*i] 
                fenetre.blit(bille, position_bille)

                if c<10 and c>0:
                    police = pygame.font.Font(None, 33)
                    texte = police.render(str(c),True, "black")
                    fenetre.blit(texte, (420+70*j, 355+60*i))
                    pygame.display.flip()
                elif c==-2:
                    bille = pygame.image.load("./image/juste prix/effacer.png").convert_alpha()
                    bille = pygame.transform.scale(bille, (40, 40))
                    position_bille = [405+70*j, 345+60*i] 
                    fenetre.blit(bille, position_bille)
                elif c==-1:
                    police = pygame.font.Font(None, 33)
                    texte = police.render(str(0),True, "black")
                    fenetre.blit(texte, (420+70*j, 355+60*i))
                    pygame.display.flip()
                elif c==0:
                    bille = pygame.image.load("./image/juste prix/entrer.png").convert_alpha()
                    bille = pygame.transform.scale(bille, (40, 40))
                    position_bille = [405+70*j, 345+60*i] 
                    fenetre.blit(bille, position_bille)
                
                if j != 2: 
                    c+=1                      



        police = pygame.font.Font(None, 72)
        texte = police.render(str(borne_min) + "<", True, "black")
        fenetre.blit(texte, (350, 270))
        police = pygame.font.Font(None, 72)
        texte = police.render( "<" + str(borne_sup), True, "black")
        fenetre.blit(texte, (550, 270))
        pygame.display.flip()


        police = pygame.font.Font(None, 36)
        texte = police.render("Nombre d'essai max :  ",True, "black")
        fenetre.blit(texte, (10, 10))

        police = pygame.font.Font(None, 36)
        texte = police.render("Ton nombre de coup :  ",True, "black")
        fenetre.blit(texte, (690, 10))
        pygame.display.flip()


        if nbrj==1 :
            restart=0
            while restart==0:
                nbr_essais = 13
                point = 0
                end=0
                while end==0:
                    nbr_essais_max = nbr_essais
                    nbr_essais = 1
                    borne_sup = 1000
                    borne_min = 1
                    mon_nombre = randint(2,999)  
                    ton_nombre = 0

                    bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                    bille = pygame.transform.scale(bille, (30, 30))
                    position_bille = [270, 10] 
                    fenetre.blit(bille, position_bille)

                    bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                    bille = pygame.transform.scale(bille, (1000, 200))
                    position_bille = [20, 110] 
                    fenetre.blit(bille, position_bille)

                    bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                    bille = pygame.transform.scale(bille, (60, 60))
                    position_bille = [5, 40] 
                    fenetre.blit(bille, position_bille)

                    police = pygame.font.Font(None, 36)
                    texte = police.render("Tes points :  " + str(point),True, "black")
                    fenetre.blit(texte, (10, 500))

                    police = pygame.font.Font(None, 36)
                    texte = police.render(str(nbr_essais_max),True, "black")
                    fenetre.blit(texte, (270, 10))

                    police = pygame.font.Font("./police/Sketchzone.otf", 76)
                    texte = police.render("Choisissez un nombre : ",True, "Yellow")
                    fenetre.blit(texte, (120, 70))
                    pygame.display.flip()

                    while ton_nombre != mon_nombre and nbr_essais <= nbr_essais_max:

                        bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                        bille = pygame.transform.scale(bille, (30, 30))
                        position_bille = [960, 10] 
                        fenetre.blit(bille, position_bille)

                        police = pygame.font.Font(None, 36)
                        texte = police.render(str(nbr_essais),True, "black")
                        fenetre.blit(texte, (960, 10))

                        bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                        bille = pygame.transform.scale(bille, (450, 50))
                        position_bille = [300, 270] 
                        fenetre.blit(bille, position_bille)

                        police = pygame.font.Font(None, 72)
                        texte = police.render((3-len(str(borne_min)))* "  " + str(borne_min) + "<", True, "black")
                        fenetre.blit(texte, (320, 270))
                        police = pygame.font.Font(None, 72)
                        texte = police.render( "<" + str(borne_sup), True, "black")
                        fenetre.blit(texte, (550, 270))
                        pygame.display.flip()

                        ton_nombre = choix_nombre()
                        if ton_nombre == "NULL":
                            return 0

                        bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                        bille = pygame.transform.scale(bille, (450, 70))
                        position_bille = [400, 190] 
                        fenetre.blit(bille, position_bille)

                        if ton_nombre < mon_nombre and borne_min < ton_nombre and borne_sup > ton_nombre:
                            
                            police = pygame.font.Font("./police/Sketchzone.otf", 66)
                            texte = police.render("Plus",True, "green")
                            fenetre.blit(texte, (440, 180))
                            pygame.display.flip()

                            nbr_essais += 1
                            borne_min = ton_nombre
                        elif ton_nombre > mon_nombre and borne_min < ton_nombre and borne_sup > ton_nombre:
                            
                            police = pygame.font.Font("./police/Sketchzone.otf", 66)
                            texte = police.render("Moins",True, "red")
                            fenetre.blit(texte, (420, 180))
                            pygame.display.flip()

                            borne_sup = ton_nombre
                            nbr_essais += 1
                        elif ton_nombre == mon_nombre:
                            point += 13 - nbr_essais

                            bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                            bille = pygame.transform.scale(bille, (200, 50))
                            position_bille = [10, 500] 
                            fenetre.blit(bille, position_bille)

                            police = pygame.font.Font(None, 36)
                            texte = police.render("Tes points :  " + str(point),True, "black")
                            fenetre.blit(texte, (10, 500))
                        
                            bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                            bille = pygame.transform.scale(bille, (1000, 100))
                            position_bille = [120, 70] 
                            fenetre.blit(bille, position_bille)

                            police = pygame.font.Font("./police/Sketchzone.otf", 52)
                            texte = police.render("Bravo ! Vous avez trouvé en "+str(nbr_essais)+" essais",True, "Green")
                            fenetre.blit(texte, (55, 110))

                            police = pygame.font.Font("./police/Sketchzone.otf", 52)
                            texte = police.render("Le nombre était : "+str(mon_nombre),True, "Green")
                            fenetre.blit(texte, (240, 180))
                            pygame.display.flip()

                            bille = pygame.image.load("./image/juste prix/suivant.png").convert_alpha()
                            bille = pygame.transform.scale(bille, (300, 80.7))
                            position_bille = [680, 500] 
                            fenetre.blit(bille, position_bille)
                            pygame.display.flip()

                            bille = pygame.image.load("./image/juste prix/fleche.png").convert_alpha()
                            bille = pygame.transform.scale(bille, (50,34.35))
                            bille = pygame.transform.rotate(bille, 180)
                            position_bille = [5, 40] 
                            fenetre.blit(bille, position_bille)
                            pygame.display.flip() 

                            fin = 0
                            while fin == 0:
                                for event in pygame.event.get():
                                    if (event.type == MOUSEBUTTONUP):
                                        x = event.pos[0]
                                        y = event.pos[1]
                                        if x > 680 and x < 977 and y > 500 and y < 579:
                                            fin=1
                                            bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                                            bille = pygame.transform.scale(bille, (300, 82))
                                            position_bille = [680, 500] 
                                            fenetre.blit(bille, position_bille)
                                            pygame.display.flip()
                                        if(x>21 and x<51 and y>50 and y<61) or (x>5 and x<20 and y>41 and y<71):
                                            fin=1
                                            restart=1
                                            end=1
                    
                                    if (event.type == QUIT): 
                                        return 0

                        
                        if nbr_essais>nbr_essais_max and ton_nombre != mon_nombre :

                            bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                            bille = pygame.transform.scale(bille, (450, 70))
                            position_bille = [400, 190] 
                            fenetre.blit(bille, position_bille)

                            bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                            bille = pygame.transform.scale(bille, (1000, 130))
                            position_bille = [120, 70] 
                            fenetre.blit(bille, position_bille)

                            police = pygame.font.Font("./police/Sketchzone.otf", 62)
                            texte = police.render("Perdu ! Vous n'avez plus d'essai",True, "Red")
                            fenetre.blit(texte, (50, 110))

                            police = pygame.font.Font("./police/Sketchzone.otf", 62)
                            texte = police.render("Le nombre était : "+str(mon_nombre),True, "Red")
                            fenetre.blit(texte, (210, 180))
                            pygame.display.flip()

                            bille = pygame.image.load("./image/juste prix/rejouer.png").convert_alpha()
                            bille = pygame.transform.scale(bille, (300, 80.7))
                            position_bille = [680, 500] 
                            fenetre.blit(bille, position_bille)
                            pygame.display.flip()

                            bille = pygame.image.load("./image/juste prix/fleche.png").convert_alpha()
                            bille = pygame.transform.scale(bille, (50,34.35))
                            bille = pygame.transform.rotate(bille, 180)
                            position_bille = [5, 40] 
                            fenetre.blit(bille, position_bille)
                            pygame.display.flip() 

                            fin = 0
                            while fin == 0:
                                for event in pygame.event.get():
                                    if (event.type == MOUSEBUTTONUP):
                                        x = event.pos[0]
                                        y = event.pos[1]
                                        if x > 680 and x < 977 and y > 500 and y < 579:
                                            fin = 1
                                            end=1
                                            bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                                            bille = pygame.transform.scale(bille, (300, 82))
                                            position_bille = [680, 500] 
                                            fenetre.blit(bille, position_bille)
                                            bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                                            bille = pygame.transform.scale(bille, (200, 50))
                                            position_bille = [10, 500] 
                                            fenetre.blit(bille, position_bille)
                                            pygame.display.flip()
                                        if(x>21 and x<51 and y>50 and y<61) or (x>5 and x<20 and y>41 and y<71):
                                            fin=1
                                            restart=1
                                            end=1


                                    if (event.type == QUIT): 
                                        return 0


                
            








        pointj1 = 0
        pointj2 = 0

        if nbrj==2 :
            restart=0
            kijou += 1
            while restart==0:
                nbr_essais = 13
                end=0                
                while end == 0:

                    nbr_essais_max = nbr_essais
                    nbr_essais = 1
                    borne_min = 1
                    borne_sup = 1000
                    mon_nombre = randint(2,999)   
                    ton_nombre = 0
                    

                    if kijou%2 == 0:
                        joueur = "Joueur 1"
                    else:
                        joueur = "Joueur 2"

                    
                    bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                    bille = pygame.transform.scale(bille, (30, 30))
                    position_bille = [270, 10] 
                    fenetre.blit(bille, position_bille)

                    bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                    bille = pygame.transform.scale(bille, (1000, 200))
                    position_bille = [20, 110] 
                    fenetre.blit(bille, position_bille)

                    bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                    bille = pygame.transform.scale(bille, (60, 60))
                    position_bille = [5, 40] 
                    fenetre.blit(bille, position_bille)

                    police = pygame.font.Font(None, 36)
                    texte = police.render("Points joueur 1 :  " + str(pointj1),True, "black")
                    fenetre.blit(texte, (10, 500))

                    police = pygame.font.Font(None, 36)
                    texte = police.render("Points joueur 2 :  " + str(pointj2),True, "black")
                    fenetre.blit(texte, (10, 550))

                    police = pygame.font.Font(None, 36)
                    texte = police.render(str(nbr_essais_max),True, "black")
                    fenetre.blit(texte, (270, 10))

                    police = pygame.font.Font("./police/Sketchzone.otf", 66)
                    texte = police.render(joueur +" Choisissez un nombre : ",True, "Yellow")
                    fenetre.blit(texte, (10, 70))
                    pygame.display.flip()


                    mon_nombre = randint(1,borne_sup) 
                    while ton_nombre != mon_nombre and nbr_essais <= nbr_essais_max:

                        bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                        bille = pygame.transform.scale(bille, (30, 30))
                        position_bille = [960, 10] 
                        fenetre.blit(bille, position_bille)

                        police = pygame.font.Font(None, 36)
                        texte = police.render(str(nbr_essais),True, "black")
                        fenetre.blit(texte, (960, 10))

                        bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                        bille = pygame.transform.scale(bille, (450, 50))
                        position_bille = [300, 270] 
                        fenetre.blit(bille, position_bille)

                        police = pygame.font.Font(None, 72)
                        texte = police.render((3-len(str(borne_min)))* "  " + str(borne_min) + "<", True, "black")
                        fenetre.blit(texte, (320, 270))
                        police = pygame.font.Font(None, 72)
                        texte = police.render( "<" + str(borne_sup), True, "black")
                        fenetre.blit(texte, (550, 270))
                        pygame.display.flip()

                        ton_nombre = choix_nombre()
                        if ton_nombre=="NULL":
                            return 0

                        bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                        bille = pygame.transform.scale(bille, (450, 90))
                        position_bille = [400, 170] 
                        fenetre.blit(bille, position_bille)

                        
                        if ton_nombre < mon_nombre and borne_min < ton_nombre and borne_sup > ton_nombre:
                            
                            police = pygame.font.Font("./police/Sketchzone.otf", 66)
                            texte = police.render("Plus",True, "green")
                            fenetre.blit(texte, (440, 170))
                            pygame.display.flip()

                            nbr_essais += 1
                            borne_min = ton_nombre
                        elif ton_nombre > mon_nombre and borne_min < ton_nombre and borne_sup > ton_nombre:
                            
                            police = pygame.font.Font("./police/Sketchzone.otf", 66)
                            texte = police.render("Moins",True, "red")
                            fenetre.blit(texte, (420, 170))
                            pygame.display.flip()

                            borne_sup = ton_nombre
                            nbr_essais += 1
                        elif ton_nombre == mon_nombre:
                            kijou += 1
                        
                            bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                            bille = pygame.transform.scale(bille, (1000, 100))
                            position_bille = [10, 70] 
                            fenetre.blit(bille, position_bille)

                            police = pygame.font.Font("./police/Sketchzone.otf", 52)
                            texte = police.render("Bravo ! Vous avez trouvé en "+str(nbr_essais)+" essais",True, "Green")
                            fenetre.blit(texte, (55, 110))

                            police = pygame.font.Font("./police/Sketchzone.otf", 52)
                            texte = police.render("Le nombre était : "+str(mon_nombre),True, "Green")
                            fenetre.blit(texte, (240, 180))
                            pygame.display.flip()

                            bille = pygame.image.load("./image/juste prix/suivant.png").convert_alpha()
                            bille = pygame.transform.scale(bille, (300, 80.7))
                            position_bille = [680, 500] 
                            fenetre.blit(bille, position_bille)

                            bille = pygame.image.load("./image/juste prix/fleche.png").convert_alpha()
                            bille = pygame.transform.scale(bille, (50,34.35))
                            bille = pygame.transform.rotate(bille, 180)
                            position_bille = [5, 40] 
                            fenetre.blit(bille, position_bille)

                            pygame.display.flip()

                            fin = 0
                            while fin == 0:
                                for event in pygame.event.get():
                                    if (event.type == MOUSEBUTTONUP):
                                        x = event.pos[0]
                                        y = event.pos[1]
                                        if x > 680 and x < 977 and y > 500 and y < 579:
                                            fin=1
                                            bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                                            bille = pygame.transform.scale(bille, (300, 82))
                                            position_bille = [680, 500] 
                                            fenetre.blit(bille, position_bille)
                                            pygame.display.flip()
                                        if(x>21 and x<51 and y>50 and y<61) or (x>5 and x<20 and y>41 and y<71):
                                                fin=1
                                                restart=1
                                                end=1

                    
                                    if (event.type == QUIT): 
                                        return 0
                            
                        
                        
                        if nbr_essais>nbr_essais_max and ton_nombre != mon_nombre :
                            if kijou%2 == 0:
                                pointj2 += 1
                            else:
                                pointj1 += 1
                            
                            bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                            bille = pygame.transform.scale(bille, (300, 100))
                            position_bille = [10, 500] 
                            fenetre.blit(bille, position_bille)

                            police = pygame.font.Font(None, 36)
                            texte = police.render("Points joueur 1 :  " + str(pointj1),True, "black")
                            fenetre.blit(texte, (10, 500))

                            police = pygame.font.Font(None, 36)
                            texte = police.render("Points joueur 2 :  " + str(pointj2),True, "black")
                            fenetre.blit(texte, (10, 550))

                            bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                            bille = pygame.transform.scale(bille, (1000, 200))
                            position_bille = [10, 70] 
                            fenetre.blit(bille, position_bille)

                            police = pygame.font.Font("./police/Sketchzone.otf", 62)
                            texte = police.render("Perdu ! Vous n'avez plus d'essai",True, "Red")
                            fenetre.blit(texte, (50, 110))

                            police = pygame.font.Font("./police/Sketchzone.otf", 62)
                            texte = police.render("Le nombre était : "+str(mon_nombre),True, "Red")
                            fenetre.blit(texte, (210, 180))

                            bille = pygame.image.load("./image/juste prix/rejouer.png").convert_alpha()
                            bille = pygame.transform.scale(bille, (300, 80.7))
                            position_bille = [680, 500] 
                            fenetre.blit(bille, position_bille)

                            bille = pygame.image.load("./image/juste prix/fleche.png").convert_alpha()
                            bille = pygame.transform.scale(bille, (50,34.35))
                            bille = pygame.transform.rotate(bille, 180)
                            position_bille = [5, 40] 
                            fenetre.blit(bille, position_bille)

                            pygame.display.flip()

                            fin = 0
                            while fin == 0:
                                for event in pygame.event.get():
                                    if (event.type == MOUSEBUTTONUP):
                                        x = event.pos[0]
                                        y = event.pos[1]
                                        if x > 680 and x < 977 and y > 500 and y < 579:
                                            fin = 1
                                            end=1
                                            bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                                            bille = pygame.transform.scale(bille, (300, 82))
                                            position_bille = [680, 500] 
                                            fenetre.blit(bille, position_bille)
                                            bille = pygame.image.load("./image/juste prix/fond.jpg").convert_alpha()
                                            bille = pygame.transform.scale(bille, (200, 50))
                                            position_bille = [10, 500] 
                                            fenetre.blit(bille, position_bille)
                                            pygame.display.flip()
                                        if(x>21 and x<51 and y>50 and y<61) or (x>5 and x<20 and y>41 and y<71):
                                            fin=1
                                            restart=1
                                            end=1


                                    if (event.type == QUIT): 
                                        return 0
                    


 
    