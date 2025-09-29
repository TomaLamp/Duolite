from pygame import *
import pygame
from random import choice


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


    pygame.init()
    pygame.font.init()
    fenetre = pygame.display.set_mode((1000,600))
    fenetre.fill("#4682B4")
    pygame.display.set_caption("motus")
    pygame_icon = pygame.image.load('./image/motus/icon.png')
    pygame.display.set_icon(pygame_icon)
    pygame.display.flip()

    bille = pygame.image.load("./image/motus/play.png").convert_alpha()
    bille = pygame.transform.scale(bille, (700, 350.315))
    fenetre.blit(bille, (150,110))
    pygame.display.flip()
            

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
            bille = pygame.image.load("./image/motus/1joueur.png")
            bille = pygame.transform.scale(bille, (750, 185.7))
            position_bille = [150, 65] 
            fenetre.blit(bille, position_bille)
            pygame.display.flip()

            bille = pygame.image.load("./image/motus/2joueur.png")
            bille = pygame.transform.scale(bille, (750, 185.7))
            position_bille = [150, 350] 
            fenetre.blit(bille, position_bille)
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


        bille = pygame.image.load("./image/motus/bleu.png").convert_alpha()
        bille = pygame.transform.scale(bille, (1000, 600))
        position_bille = [0, 0]
        fenetre.blit(bille, position_bille)
        pygame.display.flip()


        if nb_joueur==1:

            points = 0
            partie = 0
            lettre = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "<", ">"]
            fond = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]

            police = pygame.font.Font(None, 32)
            police.underline = True
            texte = police.render("mes points :",True,pygame.Color("black"))
            fenetre.blit(texte, (10, 200))

            police = pygame.font.Font(None, 32)
            police.underline = True
            texte = police.render("parties jouée :",True,pygame.Color("black"))
            fenetre.blit(texte, (835, 200))


            end=0
            while end==0:
                bille = pygame.image.load("./image/motus/bleu.png").convert_alpha()
                bille = pygame.transform.scale(bille, (60, 60))
                position_bille = [0,40] 
                fenetre.blit(bille, position_bille)

                mot_choisi = choice(liste_mots).rstrip().upper()
                while len(mot_choisi)!=4 and len(mot_choisi)!=5 and len(mot_choisi)!=6 and len(mot_choisi)!=7:
                    mot_choisi = choice(liste_mots).rstrip().upper()

                #print(mot_choisi)
                mot_partiel = [mot_choisi[0]]
                for i in range(1, len(mot_choisi)):
                    mot_partiel.append(".")

                bille = pygame.image.load("./image/motus/bleu.png").convert_alpha()
                bille = pygame.transform.scale(bille, (650, 520))
                position_bille = [170, 70]
                fenetre.blit(bille, position_bille)

                bille = pygame.image.load("./image/motus/bleu.png").convert_alpha()
                bille = pygame.transform.scale(bille, (180, 150))
                position_bille = [10, 500] 
                fenetre.blit(bille, position_bille)

                bille = pygame.image.load("./image/motus/bleu.png").convert_alpha()
                bille = pygame.transform.scale(bille, (200, 100))
                position_bille = [825, 500] 
                fenetre.blit(bille, position_bille)

                
                taille = [0, 0, 0, 0, 320, 290, 250, 210]
                for i in range(len(mot_choisi)):
                    bille = pygame.image.load("./image/motus/grille.png").convert_alpha()
                    bille = pygame.transform.scale(bille, (82, 505))
                    position_bille = [i*84+taille[len(mot_choisi)], 70] 
                    fenetre.blit(bille, position_bille)

                    police = pygame.font.Font(None, 40)
                    texte = police.render(mot_partiel[i],True,pygame.Color("black"))
                    fenetre.blit(texte, (i*84+taille[len(mot_choisi)]+30+2*i, 100))
                    pygame.display.flip()

                bille = pygame.image.load("./image/motus/bleu.png").convert_alpha()
                bille = pygame.transform.scale(bille, (30, 30))
                position_bille = [15, 245] 
                fenetre.blit(bille, position_bille)

                bille = pygame.image.load("./image/motus/bleu.png").convert_alpha()
                bille = pygame.transform.scale(bille, (30, 30))
                position_bille = [960, 245] 
                fenetre.blit(bille, position_bille)

                police = pygame.font.Font(None, 32)
                texte = police.render(str(points),True,pygame.Color("black"))
                fenetre.blit(texte, (20, 250))

                police = pygame.font.Font(None, 32)
                texte = police.render(str(partie),True,pygame.Color("black"))
                fenetre.blit(texte, (965, 250))
                pygame.display.flip()


                fond = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
                tour = 0
                mot_final = []
                for i in range(len(mot_choisi)):
                    mot_final.append(mot_choisi[i])

                while tour<6:

                    
                    for i in range(28):
                        if fond[i] == 0:
                            bille = pygame.image.load("./image/motus/carresB.jpg").convert_alpha()
                            bille = pygame.transform.scale(bille, (35.71, 35.71))
                            position_bille = [i*35.71, 0] 
                            fenetre.blit(bille, position_bille)
                        elif fond[i] == 1 :
                            bille = pygame.image.load("./image/motus/carresR.jpg").convert_alpha()
                            bille = pygame.transform.scale(bille, (35.71, 35.71))
                            position_bille = [i*35.71, 0] 
                            fenetre.blit(bille, position_bille)
                        elif fond[i] == 2:
                            bille = pygame.image.load("./image/motus/carresJ.png").convert_alpha()
                            bille = pygame.transform.scale(bille, (35.71, 35.71))
                            position_bille = [i*35.71, 0] 
                            fenetre.blit(bille, position_bille)
                        else:
                            bille = pygame.image.load("./image/motus/carresP.jpg").convert_alpha()
                            bille = pygame.transform.scale(bille, (35.71, 35.71))
                            position_bille = [i*35.71, 0] 
                            fenetre.blit(bille, position_bille)
                    

                        police = pygame.font.Font(None, 25)
                        texte = police.render(lettre[i],True,pygame.Color("black"))
                        fenetre.blit(texte, (i*35.8+10, 10))
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

                        police = pygame.font.Font(None, 40)
                        texte = police.render(mot_partiel[i],True,pygame.Color("black"))
                        fenetre.blit(texte, (i*84+taille[len(mot_choisi)]+30+2*i, 100+tour*85))
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
                                bille = pygame.image.load("./image/motus/bleu.png").convert_alpha()
                                bille = pygame.transform.scale(bille, (60, 60))
                                position_bille = [i*84+taille[len(mot_choisi)]+12, 80+tour*85] 
                                fenetre.blit(bille, position_bille)

                                police = pygame.font.Font(None, 40)
                                texte = police.render(mot_partiel[i],True,pygame.Color("black"))
                                fenetre.blit(texte, (i*84+taille[len(mot_choisi)]+30+1.5*i, 100+tour*85))
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
                                        bille = pygame.image.load("./image/motus/rouge.jpg").convert_alpha()
                                        bille = pygame.transform.scale(bille, (60, 60))
                                        position_bille = [(i+1)*84+taille[len(mot_choisi)]+12, 80+tour*85] 
                                        fenetre.blit(bille, position_bille)

                                        police = pygame.font.Font(None, 40)
                                        texte = police.render(mot_test[i+1],True,pygame.Color("black"))
                                        fenetre.blit(texte, ((i+1)*84+taille[len(mot_choisi)]+30+i, 100+tour*85))
                                        pygame.display.flip()

                                    elif verif[i] == 1:
                                        bille = pygame.image.load("./image/motus/cerclejaune.png").convert_alpha()
                                        bille = pygame.transform.scale(bille, (60, 60))
                                        position_bille = [(i+1)*84+taille[len(mot_choisi)]+12, 80+tour*85] 
                                        fenetre.blit(bille, position_bille)

                                        police = pygame.font.Font(None, 40)
                                        texte = police.render(mot_test[i+1],True,pygame.Color("black"))
                                        fenetre.blit(texte, ((i+1)*84+taille[len(mot_choisi)]+30+i, 100+tour*85))
                                        pygame.display.flip()
                                tour+=1

                                if mot_test == mot_final:
                                    points+=7-tour
                                    tour=10
                                    
                                    police = pygame.font.Font(None, 40)
                                    texte = police.render('Bravo',True,pygame.Color("green"))
                                    fenetre.blit(texte, (50,500))
                                    pygame.display.flip()
                            
                        else:
                            if len(mot_test)<len(mot_choisi):
                                mot_partiel[nbr_lettre] = lettre_choisis
                                nbr_lettre += 1
                                mot_test = mot_partiel[0:nbr_lettre] 

                                for i in range(len(mot_choisi)):
                                    bille = pygame.image.load("./image/motus/bleu.png").convert_alpha()
                                    bille = pygame.transform.scale(bille, (60, 60))
                                    position_bille = [i*84+taille[len(mot_choisi)]+12, 80+tour*85] 
                                    fenetre.blit(bille, position_bille)

                                    police = pygame.font.Font(None, 40)
                                    texte = police.render(str(mot_partiel[i]),True,pygame.Color("black"))
                                    fenetre.blit(texte, (i*84+taille[len(mot_choisi)]+30+i, 100+tour*85))
                                    pygame.display.flip()

                        for event in pygame.event.get():
                            if (event.type == QUIT): 
                                return 0


                partie+=1
                if tour!=10:
                    police = pygame.font.Font(None, 40)
                    texte = police.render('Perdu',True,pygame.Color("red"))
                    fenetre.blit(texte, (50,500))

                    police = pygame.font.Font(None, 30)
                    texte = police.render('le mot etait ' + mot_choisi.lower(),True,pygame.Color("red"))
                    fenetre.blit(texte, (10,530))

                    pygame.display.flip()

                
                bille = pygame.image.load("./image/motus/suivant.png").convert_alpha()
                bille = pygame.transform.scale(bille, (150, 35.7585))
                position_bille = [830, 530] 
                fenetre.blit(bille, position_bille)

                bille = pygame.image.load("./image/juste prix/fleche.png").convert_alpha()
                bille = pygame.transform.scale(bille, (50,34.35))
                bille = pygame.transform.rotate(bille, 180)
                position_bille = [5, 40] 
                fenetre.blit(bille, position_bille)

                                
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
                        joueur = "1"
                        j2 = "2"
                    else:
                        joueur = "2"
                        j2 = "1"
                    police = pygame.font.Font(None, 55)
                    texte = police.render("Joueur "+ joueur +" ne regardez pas",True,pygame.Color("black"))
                    fenetre.blit(texte, (270, 200))
                    police = pygame.font.Font(None, 55)
                    texte = police.render("Joueur "+ j2 +" vous allez choisir un mot pour l'adversaire",True,pygame.Color("black"))
                    fenetre.blit(texte, (30, 150))
                    bille = pygame.image.load("./image/motus/suivant.png").convert_alpha()
                    bille = pygame.transform.scale(bille, (600, 143.04))
                    fenetre.blit(bille, (200, 350))
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
                police = pygame.font.Font(None, 60)
                police.underline = True
                texte = police.render("Choisissez un mot pour l'adversaire",True,pygame.Color("black"))
                fenetre.blit(texte, (150, 10))
                pygame.display.flip()

                c = 0
                for i in range(3):
                    for j in range(5):
                        bille = pygame.image.load("./image/motus/mots.png").convert_alpha()
                        bille = pygame.transform.scale(bille, (250, 42.85))
                        rectImage = bille.get_rect().width 
                        position_bille = [i*250 + 60*(i+1), j*100 + 105] 
                        fenetre.blit(bille, position_bille)

                        police = pygame.font.Font(None, 32)
                        texte = police.render(choix_mot[c],True,pygame.Color("black"))
                        rectText = texte.get_rect().width 
                        fenetre.blit(texte, ((i*250 + 60*(i+1))+rectImage/2 - rectText/2, (j*100 + 105)+10))
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

                police = pygame.font.Font(None, 32)
                police.underline = True
                texte = police.render("Joueur 1 :",True,pygame.Color("black"))
                fenetre.blit(texte, (10, 200))

                police = pygame.font.Font(None, 32)
                police.underline = True
                texte = police.render("Joueur 2 :",True,pygame.Color("black"))
                fenetre.blit(texte, (880, 200))


                end=0
                while end==0:

                    mot_choisi = mot_choisi.upper()

                    #print(mot_choisi)
                    mot_partiel = [mot_choisi[0]]
                    for i in range(1, len(mot_choisi)):
                        mot_partiel.append(".")

                    bille = pygame.image.load("./image/motus/bleu.png").convert_alpha()
                    bille = pygame.transform.scale(bille, (650, 520))
                    position_bille = [170, 70]
                    fenetre.blit(bille, position_bille)

                    bille = pygame.image.load("./image/motus/bleu.png").convert_alpha()
                    bille = pygame.transform.scale(bille, (180, 150))
                    position_bille = [10, 500] 
                    fenetre.blit(bille, position_bille)

                    bille = pygame.image.load("./image/motus/bleu.png").convert_alpha()
                    bille = pygame.transform.scale(bille, (200, 100))
                    position_bille = [825, 500] 
                    fenetre.blit(bille, position_bille)

                    
                    taille = [0, 0, 0, 0, 320, 290, 250, 210]
                    for i in range(len(mot_choisi)):
                        bille = pygame.image.load("./image/motus/grille.png").convert_alpha()
                        bille = pygame.transform.scale(bille, (82, 505))
                        position_bille = [i*84+taille[len(mot_choisi)], 70] 
                        fenetre.blit(bille, position_bille)

                        police = pygame.font.Font(None, 40)
                        texte = police.render(mot_partiel[i],True,pygame.Color("black"))
                        fenetre.blit(texte, (i*84+taille[len(mot_choisi)]+30+2*i, 100))
                        pygame.display.flip()

                    bille = pygame.image.load("./image/motus/bleu.png").convert_alpha()
                    bille = pygame.transform.scale(bille, (30, 30))
                    position_bille = [15, 245] 
                    fenetre.blit(bille, position_bille)

                    bille = pygame.image.load("./image/motus/bleu.png").convert_alpha()
                    bille = pygame.transform.scale(bille, (30, 30))
                    position_bille = [960, 245] 
                    fenetre.blit(bille, position_bille)

                    police = pygame.font.Font(None, 32)
                    texte = police.render(str(points1),True,pygame.Color("black"))
                    fenetre.blit(texte, (20, 250))

                    police = pygame.font.Font(None, 32)
                    texte = police.render(str(points2),True,pygame.Color("black"))
                    fenetre.blit(texte, (965, 250))
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
                                bille = pygame.image.load("./image/motus/carresB.jpg").convert_alpha()
                                bille = pygame.transform.scale(bille, (35.71, 35.71))
                                position_bille = [i*35.71, 0] 
                                fenetre.blit(bille, position_bille)
                            elif fond[i] == 1 :
                                bille = pygame.image.load("./image/motus/carresR.jpg").convert_alpha()
                                bille = pygame.transform.scale(bille, (35.71, 35.71))
                                position_bille = [i*35.71, 0] 
                                fenetre.blit(bille, position_bille)
                            elif fond[i] == 2:
                                bille = pygame.image.load("./image/motus/carresJ.png").convert_alpha()
                                bille = pygame.transform.scale(bille, (35.71, 35.71))
                                position_bille = [i*35.71, 0] 
                                fenetre.blit(bille, position_bille)
                            else:
                                bille = pygame.image.load("./image/motus/carresP.jpg").convert_alpha()
                                bille = pygame.transform.scale(bille, (35.71, 35.71))
                                position_bille = [i*35.71, 0] 
                                fenetre.blit(bille, position_bille)
                        

                            police = pygame.font.Font(None, 25)
                            texte = police.render(lettre[i],True,pygame.Color("black"))
                            fenetre.blit(texte, (i*35.8+10, 10))
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

                            police = pygame.font.Font(None, 40)
                            texte = police.render(mot_partiel[i],True,pygame.Color("black"))
                            fenetre.blit(texte, (i*84+taille[len(mot_choisi)]+30+2*i, 100+tour*85))
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
                                    bille = pygame.image.load("./image/motus/bleu.png").convert_alpha()
                                    bille = pygame.transform.scale(bille, (60, 60))
                                    position_bille = [i*84+taille[len(mot_choisi)]+12, 80+tour*85] 
                                    fenetre.blit(bille, position_bille)

                                    police = pygame.font.Font(None, 40)
                                    texte = police.render(mot_partiel[i],True,pygame.Color("black"))
                                    fenetre.blit(texte, (i*84+taille[len(mot_choisi)]+30+1.5*i, 100+tour*85))
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
                                            bille = pygame.image.load("./image/motus/rouge.jpg").convert_alpha()
                                            bille = pygame.transform.scale(bille, (60, 60))
                                            position_bille = [(i+1)*84+taille[len(mot_choisi)]+12, 80+tour*85] 
                                            fenetre.blit(bille, position_bille)

                                            police = pygame.font.Font(None, 40)
                                            texte = police.render(mot_test[i+1],True,pygame.Color("black"))
                                            fenetre.blit(texte, ((i+1)*84+taille[len(mot_choisi)]+30+i, 100+tour*85))
                                            pygame.display.flip()

                                        elif verif[i] == 1:
                                            bille = pygame.image.load("./image/motus/cerclejaune.png").convert_alpha()
                                            bille = pygame.transform.scale(bille, (60, 60))
                                            position_bille = [(i+1)*84+taille[len(mot_choisi)]+12, 80+tour*85] 
                                            fenetre.blit(bille, position_bille)

                                            police = pygame.font.Font(None, 40)
                                            texte = police.render(mot_test[i+1],True,pygame.Color("black"))
                                            fenetre.blit(texte, ((i+1)*84+taille[len(mot_choisi)]+30+i, 100+tour*85))
                                            pygame.display.flip()
                                    tour+=1

                                    if mot_test == mot_final:
                                        if kijou%2==0:
                                            nbr_chance1 = tour
                                        else:
                                            nbr_chance2 = tour
                                        tour=10
                                        
                                        police = pygame.font.Font(None, 40)
                                        texte = police.render('Bravo',True,pygame.Color("green"))
                                        fenetre.blit(texte, (50,500))
                                        pygame.display.flip()
                                
                            else:
                                if len(mot_test)<len(mot_choisi):
                                    mot_partiel[nbr_lettre] = lettre_choisis
                                    nbr_lettre += 1
                                    mot_test = mot_partiel[0:nbr_lettre] 

                                    for i in range(len(mot_choisi)):
                                        bille = pygame.image.load("./image/motus/bleu.png").convert_alpha()
                                        bille = pygame.transform.scale(bille, (60, 60))
                                        position_bille = [i*84+taille[len(mot_choisi)]+12, 80+tour*85] 
                                        fenetre.blit(bille, position_bille)

                                        police = pygame.font.Font(None, 40)
                                        texte = police.render(mot_partiel[i],True,pygame.Color("black"))
                                        fenetre.blit(texte, (i*84+taille[len(mot_choisi)]+30+i, 100+tour*85))
                                        pygame.display.flip()

                            for event in pygame.event.get():
                                if (event.type == QUIT): 
                                    return 0


                
                    if tour!=10:
                        police = pygame.font.Font(None, 40)
                        texte = police.render('Perdu',True,pygame.Color("red"))
                        fenetre.blit(texte, (50,500))

                        police = pygame.font.Font(None, 30)
                        texte = police.render('le mot etait ' + mot_choisi.lower(),True,pygame.Color("red"))
                        fenetre.blit(texte, (10,530))

                        pygame.display.flip()
                        
                        if kijou%2==0:
                            nbr_chance1 = tour
                        else:
                            nbr_chance2 = tour

                    
                    bille = pygame.image.load("./image/motus/suivant.png").convert_alpha()
                    bille = pygame.transform.scale(bille, (150, 35.7585))
                    position_bille = [830, 530] 
                    fenetre.blit(bille, position_bille)

                    bille = pygame.image.load("./image/juste prix/fleche.png").convert_alpha()
                    bille = pygame.transform.scale(bille, (50,34.35))
                    bille = pygame.transform.rotate(bille, 180)
                    position_bille = [5, 40] 
                    fenetre.blit(bille, position_bille)

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
    

