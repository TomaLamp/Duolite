from pygame import *
import pygame
from random import choice
from module.pygameCore import *


def motus():

    def get_lettre():
        lettre = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "<", ">"]
        end = 0
        while end==0:
            for event in pygame.event.get():
                if (event.type == MOUSEBUTTONUP):
                    x = event.pos[0]
                    y = event.pos[1]
                    if y<30:
                        return lettre[round(x//35.71)]

                if event.type == KEYDOWN:
                    if event.key<=122 and event.key>=97:
                        return chr(event.key).upper()
                    elif event.key==8:
                        return("<")
                    elif event.key==13:
                        return(">")
                    
                if (event.type == QUIT): 
                    return 0


    # %% main

    fenetre = initScreen((1000,600), "motus", "#4682B4", "./image/motus/icon.png")

    printImage("./image/motus/play.png", (700, 350.315), [150,110], fenetre)
    pygame.display.flip()
    
    nomj1, nomj2 = get_nom()

    fin = 0
    while fin == 0:
        for event in pygame.event.get():
            if (event.type == MOUSEBUTTONUP):
                x = event.pos[0]
                y = event.pos[1]
                if x > 150 and x < 850 and y > 110 and y < 461:
                    fin = 1 
                        
            if (event.type == KEYDOWN) or (event.type == QUIT): 
                return 0

    fenetre.fill("#4682B4")
    fichier = open("./annexes/liste.py", "r")
    liste_mots = fichier.readlines()   
    fichier.close()

    fichier = open("./annexes/dico.txt", "r")
    dico = fichier.readlines()   
    fichier.close()


    restart = 0
    while restart == 0:
        fenetre.fill("#4682B4")
        end = 0
        while end==0:
            printImage("./image/motus/1joueur.png", (750, 185.7), [150, 65], fenetre)
            pygame.display.flip()

            printImage("./image/motus/2joueur.png", (750, 185.7), [150, 350], fenetre)
            pygame.display.flip()

            for event in pygame.event.get():

                if (event.type == MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]
                        if x>150 and x<900 and y>65 and y<250.7:
                            end=1
                            nb_joueur = 1
                        elif x>150 and x<900 and y>350 and y<535.7:
                            end=1
                            nb_joueur = 2


                if (event.type == QUIT): 
                    return 0


        printImage("./image/motus/bleu.png", (1000, 600), [0, 0], fenetre)
        pygame.display.flip()


        if nb_joueur==1:

            points = 0
            partie = 0
            lettre = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "<", ">"]
            fond = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

            printText("mes points :", 32, "black", (10, 200), fenetre, underline=True)

            printText("parties jouée :", 32, "black", (835, 200), fenetre, underline=True)


            end=0
            while end==0:
                printImage("./image/motus/bleu.png", (60, 60), [0,40], fenetre)

                mot_choisi = choice(liste_mots).rstrip().upper()
                while len(mot_choisi)!=4 and len(mot_choisi)!=5 and len(mot_choisi)!=6 and len(mot_choisi)!=7:
                    mot_choisi = choice(liste_mots).rstrip().upper()

                #print(mot_choisi)
                mot_partiel = [mot_choisi[0]]
                for i in range(1, len(mot_choisi)):
                    mot_partiel.append(".")

                printImage("./image/motus/bleu.png", (650, 520), [170, 70], fenetre)

                printImage("./image/motus/bleu.png", (180, 150), [10, 500], fenetre)

                printImage("./image/motus/bleu.png", (200, 100), [825, 500], fenetre)

                
                taille = [0, 0, 0, 0, 320, 290, 250, 210]
                for i in range(len(mot_choisi)):
                    printImage("./image/motus/grille.png", (82, 505), [i*84+taille[len(mot_choisi)], 70], fenetre)

                    printText(mot_partiel[i], 40, "black", (i*84+taille[len(mot_choisi)]+30+2*i, 100), fenetre)
                    pygame.display.flip()

                printImage("./image/motus/bleu.png", (30, 30), [15, 245], fenetre)

                printImage("./image/motus/bleu.png", (30, 30), [960, 245], fenetre)

                printText(str(points), 32, "black", (20, 250), fenetre)

                printText(str(partie), 32, "black", (965, 250), fenetre)
                pygame.display.flip()


                fond = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
                tour = 0
                mot_final = []
                for i in range(len(mot_choisi)):
                    mot_final.append(mot_choisi[i])

                while tour<6:

                    
                    for i in range(28):
                        if fond[i] == 0:
                            printImage("./image/motus/carresB.jpg", (35.71, 35.71), [i*35.71, 0], fenetre)
                        elif fond[i] == 1 :
                            printImage("./image/motus/carresR.jpg", (35.71, 35.71), [i*35.71, 0], fenetre)
                        elif fond[i] == 2:
                            printImage("./image/motus/carresJ.png", (35.71, 35.71), [i*35.71, 0], fenetre)
                        else:
                            printImage("./image/motus/carresP.jpg", (35.71, 35.71), [i*35.71, 0], fenetre)
                    

                        printText(lettre[i], 25, "black", (i*35.8+10, 10), fenetre)
                        pygame.display.flip()

                    mot_point = list(mot_partiel)
                    mot_verif = mot_choisi
                    mot_test = mot_partiel[0]
                    verif = []
                    nbr_lettre = 1
                    fin=0
                    for i in range(len(mot_choisi)-1):
                        verif.append(0)
                    

                    taille = [0, 0, 0, 0, 320, 290, 250, 210]
                    for i in range(len(mot_choisi)):

                        printText(mot_partiel[i], 40, "black", (i*84+taille[len(mot_choisi)]+30+2*i, 100+tour*85), fenetre)
                        pygame.display.flip()

                    while fin==0:

                        lettre_choisis = get_lettre()
                        if lettre_choisis==0:
                            return 0
                        if lettre_choisis == "<":
                            if nbr_lettre>1:
                                nbr_lettre -= 1
                                mot_partiel[nbr_lettre] = "."
                                mot_test = mot_partiel[0:nbr_lettre] 

                            for i in range(len(mot_choisi)):
                                printImage("./image/motus/bleu.png", (60, 60), [i*84+taille[len(mot_choisi)]+12, 80+tour*85], fenetre)

                                printText(mot_partiel[i], 40, "black", (i*84+taille[len(mot_choisi)]+30+1.5*i, 100+tour*85), fenetre)
                                pygame.display.flip()
                        
                        
                        elif lettre_choisis == ">":
                            mot_dico = ''
                            for i in range(len(mot_test)):
                                mot_dico = mot_dico + mot_test[i]
                            if len(mot_test)==len(mot_choisi) and (mot_dico.upper()+'\n') in dico:
                                j = 0
                                fin = 1
                                for i in range(len(mot_choisi)-1):
                                    if mot_test[i+1] == mot_choisi[i+1]:
                                        verif[i] = 2
                                        n = mot_verif.index(mot_test[i+1])+1
                                        mot_verif2 = mot_verif
                                        mot_verif = ''
                                        for k in range(len(mot_verif2)):
                                            if k+1!=n:
                                                mot_verif += mot_verif2[k]
                                        mot_partiel = list(mot_point)
                                        mot_partiel[i+1] = mot_test[i+1]
                                        mot_point = list(mot_partiel)
                                for i in range(len(mot_choisi)-1):
                                    if verif[i]!=2:
                                        if mot_test[i+1] in mot_verif[1:]:
                                            verif[i] = 1
                                            n = mot_verif.index(mot_test[i+1])+1
                                            mot_verif2 = mot_verif
                                            mot_verif = ''
                                            for k in range(len(mot_verif2)):
                                                if k+1!=n:
                                                    mot_verif += mot_verif2[k]
                                for i in range(len(verif)):
                                    if verif[i]==0 and fond[lettre.index(mot_test[i+1])]==0:
                                        fond[lettre.index(mot_test[i+1])] = 3
                                    elif verif[i]==1 and fond[lettre.index(mot_test[i+1])]!=1:
                                        fond[lettre.index(mot_test[i+1])] = 2
                                    elif verif[i]==2:
                                        fond[lettre.index(mot_test[i+1])] = 1
                                if mot_test == mot_partiel:
                                    mot_partiel = mot_point

                                for i in range(len(verif)):
                                    if verif[i]==2:
                                        printImage("./image/motus/rouge.jpg", (60, 60), [(i+1)*84+taille[len(mot_choisi)]+12, 80+tour*85], fenetre)

                                        printText(mot_test[i+1], 40, "black", ((i+1)*84+taille[len(mot_choisi)]+30+i, 100+tour*85), fenetre)
                                        pygame.display.flip()

                                    elif verif[i] == 1:
                                        printImage("./image/motus/cerclejaune.png", (60, 60), [(i+1)*84+taille[len(mot_choisi)]+12, 80+tour*85], fenetre)

                                        printText(mot_test[i+1], 40, "black", ((i+1)*84+taille[len(mot_choisi)]+30+i, 100+tour*85), fenetre)
                                        pygame.display.flip()
                                tour+=1

                                if mot_test == mot_final:
                                    points+=7-tour
                                    tour=10
                                    
                                    printText('Bravo', 40, "green", (50,500), fenetre)
                                    pygame.display.flip()
                            
                        else:
                            if len(mot_test)<len(mot_choisi):
                                mot_partiel[nbr_lettre] = lettre_choisis
                                nbr_lettre += 1
                                mot_test = mot_partiel[0:nbr_lettre] 

                                for i in range(len(mot_choisi)):
                                    printImage("./image/motus/bleu.png", (60, 60), [i*84+taille[len(mot_choisi)]+12, 80+tour*85], fenetre)

                                    printText(str(mot_partiel[i]), 40, "black", (i*84+taille[len(mot_choisi)]+30+i, 100+tour*85), fenetre)
                                    pygame.display.flip()

                        for event in pygame.event.get():
                            if (event.type == QUIT): 
                                return 0


                partie+=1
                if tour!=10:
                    printText('Perdu', 40, "red", (50,500), fenetre)

                    printText('le mot etait ' + mot_choisi.lower(), 30, "red", (10,530), fenetre)

                    pygame.display.flip()

                
                printImage("./image/motus/suivant.png", (150, 35.7585), [830, 530], fenetre)

                printImage("./image/juste prix/fleche.png", (50,34.35), [5, 40], fenetre, rotation=180)

                                
                pygame.display.flip()

                
                fin=0
                while fin==0:
                    for event in pygame.event.get():
                        if (event.type == MOUSEBUTTONUP):
                            x = event.pos[0]
                            y = event.pos[1]
                            if x>830 and x<980 and y>530 and y<564:
                                fin=1
                            if(x>21 and x<51 and y>50 and y<61) or (x>5 and x<20 and y>41 and y<71):
                                fin=1
                                end=1

                        if (event.type == QUIT): 
                            return 0


        kijou=0
        taille_mot = 0
        points1 = 0
        points2 = 0
        etape = 0
        if nb_joueur==2:


            start=0
            while start==0:

                fenetre.fill("#4682B4")
                end=0
                while end==0:
                    if kijou%2 == 0:
                        joueur = nomj1
                        j2 = nomj2
                    else:
                        joueur = nomj2
                        j2 = nomj1
                    printText(joueur +" ne regardez pas", 55, "black", (500, 200), fenetre, Alignement="Center")
                    printText(j2 +" vous allez choisir un mot pour l'adversaire", 32, "black", (500, 150), fenetre, Alignement="Center")
                    printImage("./image/motus/suivant.png", (600, 143.04), (500, 350), fenetre, Alignement="Center")
                    pygame.display.flip()

                    for event in pygame.event.get():

                        if (event.type == MOUSEBUTTONUP):
                                x = event.pos[0]
                                y = event.pos[1]
                                if x>200 and x<800 and y>350 and y<493.04:
                                    end=1


                        if (event.type == QUIT): 
                            return 0

                choix_mot = []
                for i in range(15):
                    mot = choice(liste_mots).rstrip()
                    if taille_mot==0:
                        while len(mot)!=4 and len(mot)!=5 and len(mot)!=6 and len(mot)!=7:
                            mot = choice(liste_mots).rstrip()
                    else:
                        while len(mot)!=taille_mot:
                            mot = choice(liste_mots).rstrip()
                    choix_mot.append(mot)
                    if liste_mots[len(liste_mots)-1] != mot:
                        liste_mots.remove(mot + "\n")
                    else:
                        liste_mots.remove(mot)

                
                fenetre.fill("#4682B4")
                printText("Choisissez un mot pour l'adversaire", 60, "black", (150, 10), fenetre, underline=True)
                pygame.display.flip()

                c = 0
                for i in range(3):
                    for j in range(5):
                        rect = printImage("./image/motus/mots.jpg", (250, 42.85), (i*250 + 60*(i+1), j*100 + 105), fenetre).width

                        printText(choix_mot[c], 32, "black", ((i*250 + 60*(i+1))+rect/2, (j*100 + 105)+10), fenetre, Alignement="Center")
                        pygame.display.flip()
                        c += 1
                            
                end=0
                while end==0:
                    for event in pygame.event.get():

                        if (event.type == MOUSEBUTTONUP):
                            x = event.pos[0]
                            y = event.pos[1]
                            if x>60 and x<310 and y>105 and y<144:
                                end=1
                                mot_choisi = choix_mot[0]
                            elif x>370 and x<620 and y>105 and y<144:
                                end=1
                                mot_choisi = choix_mot[5]
                            elif x>680 and x<930 and y>105 and y<144:
                                end=1
                                mot_choisi = choix_mot[10]
                            elif x>60 and x<310 and y>204 and y<242:
                                end=1
                                mot_choisi = choix_mot[1]
                            elif x>370 and x<620 and y>204 and y<242:
                                end=1
                                mot_choisi = choix_mot[6]
                            elif x>680 and x<930 and y>204 and y<242:
                                end=1
                                mot_choisi = choix_mot[11]
                            elif x>60 and x<310 and y>304 and y<341:
                                end=1
                                mot_choisi = choix_mot[2]
                            elif x>370 and x<620 and y>304 and y<341:
                                end=1
                                mot_choisi = choix_mot[7]
                            elif x>680 and x<930 and y>304 and y<341:
                                end=1
                                mot_choisi = choix_mot[12]
                            elif x>60 and x<310 and y>405 and y<442:
                                end=1
                                mot_choisi = choix_mot[3]
                            elif x>370 and x<620 and y>405 and y<442:
                                end=1
                                mot_choisi = choix_mot[8]
                            elif x>680 and x<930 and y>405 and y<442:
                                end=1
                                mot_choisi = choix_mot[13]
                            elif x>60 and x<310 and y>502 and y<544:
                                end=1
                                mot_choisi = choix_mot[4]
                            elif x>370 and x<620 and y>502 and y<544:
                                end=1
                                mot_choisi = choix_mot[9]
                            elif x>680 and x<930 and y>502 and y<544:
                                end=1
                                mot_choisi = choix_mot[14]
                                        

                        if (event.type == QUIT): 
                            return 0


                fenetre.fill("#4682B4")
                lettre = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "<", ">"]
                fond = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

                printText(nomj1+" :", 32, "black", (10, 200), fenetre, underline=True)

                printText(nomj2+" :", 32, "black", (990, 200), fenetre, underline=True, Alignement="Right")


                end=0
                while end==0:

                    mot_choisi = mot_choisi.upper()

                    #print(mot_choisi)
                    mot_partiel = [mot_choisi[0]]
                    for i in range(1, len(mot_choisi)):
                        mot_partiel.append(".")

                    printImage("./image/motus/bleu.png", (650, 520), [170, 70], fenetre)

                    printImage("./image/motus/bleu.png", (180, 150), [10, 500], fenetre)

                    printImage("./image/motus/bleu.png", (200, 100), [825, 500], fenetre)

                    
                    taille = [0, 0, 0, 0, 320, 290, 250, 210]
                    for i in range(len(mot_choisi)):
                        printImage("./image/motus/grille.png", (82, 505), [i*84+taille[len(mot_choisi)], 70], fenetre)

                        printText(mot_partiel[i], 40, "black", (i*84+taille[len(mot_choisi)]+30+2*i, 100), fenetre)
                        pygame.display.flip()

                    printImage("./image/motus/bleu.png", (30, 30), [15, 245], fenetre)

                    printImage("./image/motus/bleu.png", (30, 30), [960, 245], fenetre)

                    printText(str(points1), 32, "black", (20, 250), fenetre)

                    printText(str(points2), 32, "black", (965, 250), fenetre)
                    pygame.display.flip()

                    if etape%2==0:
                        nbr_chance1=0
                        nbr_chance2=0

                    fond = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
                    tour = 0
                    mot_final = []
                    for i in range(len(mot_choisi)):
                        mot_final.append(mot_choisi[i])

                    while tour<6:

                        
                        for i in range(28):
                            if fond[i] == 0:
                                printImage("./image/motus/carresB.jpg", (35.71, 35.71), [i*35.71, 0], fenetre)
                            elif fond[i] == 1 :
                                printImage("./image/motus/carresR.jpg", (35.71, 35.71), [i*35.71, 0], fenetre)
                            elif fond[i] == 2:
                                printImage("./image/motus/carresJ.png", (35.71, 35.71), [i*35.71, 0], fenetre)
                            else:
                                printImage("./image/motus/carresP.jpg", (35.71, 35.71), [i*35.71, 0], fenetre)
                        

                            printText(lettre[i], 25, pygame.Color("black"), (i*35.8+10, 10), fenetre)
                            pygame.display.flip()

                        mot_point = list(mot_partiel)
                        mot_verif = mot_choisi
                        mot_test = mot_partiel[0]
                        verif = []
                        nbr_lettre = 1
                        fin=0
                        for i in range(len(mot_choisi)-1):
                            verif.append(0)
                        

                        taille = [0, 0, 0, 0, 320, 290, 250, 210]
                        for i in range(len(mot_choisi)):

                            printText(mot_partiel[i], 40, pygame.Color("black"), (i*84+taille[len(mot_choisi)]+30+2*i, 100+tour*85), fenetre)
                            pygame.display.flip()

                        while fin==0:

                            lettre_choisis = get_lettre()
                            if lettre_choisis==0:
                                return 0
                            if lettre_choisis == "<":
                                if nbr_lettre>1:
                                    nbr_lettre -= 1
                                    mot_partiel[nbr_lettre] = "."
                                    mot_test = mot_partiel[0:nbr_lettre] 

                                for i in range(len(mot_choisi)):
                                    printImage("./image/motus/bleu.png", (60, 60), [i*84+taille[len(mot_choisi)]+12, 80+tour*85], fenetre)
                                    printText(mot_partiel[i], 40, pygame.Color("black"), (i*84+taille[len(mot_choisi)]+30+1.5*i, 100+tour*85), fenetre)
                                    pygame.display.flip()
                            
                            
                            elif lettre_choisis == ">":
                                mot_dico = ''
                                for i in range(len(mot_test)):
                                    mot_dico = mot_dico + mot_test[i]
                                if len(mot_test)==len(mot_choisi) and (mot_dico.upper()+'\n') in dico:
                                    fin = 1
                                    for i in range(len(mot_choisi)-1):
                                        if mot_test[i+1] == mot_choisi[i+1]:
                                            verif[i] = 2
                                            n = mot_verif.index(mot_test[i+1])+1
                                            mot_verif2 = mot_verif
                                            mot_verif = ''
                                            for k in range(len(mot_verif2)):
                                                if k+1!=n:
                                                    mot_verif += mot_verif2[k]
                                            mot_partiel = list(mot_point)
                                            mot_partiel[i+1] = mot_test[i+1]
                                            mot_point = list(mot_partiel)
                                    for i in range(len(mot_choisi)-1):
                                        if verif[i]!=2:
                                            if mot_test[i+1] in mot_verif[1:]:
                                                verif[i] = 1
                                                n = mot_verif.index(mot_test[i+1])+1
                                                mot_verif2 = mot_verif
                                                mot_verif = ''
                                                for k in range(len(mot_verif2)):
                                                    if k+1!=n:
                                                        mot_verif += mot_verif2[k]
                                    for i in range(len(verif)):
                                        if verif[i]==0 and fond[lettre.index(mot_test[i+1])]==0:
                                            fond[lettre.index(mot_test[i+1])] = 3
                                        elif verif[i]==1 and fond[lettre.index(mot_test[i+1])]!=1:
                                            fond[lettre.index(mot_test[i+1])] = 2
                                        elif verif[i]==2:
                                            fond[lettre.index(mot_test[i+1])] = 1
                                    if mot_test == mot_partiel:
                                        mot_partiel = mot_point

                                    for i in range(len(verif)):
                                        if verif[i]==2:
                                            printImage("./image/motus/rouge.jpg", (60, 60), [(i+1)*84+taille[len(mot_choisi)]+12, 80+tour*85], fenetre)
                                            printText(mot_test[i+1], 40, pygame.Color("black"), [(i+1)*84+taille[len(mot_choisi)]+30+i, 100+tour*85], fenetre)
                                            pygame.display.flip()

                                        elif verif[i] == 1:
                                            printImage("./image/motus/cerclejaune.png", (60, 60), [(i+1)*84+taille[len(mot_choisi)]+12, 80+tour*85], fenetre)
                                            printText(mot_test[i+1], 40, pygame.Color("black"), [(i+1)*84+taille[len(mot_choisi)]+30+i, 100+tour*85], fenetre)
                                            pygame.display.flip()
                                    tour+=1

                                    if mot_test == mot_final:
                                        if kijou%2==0:
                                            nbr_chance1 = tour
                                        else:
                                            nbr_chance2 = tour
                                        tour=10
                                        
                                        printText('Bravo', 40, pygame.Color("green"), (50,500), fenetre)
                                        pygame.display.flip()
                                
                            else:
                                if len(mot_test)<len(mot_choisi):
                                    mot_partiel[nbr_lettre] = lettre_choisis
                                    nbr_lettre += 1
                                    mot_test = mot_partiel[0:nbr_lettre] 

                                    for i in range(len(mot_choisi)):
                                        printImage("./image/motus/bleu.png", (60, 60), [i*84+taille[len(mot_choisi)]+12, 80+tour*85], fenetre)
                                        printText(mot_partiel[i], 40, pygame.Color("black"), [i*84+taille[len(mot_choisi)]+30+i, 100+tour*85], fenetre)
                                        pygame.display.flip()

                            for event in pygame.event.get():
                                if (event.type == QUIT): 
                                    return 0


                
                    if tour!=10:
                        printText('Perdu', 40, pygame.Color("red"), (50,500), fenetre)
                        printText('le mot etait ' + mot_choisi.lower(), 30, pygame.Color("red"), (10,530), fenetre)
                        pygame.display.flip()
                        
                        if kijou%2==0:
                            nbr_chance1 = tour
                        else:
                            nbr_chance2 = tour

                    
                    printImage("./image/motus/suivant.png", (150, 35.7585), [830, 530], fenetre)
                    printImage("./image/juste prix/fleche.png", (50,34.35), [5, 40], fenetre, rotation=180)
                    pygame.display.flip()

                        
                    if etape%2==0:
                        kijou+=1
                        taille_mot=len(mot_choisi)
                    else:
                        taille_mot=0
                        if nbr_chance1>nbr_chance2:
                            points2 += nbr_chance1 - nbr_chance2
                        else:
                            points1 += nbr_chance2 - nbr_chance1

                    etape+=1
                    fin=0
                    while fin==0:
                        for event in pygame.event.get():
                            if (event.type == MOUSEBUTTONUP):
                                x = event.pos[0]
                                y = event.pos[1]
                                if x>830 and x<980 and y>530 and y<564:
                                    fin=1
                                    end=1
                                if(x>21 and x<51 and y>50 and y<61) or (x>5 and x<20 and y>41 and y<71):
                                    fin=1       
                                    end=1
                                    start=1

                            if (event.type == QUIT): 
                                return 0
    
if __name__ == "__main__":
    motus()
