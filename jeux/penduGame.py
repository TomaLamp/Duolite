from pygame import *
import pygame


def pendu():
    from random import choice


    def place_image(nb_echecs):
        nomFichier = "./image/pendu/pendu_"+str(nb_echecs)+".png"
        bille = pygame.image.load(nomFichier).convert_alpha()
        bille = pygame.transform.scale(bille, (300, 239.682))
        position_bille = [240, 150] 
        fenetre.blit(bille, position_bille)
        pygame.display.flip()

    def printt(mot):
        i=0
        mot_large = ""
        while i<len(mot):  
            mot_large = mot_large + mot[i] + " "
            i+=1
        mot = mot_large

        bille = pygame.image.load("./image/pendu/bande.jpg").convert_alpha()
        position_bille = [0, 70] 
        fenetre.blit(bille, position_bille)
        rectImage = bille.get_rect().width 
        pygame.display.flip()

        police = pygame.font.Font(None, 64)
        texte = police.render(mot ,True,pygame.Color("black"))
        rectTexte = texte.get_rect().width
        fenetre.blit(texte, (rectImage/2-rectTexte/2, 70))
        pygame.display.flip()


    def get_lettre():
        pygame.init()
        lettre = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        end = 0
        while end==0:
            for event in pygame.event.get():
                if (event.type == MOUSEBUTTONUP):
                    x = event.pos[0]
                    y = event.pos[1]
                    if y<30:
                        bille = pygame.image.load("./image/pendu/dejavue.png").convert_alpha()
                        bille = pygame.transform.scale(bille, (30, 30))
                        position_bille = [(lettre.index(lettre[x//30]))*30, 0] 
                        fenetre.blit(bille, position_bille)
                        pygame.display.flip()

                        police = pygame.font.Font(None, 20)
                        texte = police.render(lettre[x//30],True,pygame.Color("black"))
                        fenetre.blit(texte, ((lettre.index(lettre[x//30]))*30+10, 10))
                        pygame.display.flip()

                        return lettre[x//30]

                if event.type == KEYDOWN:
                    if event.key<=122 and event.key>=97:
                        bille = pygame.image.load("./image/pendu/dejavue.png").convert_alpha()
                        bille = pygame.transform.scale(bille, (30, 30))
                        position_bille = [(lettre.index(chr(event.key).upper()))*30, 0] 
                        fenetre.blit(bille, position_bille)
                        pygame.display.flip()

                        police = pygame.font.Font(None, 20)
                        texte = police.render(chr(event.key).upper(),True,pygame.Color("black"))
                        fenetre.blit(texte, ((lettre.index(chr(event.key).upper()))*30+10, 10))
                        pygame.display.flip()

                        return chr(event.key).upper()
                
                if (event.type == QUIT): 
                    return "NULL"

    fichier = open("./annexes/liste.py", "r")
    liste_mots = fichier.readlines()   
    fichier.close()

    pygame.init()
    pygame.font.init()
    fenetre = pygame.display.set_mode((780,400))
    fenetre.fill('red')
    pygame.display.set_caption("Pendu")
    pygame_icon = pygame.image.load('./image/pendu/icon.jpg')
    pygame.display.set_icon(pygame_icon)
    pygame.display.flip()

    end = 0
    while end==0:
        bille = pygame.image.load("./image/pendu/play-chifoumi.png")
        bille = pygame.transform.scale(bille, (500, 337.5))
        position_bille = [150, 30] 
        fenetre.blit(bille, position_bille)
        pygame.display.flip()

        for event in pygame.event.get():

            if (event.type == MOUSEBUTTONUP):
                    x = event.pos[0]
                    y = event.pos[1]
                    if x>150 and x<649 and y>212 and y<366:
                        end=1


            if (event.type == QUIT): 
                return 0



    startj2=0
    while startj2==0:
        fenetre.fill('red')
        end = 0
        while end==0:
            bille = pygame.image.load("./image/pendu/joueur.png")
            bille = pygame.transform.scale(bille, (500, 123.8))
            position_bille = [150, 30] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip()

            bille = pygame.image.load("./image/pendu/joueur2.png")
            bille = pygame.transform.scale(bille, (500, 123.8))
            position_bille = [150, 250] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip()

            for event in pygame.event.get():

                if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]
                        if x>150 and x<649 and y>30 and y<147:
                            end=1
                            nb_joueur = 1
                        elif x>150 and x<649 and y>249 and y<367:
                            end=1
                            nb_joueur = 2


                if (event.type == QUIT): 
                    return 0


        partie = 0
        point = 0
        pointj2 = 0
        kijou = 1
        restart = 1
        while restart==1:
            fenetre.fill('red')
            lettre = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
            
            if nb_joueur == 1:
                mot_choisi = choice(liste_mots).rstrip()
            else:
                end=0
                while end==0:
                    if kijou%2 == 1:
                        joueur = "1"
                        j2 = "2"
                    else:
                        joueur = "2"
                        j2 = "1"
                    fenetre.fill('red')
                    police = pygame.font.Font(None, 42)
                    texte = police.render("Joueur "+ joueur +" ne regardez pas",True,pygame.Color("black"))
                    fenetre.blit(texte, (200, 200))
                    police = pygame.font.Font(None, 42)
                    texte = police.render("Joueur "+ j2 +" vous allez choisir un mot pour l'adversaire",True,pygame.Color("black"))
                    fenetre.blit(texte, (30, 150))
                    bille = pygame.image.load("./image/pendu/suivant.png").convert_alpha()
                    bille = pygame.transform.scale(bille, (200, 47.68))
                    fenetre.blit(bille, (280, 250))
                    pygame.display.flip()

                    for event in pygame.event.get():

                        if (event.type == MOUSEBUTTONUP):
                                x = event.pos[0]
                                y = event.pos[1]
                                if x>280 and x<476 and y>250 and y<296:
                                    end=1


                        if (event.type == QUIT): 
                            return 0

                fenetre.fill('red')
                choix_mot = []
                for i in range(9):
                    mot = choice(liste_mots).rstrip()
                    choix_mot.append(mot)
                    if liste_mots[len(liste_mots)-1] != mot:
                        liste_mots.remove(mot + "\n")
                    else:
                        liste_mots.remove(mot)
                

                police = pygame.font.Font(None, 42)
                police.underline = True
                texte = police.render("Choisissez un mot pour l'adversaire",True,pygame.Color("black"))
                fenetre.blit(texte, (150, 10))
                pygame.display.flip()

                c = 0
                for i in range(3):
                    for j in range(3):
                        bille = pygame.image.load("./image/pendu/mots.png").convert_alpha()
                        bille = pygame.transform.scale(bille, (180, 42.85))
                        rectImage = bille.get_rect().width 
                        position_bille = [i*180 + 60*(i+1), j*100 + 105] 
                        fenetre.blit(bille, position_bille)
                        pygame.display.flip()

                        police = pygame.font.Font(None, 32)
                        texte = police.render(choix_mot[c],True,pygame.Color("black"))
                        rectText = texte.get_rect().width 
                        fenetre.blit(texte, ((i*180 + 60*(i+1))+rectImage/2 - rectText/2, (j*100 + 105)+10))
                        pygame.display.flip()
                        c += 1
                
                end=0
                while end==0:
                    for event in pygame.event.get():

                        if (event.type == MOUSEBUTTONUP):
                            x = event.pos[0]
                            y = event.pos[1]
                            if x>63 and x<236 and y>105 and y<144:
                                end=1
                                mot_choisi = choix_mot[0]
                            elif x>303 and x<477 and y>105 and y<144:
                                end=1
                                mot_choisi = choix_mot[3]
                            elif x>543 and x<717 and y>105 and y<144:
                                end=1
                                mot_choisi = choix_mot[6]
                            elif x>63 and x<236 and y>204 and y<242:
                                end=1
                                mot_choisi = choix_mot[1]
                            elif x>303 and x<477 and y>204 and y<242:
                                end=1
                                mot_choisi = choix_mot[4]
                            elif x>543 and x<717 and y>204 and y<242:
                                end=1
                                mot_choisi = choix_mot[7]
                            elif x>63 and x<236 and y>304 and y<341:
                                end=1
                                mot_choisi = choix_mot[2]
                            elif x>303 and x<477 and y>304 and y<341:
                                end=1
                                mot_choisi = choix_mot[5]
                            elif x>543 and x<717 and y>304 and y<341:
                                end=1
                                mot_choisi = choix_mot[8]
                            

                        if (event.type == QUIT): 
                            return 0

            fenetre.fill('red')            
            for i in range(26):
                bille = pygame.image.load("./image/pendu/carres.jpg").convert_alpha()
                bille = pygame.transform.scale(bille, (30, 30))
                position_bille = [i*30, 0] 
                fenetre.blit(bille, position_bille)
                pygame.display.flip()

                police = pygame.font.Font(None, 20)
                texte = police.render(lettre[i],True,pygame.Color("black"))
                fenetre.blit(texte, (i*30+10, 10))
                pygame.display.flip()

            police = pygame.font.Font(None, 32)
            police.underline = True
            texte = police.render("Lettres fausses :",True,pygame.Color("black"))
            fenetre.blit(texte, (10, 150))
            pygame.display.flip()

            police = pygame.font.Font(None, 32)
            police.underline = True
            texte = police.render("Lettres bonnes :",True,pygame.Color("black"))
            fenetre.blit(texte, (605, 150))
            pygame.display.flip()


            if nb_joueur == 2:
                police = pygame.font.Font(None, 28)
                texte = police.render("Joueur 2 : " + str(pointj2),True,pygame.Color("black"))
                fenetre.blit(texte, (625, 375))
                pygame.display.flip()
                txt_point = "Joueur 1 : "
            else:
                police = pygame.font.Font(None, 28)
                texte = police.render("Partie jouée : " + str(partie),True,pygame.Color("black"))
                fenetre.blit(texte, (625, 375))
                pygame.display.flip()
                txt_point = "Mes points : "

            police = pygame.font.Font(None, 28)
            texte = police.render(txt_point + str(point),True,pygame.Color("black"))
            fenetre.blit(texte, (625, 350))
            pygame.display.flip()
            
            nb_echecs = 0
            partie_en_cours = True
            mot_choisi = mot_choisi.upper()
            mot_partiel = "-" * len(mot_choisi)
            lettre_deja_choisie = []
            lettre_bonne = []
            lettre_fausse = []

            printt(mot_partiel)
            place_image(nb_echecs)
            while nb_echecs < 10:
                nouveau_mot_partiel = ""
                fin = 0
                while fin==0:
                    lettre_choisi = get_lettre()
                    if lettre_choisi == "NULL":
                        return 0
                    if lettre_choisi not in lettre_deja_choisie:
                        fin = 1
                for i in range(len(mot_choisi)):
                    if lettre_choisi == mot_choisi[i]:
                        nouveau_mot_partiel = nouveau_mot_partiel + lettre_choisi
                        if lettre_choisi not in lettre_bonne:
                            lettre_bonne.append(lettre_choisi)
                    else:
                        nouveau_mot_partiel = nouveau_mot_partiel + mot_partiel[i]
                if mot_partiel == nouveau_mot_partiel:
                    nb_echecs+=1
                    place_image(nb_echecs)
                    lettre_fausse.append(lettre_choisi)
                mot_partiel = nouveau_mot_partiel
                lettre_deja_choisie.append(lettre_choisi)
                printt(mot_partiel)

                for i in range(len(lettre_fausse)):
                    if i>4:
                        y = 30
                        x = 175
                    else:
                        y = 0
                        x = 0
                    police = pygame.font.Font(None, 32)
                    texte = police.render(lettre_fausse[i],True,pygame.Color("black"))
                    fenetre.blit(texte, ((i*35+10)-x, 180+y))
                    pygame.display.flip()

                for i in range(len(lettre_bonne)):
                    if i>4:
                        y = 30
                        x = 175
                    else:
                        y = 0
                        x = 0
                    police = pygame.font.Font(None, 32)
                    texte = police.render(lettre_bonne[i],True,pygame.Color("black"))
                    fenetre.blit(texte, ((i*35+605)-x, 180+y))
                    pygame.display.flip()

                if mot_partiel == mot_choisi:
                    break
                                   

            if nb_echecs == 10:
                printt(mot_choisi)
                place_image(nb_echecs)
            else:
                bille = pygame.image.load("./image/pendu/bravo.png").convert_alpha()
                bille = pygame.transform.scale(bille, (300, 239.682))
                position_bille = [240, 150] 
                fenetre.blit(bille, position_bille)
                pygame.display.flip()

            if len(lettre_fausse) != 10:
                if kijou%2 == 1:
                    if len(lettre_fausse) == 0:
                        point += 15
                    else:
                        point += 11 - len(lettre_fausse)
                else:
                    if len(lettre_fausse) == 0:
                        pointj2 += 15
                    else:
                        pointj2 += 11 - len(lettre_fausse)
                


            if nb_joueur == 1:
                x = 740
            else:
                x = 720
                
            if kijou%2 == 1:
                y = 350
                pt = point
            else:
                y=375
                pt = pointj2

            
            bille = pygame.image.load("./image/pendu/cache.jpg").convert_alpha()
            bille = pygame.transform.scale(bille, (30, 20))
            position_bille = [x, y] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip() 

            police = pygame.font.Font(None, 28)
            texte = police.render(str(pt),True,pygame.Color("black"))
            fenetre.blit(texte, (x+5, y))
            pygame.display.flip()

            if nb_joueur == 2: 
                kijou += 1
                partie += 0.5
            else:
                partie += 1

            bille = pygame.image.load("./image/pendu/rejouer.png").convert_alpha()
            bille = pygame.transform.scale(bille, (200, 46.58))
            position_bille = [10, 350] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip() 

            bille = pygame.image.load("./image/pendu/fleche.png").convert_alpha()
            bille = pygame.transform.scale(bille, (50,34.35))
            bille = pygame.transform.rotate(bille, 180)
            position_bille = [5, 40] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip() 
            end = 0
            while end==0:
                if nb_joueur == 2:
                    if partie == 5:
                        pygame.time.wait(1000)
                        fenetre.fill('red')
                        end=0
                        while end==0:
                            if point>pointj2:
                                police = pygame.font.Font(None, 42)
                                texte = police.render("Victoire du joueur 1",True,"green")
                                fenetre.blit(texte, (240, 200))
                            elif point<pointj2:
                                police = pygame.font.Font(None, 42)
                                texte = police.render("Victoire du joueur 2",True,"green")
                                fenetre.blit(texte, (240, 200)) 
                            else:
                                police = pygame.font.Font(None, 62)
                                texte = police.render("Egalité",True,"#9C0000")
                                fenetre.blit(texte, (310, 195))
                                
                            
                            police = pygame.font.Font(None, 42)
                            texte = police.render("Joueur 1 : " +str(point)+" points / Joueur 2 : "+str(pointj2)+ " points",True,pygame.Color("black"))
                            fenetre.blit(texte, (100, 150))
                            bille = pygame.image.load("./image/pendu/suivant.png").convert_alpha()
                            bille = pygame.transform.scale(bille, (200, 47.68))
                            fenetre.blit(bille, (280, 250))
                            pygame.display.flip()

                            for event in pygame.event.get():

                                if (event.type == MOUSEBUTTONUP):
                                        x = event.pos[0]
                                        y = event.pos[1]
                                        if x>280 and x<476 and y>250 and y<296:
                                            end=1


                                if (event.type == QUIT): 
                                    return 0
                        restart=0
                for event in pygame.event.get():

                    if (event.type == MOUSEBUTTONUP):
                            x = event.pos[0]
                            y = event.pos[1]
                            if x>10 and x<206 and y>350 and y<393:
                                end=1
                            if(x>21 and x<51 and y>50 and y<61) or (x>5 and x<20 and y>41 and y<71):
                                end=1
                                restart=0
                            

                    if (event.type == QUIT): 
                        return 0 

    


    end = 0
    while end==0:
            
        for event in pygame.event.get():
            if (event.type == QUIT): 
                return 0
