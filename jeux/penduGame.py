from pygame import *
import pygame
from module.pygameCore import *


def pendu():
    from random import choice

    # --- Nouvelle taille ---
    NEW_WIDTH = 1000
    NEW_HEIGHT = 600


    # --- Ancienne taille (base du jeu) ---
    BASE_WIDTH = 780
    BASE_HEIGHT = 400


    # Facteurs d'échelle
    scale_x = NEW_WIDTH / BASE_WIDTH
    scale_y = NEW_HEIGHT / BASE_HEIGHT


    def place_image(nb_echecs):
        nomFichier = "./image/pendu/pendu_"+str(nb_echecs)+".png"
        printImage(nomFichier, (300*scale_x, 239.682*scale_y), (240*scale_x, 150*scale_y), fenetre)
        
        pygame.display.flip()

    def printt(mot):
        i=0
        mot_large = ""
        while i<len(mot):  
            mot_large = mot_large + mot[i] + " "
            i+=1
        mot = mot_large

        printImage("./image/pendu/bande.jpg", (1000, 60), (0*scale_x, 70*scale_y), fenetre)
        printText(mot, int(64*scale_y), "black", (500, 70*scale_y), fenetre, Alignement="Center")
        
        pygame.display.flip()


    def get_lettre():
        lettre = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        end = 0
        while end==0:
            for event in pygame.event.get():
                if (event.type == MOUSEBUTTONUP):
                    x = event.pos[0]
                    y = event.pos[1]
                    if y < 30*scale_y:
                        index = int(x // (30*scale_x))
                        printImage("./image/pendu/dejavue.png", (30*scale_x, 30*scale_y), ((lettre.index(lettre[index]))*30*scale_x, 0), fenetre)
                        printText(lettre[index], int(20*scale_y), "black", ((lettre.index(lettre[index]))*30*scale_x+10*scale_x, 10*scale_y), fenetre)
                        pygame.display.flip()

                        return lettre[index]

                if event.type == KEYDOWN:
                    if event.key<=122 and event.key>=97:
                        printImage("./image/pendu/dejavue.png", (30*scale_x, 30*scale_y), ((lettre.index(chr(event.key).upper()))*30*scale_x, 0), fenetre)
                        printText(chr(event.key).upper(), int(20*scale_y), "black", ((lettre.index(chr(event.key).upper()))*30*scale_x+10*scale_x, 10*scale_y), fenetre)
                        pygame.display.flip()

                        return chr(event.key).upper()
                
                if (event.type == QUIT): 
                    return "NULL"

    fichier = open("./annexes/liste.py", "r")
    liste_mots = fichier.readlines()   
    fichier.close()

    fenetre = initScreen((NEW_WIDTH,NEW_HEIGHT), "Pendu", 'red', './image/pendu/icon.jpg')

    end = 0
    while end==0:
        printImage("./image/pendu/play-chifoumi.png", (500*scale_x, 337.5*scale_y), (150*scale_x, 30*scale_y), fenetre)
        pygame.display.flip()

        for event in pygame.event.get():
            if (event.type == MOUSEBUTTONUP):
                x = event.pos[0]
                y = event.pos[1]
                if x>150*scale_x and x<649*scale_x and y>212*scale_y and y<366*scale_y:
                    end=1

            if (event.type == QUIT): 
                    return 0



    startj2=0
    while startj2==0:
        fenetre.fill('red')
        end = 0
        while end==0:
            printImage("./image/pendu/joueur.png", (500*scale_x, 123.8*scale_y), (150*scale_x, 30*scale_y), fenetre)
            printImage("./image/pendu/joueur2.png", (500*scale_x, 123.8*scale_y), (150*scale_x, 250*scale_y), fenetre)
            pygame.display.flip()

            for event in pygame.event.get():

                if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]
                        if x>150*scale_x and x<649*scale_x and y>30*scale_y and y<147*scale_y:
                            end=1
                            nb_joueur = 1
                        elif x>150*scale_x and x<649*scale_x and y>249*scale_y and y<367*scale_y:
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

                    printText("Joueur "+ joueur +" ne regardez pas", int(42*scale_y), "black", (500, 70*scale_y), fenetre, Alignement="Center")
                    printText("Joueur "+ j2 +" vous allez choisir un mot pour l'adversaire", int(55), "black", (500, 150*scale_y), fenetre, Alignement="Center")
                    
                    printImage("./image/pendu/suivant.png", (200*scale_x, 47.68*scale_y), (280*scale_x, 250*scale_y), fenetre)
                    pygame.display.flip()

                    for event in pygame.event.get():

                        if (event.type == MOUSEBUTTONUP):
                                x = event.pos[0]
                                y = event.pos[1]
                                if x>280*scale_x and x<476*scale_x and y>250*scale_y and y<296*scale_y:
                                    end = 1

                        if (event.type == KEYDOWN):
                            if event.key==K_RETURN:
                                end = 1

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
                
                printText("Choisissez un mot pour l'adversaire", int(42*scale_y), "black", (500, 10*scale_y), fenetre, Alignement="Center")

                c = 0
                for i in range(3):
                    for j in range(3):
                        rectImage = printImage("./image/pendu/mots.png", (180*scale_x, 42.85*scale_y), ((i*180 + 60*(i+1))*scale_x, (j*100 + 105)*scale_y), fenetre).width
                        printText(choix_mot[c], int(32*scale_y), "black", ((i*180 + 60*(i+1))*scale_x + rectImage/2, ((j*100 + 105)+10)*scale_y), fenetre, Alignement="Center")
                        c += 1
                pygame.display.flip()

                end=0
                while end==0:
                    for event in pygame.event.get():

                        if (event.type == MOUSEBUTTONUP):
                            x = event.pos[0]
                            y = event.pos[1]
                            if x>63*scale_x and x<236*scale_x and y>105*scale_y and y<144*scale_y:
                                end=1
                                mot_choisi = choix_mot[0]
                            elif x>303*scale_x and x<477*scale_x and y>105*scale_y and y<144*scale_y:
                                end=1
                                mot_choisi = choix_mot[3]
                            elif x>543*scale_x and x<717*scale_x and y>105*scale_y and y<144*scale_y:
                                end=1
                                mot_choisi = choix_mot[6]
                            elif x>63*scale_x and x<236*scale_x and y>204*scale_y and y<242*scale_y:
                                end=1
                                mot_choisi = choix_mot[1]
                            elif x>303*scale_x and x<477*scale_x and y>204*scale_y and y<242*scale_y:
                                end=1
                                mot_choisi = choix_mot[4]
                            elif x>543*scale_x and x<717*scale_x and y>204*scale_y and y<242*scale_y:
                                end=1
                                mot_choisi = choix_mot[7]
                            elif x>63*scale_x and x<236*scale_x and y>304*scale_y and y<341*scale_y:
                                end=1
                                mot_choisi = choix_mot[2]
                            elif x>303*scale_x and x<477*scale_x and y>304*scale_y and y<341*scale_y:
                                end=1
                                mot_choisi = choix_mot[5]
                            elif x>543*scale_x and x<717*scale_x and y>304*scale_y and y<341*scale_y:
                                end=1
                                mot_choisi = choix_mot[8]
                            

                        if (event.type == QUIT): 
                            return 0

            fenetre.fill('red')            
            for i in range(26):
                printImage("./image/pendu/carres.jpg", (30*scale_x, 30*scale_y), (i*30*scale_x, 0), fenetre)
                printText(lettre[i], int(20*scale_y), "black", (i*30*scale_x+10*scale_x, 10*scale_y), fenetre)
            
            pygame.display.flip()

            printText("Lettres fausses :", int(32*scale_y), "black", (10*scale_x, 150*scale_y), fenetre, underline=True)
            printText("Lettres bonnes :", int(32*scale_y), "black", (770*scale_x, 150*scale_y), fenetre, underline=True, Alignement="Right")
            
            pygame.display.flip()


            if nb_joueur == 2:
                printText("Joueur 2 :  " + str(pointj2), int(28*scale_y), "black", (760*scale_x, 375*scale_y), fenetre, Alignement="Right")
                txt_point = "Joueur 1 :  "
            else:
                printText("Partie jouée :  " + str(partie), int(28*scale_y), "black", (760*scale_x, 375*scale_y), fenetre, Alignement="Right")
                txt_point = "Mes points :  "

            printText(txt_point + str(point), int(28*scale_y), "black", (760*scale_x, 350*scale_y), fenetre, Alignement="Right")
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

                    printText(lettre_fausse[i], int(32*scale_y), "black", (((i*35+10)-x)*scale_x, (180+y)*scale_y), fenetre)

                for i in range(len(lettre_bonne)):
                    if i>4:
                        y = 30
                        x = 175
                    else:
                        y = 0
                        x = 0
                    printText(lettre_bonne[i], int(32*scale_y), "black", (((i*35+605)-x)*scale_x, (180+y)*scale_y), fenetre)
                    police = pygame.font.Font(None, int(32*scale_y))
                    texte = police.render(lettre_bonne[i],True,pygame.Color("black"))
                    fenetre.blit(texte, (((i*35+605)-x)*scale_x, (180+y)*scale_y))
                
                pygame.display.flip()

                if mot_partiel == mot_choisi:
                    break
                                   

            if nb_echecs == 10:
                printt(mot_choisi)
                place_image(nb_echecs)
            else:
                printImage("./image/pendu/bravo.png", (300*scale_x, 239.682*scale_y), (240*scale_x, 150*scale_y), fenetre)
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
                x = 735*scale_x
            else:
                x = 733.5*scale_x
            
            if kijou%2 == 1:
                y = 350*scale_y
                pt = point
            else:
                y=375*scale_y
                pt = pointj2

            
            printImage("./image/pendu/cache.jpg", (30*scale_x, 20*scale_y), (x, y), fenetre) 
            printText(str(pt), int(28*scale_y), "black", (x+10, y), fenetre)

            if nb_joueur == 2: 
                kijou += 1
                partie += 0.5
            else:
                partie += 1

            printImage("./image/pendu/rejouer.png", (200*scale_x, 46.58*scale_y), (10*scale_x, 350*scale_y), fenetre)
            printImage("./image/pendu/fleche.png", (50*scale_x,34.35*scale_y), (5*scale_x, 40*scale_y), fenetre, rotation=180)
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
                                printText("Victoire du joueur 1", int(42*scale_y), "green", (500, 200*scale_y), fenetre, Alignement="Center")
                            elif point<pointj2:
                                printText("Victoire du joueur 2", int(42*scale_y), "green", (500, 200*scale_y), fenetre, Alignement="Center")
                            else:
                                printText("Egalité", int(62*scale_y), "#9C0000", (500, 195*scale_y), fenetre, Alignement="Center")
                                
                            
                            printText("joueur 1 : " +str(point)+" points / Joueur 2 : "+str(pointj2)+ " points", int(42*scale_y), "black", (500, 150*scale_y), fenetre, Alignement="Center")
                            printImage("./image/pendu/suivant.png", (200*scale_x, 47.68*scale_y), (500, 250*scale_y), fenetre, Alignement="Center")
                            pygame.display.flip()

                            for event in pygame.event.get():

                                if (event.type == MOUSEBUTTONUP):
                                        x = event.pos[0]
                                        y = event.pos[1]
                                        if x>280*scale_x and x<476*scale_x and y>250*scale_y and y<296*scale_y:
                                            end=1

                                if (event.type == KEYDOWN):
                                    if event.key==K_RETURN:
                                        end = 1

                                if (event.type == QUIT): 
                                    return 0
                        restart=0

                for event in pygame.event.get():

                    if (event.type == MOUSEBUTTONUP):
                            x = event.pos[0]
                            y = event.pos[1]
                            if x>10*scale_x and x<206*scale_x and y>350*scale_y and y<393*scale_y:
                                end=1
                            if(x>21*scale_x and x<51*scale_x and y>50*scale_y and y<61*scale_y) or (x>5*scale_x and x<20*scale_x and y>41*scale_y and y<71*scale_y):
                                end=1
                                restart=0

                    if (event.type == KEYDOWN):
                            if event.key==K_RETURN:
                                end = 1      

                    if (event.type == QUIT): 
                        return 0 

    


    end = 0
    while end==0:
            
        for event in pygame.event.get():
            if (event.type == QUIT): 
                return 0

if __name__ == "__main__":
    pendu()