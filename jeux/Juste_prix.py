from pygame import *
import pygame
from module.pygameCore import *
from random import randint

def justePrix():
    
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
                    rectwidth = printImage("./image/juste prix/fond.jpg", (90, 50), (445, 270), fenetre).width
                    printText(nombre, 72, "black", (rectwidth/2 + 445, 270), fenetre, Alignement="Center")
                    pygame.display.flip()  

                if (event.type == QUIT): 
                    return "NULL"

                
                

    fenetre = initScreen((1000,600), "Juste prix", "#B707C6", './image/juste prix/icon.png')

    printImage("./image/juste prix/play.png", (700, 549.5), (150,-10), fenetre)
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

        printImage("./image/juste prix/joueur1.png", (700, 173.1), (160, 70), fenetre)
        printImage("./image/juste prix/joueur2.png", (700, 173.1), (160, 370), fenetre)
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
                printImage("./image/juste prix/nbr.png", (50, 50), (400+70*j, 340+60*i), fenetre)

                if c<10 and c>0:
                    printText(str(c), 33, "black", (420+70*j, 355+60*i), fenetre)
                elif c==-2:
                    printImage("./image/juste prix/effacer.png", (40, 40), (405+70*j, 345+60*i), fenetre)
                elif c==-1:
                    printText(str(0), 33, "black", (420+70*j, 355+60*i), fenetre)
                elif c==0:
                    printImage("./image/juste prix/entrer.png", (40, 40), (405+70*j, 345+60*i), fenetre)

                pygame.display.flip()
                
                if j != 2: 
                    c+=1                      


        printText(str(borne_min) + "<", 72, "black", (350, 270), fenetre)
        printText("<" + str(borne_sup), 72, "black", (550, 270), fenetre)

        printText("Nombre d'essai max :  ", 36, "black", (10, 10), fenetre)
        printText("ton nombre de coup :  ", 36, "black", (690, 10), fenetre)

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

                    printImage("./image/juste prix/fond.jpg", (30, 30), (270, 10), fenetre)
                    printImage("./image/juste prix/fond.jpg", (1000, 200), (20, 110), fenetre)
                    printImage("./image/juste prix/fond.jpg", (60, 60), (5, 40), fenetre)
                    printText("Tes points :  " + str(point), 36, "black", (10, 500), fenetre)
                    printText(str(nbr_essais_max), 36, "black", (270, 10), fenetre)
                    printText("Choisissez un nombre : ", 76, "Yellow", (120, 70), fenetre, police="./police/Sketchzone.otf")
                    pygame.display.flip()

                    while ton_nombre != mon_nombre and nbr_essais <= nbr_essais_max:

                        printImage("./image/juste prix/fond.jpg", (30, 30), (960, 10), fenetre)
                        printText(str(nbr_essais), 36, "black", (960, 10), fenetre)
                        printImage("./image/juste prix/fond.jpg", (450, 50), (300, 270), fenetre)
                        printText((3-len(str(borne_min)))* "  " + str(borne_min) + "<", 72, "black", (320, 270), fenetre)
                        printText("<" + str(borne_sup), 72, "black", (550, 270), fenetre)
                        pygame.display.flip()

                        ton_nombre = choix_nombre()
                        if ton_nombre == "NULL":
                            return 0

                        printImage("./image/juste prix/fond.jpg", (450, 70), (400, 190), fenetre)

                        if ton_nombre < mon_nombre and borne_min < ton_nombre and borne_sup > ton_nombre:
                            
                            printText("Plus", 66, "green", (440, 180), fenetre, police="./police/Sketchzone.otf")
                            nbr_essais += 1
                            borne_min = ton_nombre

                        elif ton_nombre > mon_nombre and borne_min < ton_nombre and borne_sup > ton_nombre:
                            
                            printText("Moins", 66, "red", (420, 180), fenetre, police="./police/Sketchzone.otf")
                            borne_sup = ton_nombre
                            nbr_essais += 1

                        elif ton_nombre == mon_nombre:
                            point += 13 - nbr_essais

                            printImage("./image/juste prix/fond.jpg", (200, 50), (10, 500), fenetre)
                            printText("Tes points :  " + str(point), 36, "black", (10, 500), fenetre)
                            printImage("./image/juste prix/fond.jpg", (1000, 100), (120, 70), fenetre)
                            printText("Bravo ! Vous avez trouvé en "+str(nbr_essais)+" essais", 52, "Green", (55, 110), fenetre, police="./police/Sketchzone.otf")
                            printText("Le nombre était : "+str(mon_nombre), 52, "Green", (240, 180), fenetre, police="./police/Sketchzone.otf")
                            printImage("./image/juste prix/suivant.png", (300, 80.7), (680, 500), fenetre)
                            printImage("./image/juste prix/fleche.png", (50, 34.35), (5, 40), fenetre, rotation=180)
                            
                            pygame.display.flip() 

                            fin = 0
                            while fin == 0:
                                for event in pygame.event.get():
                                    if (event.type == MOUSEBUTTONUP):
                                        x = event.pos[0]
                                        y = event.pos[1]
                                        if x > 680 and x < 977 and y > 500 and y < 579:
                                            fin=1
                                            printImage("./image/juste prix/fond.jpg", (300, 82), (680, 500), fenetre)
                                            pygame.display.flip()
                                        if(x>21 and x<51 and y>50 and y<61) or (x>5 and x<20 and y>41 and y<71):
                                            fin=1
                                            restart=1
                                            end=1
                    
                                    if (event.type == QUIT): 
                                        return 0

                        pygame.display.flip()

                        if nbr_essais>nbr_essais_max and ton_nombre != mon_nombre :
                            
                            printImage("./image/juste prix/fond.jpg", (450, 70), (400, 190), fenetre)
                            printImage("./image/juste prix/fond.jpg", (1000, 130), (120, 70), fenetre)
                            printText("Perdu ! Vous n'avez plus d'essai", 62, "Red", (50, 110), fenetre, police="./police/Sketchzone.otf")
                            printText("Le nombre était : "+str(mon_nombre), 62, "Red", (210, 180), fenetre, police="./police/Sketchzone.otf")
                            printImage("./image/juste prix/rejouer.png", (300, 80.7), (680, 500), fenetre)
                            printImage("./image/juste prix/fleche.png", (50, 34.35), (5, 40), fenetre, rotation=180)
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
                                            printImage("./image/juste prix/fond.jpg", (300, 82), (680, 500), fenetre)
                                            printImage("./image/juste prix/fond.jpg", (200, 50), (10, 500), fenetre)
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

                    
                    printImage("./image/juste prix/fond.jpg", (30, 30), [270, 10], fenetre)

                    printImage("./image/juste prix/fond.jpg", (1000, 200), [20, 110], fenetre)

                    printImage("./image/juste prix/fond.jpg", (60, 60), [5, 40], fenetre)

                    printText("Points joueur 1 :  " + str(pointj1), 36, "black", (10, 500), fenetre)

                    printText("Points joueur 2 :  " + str(pointj2), 36, "black", (10, 550), fenetre)

                    printText(str(nbr_essais_max), 36, "black", (270, 10), fenetre)

                    printText(joueur +" Choisissez un nombre : ", 66, "Yellow", (10, 70), fenetre, police="./police/Sketchzone.otf")
                    pygame.display.flip()


                    mon_nombre = randint(1,borne_sup) 
                    while ton_nombre != mon_nombre and nbr_essais <= nbr_essais_max:

                        printImage("./image/juste prix/fond.jpg", (30, 30), [960, 10], fenetre)

                        printText(str(nbr_essais), 36, "black", (960, 10), fenetre)

                        printImage("./image/juste prix/fond.jpg", (450, 50), [300, 270], fenetre)

                        printText((3-len(str(borne_min)))* "  " + str(borne_min) + "<", 72, "black", (320, 270), fenetre)
                        printText("<" + str(borne_sup), 72, "black", (550, 270), fenetre)
                        pygame.display.flip()

                        ton_nombre = choix_nombre()
                        if ton_nombre=="NULL":
                            return 0

                        printImage("./image/juste prix/fond.jpg", (450, 90), [400, 170], fenetre)

                        
                        if ton_nombre < mon_nombre and borne_min < ton_nombre and borne_sup > ton_nombre:
                            
                            printText("Plus", 66, "green", (440, 170), fenetre, police="./police/Sketchzone.otf")
                            pygame.display.flip()

                            nbr_essais += 1
                            borne_min = ton_nombre
                        elif ton_nombre > mon_nombre and borne_min < ton_nombre and borne_sup > ton_nombre:
                            
                            printText("Moins", 66, "red", (420, 170), fenetre, police="./police/Sketchzone.otf")
                            pygame.display.flip()

                            borne_sup = ton_nombre
                            nbr_essais += 1
                        elif ton_nombre == mon_nombre:
                            kijou += 1
                        
                            printImage("./image/juste prix/fond.jpg", (1000, 100), [10, 70], fenetre)

                            printText("Bravo ! Vous avez trouvé en "+str(nbr_essais)+" essais", 52, "Green", (55, 110), fenetre, police="./police/Sketchzone.otf")

                            printText("Le nombre était : "+str(mon_nombre), 52, "Green", (240, 180), fenetre, police="./police/Sketchzone.otf")
                            pygame.display.flip()

                            printImage("./image/juste prix/suivant.png", (300, 80.7), [680, 500], fenetre)

                            printImage("./image/juste prix/fleche.png", (50,34.35), [5, 40], fenetre, rotation=180)

                            pygame.display.flip()

                            fin = 0
                            while fin == 0:
                                for event in pygame.event.get():
                                    if (event.type == MOUSEBUTTONUP):
                                        x = event.pos[0]
                                        y = event.pos[1]
                                        if x > 680 and x < 977 and y > 500 and y < 579:
                                            fin=1
                                            printImage("./image/juste prix/fond.jpg", (300, 82), [680, 500], fenetre)
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
                            
                            printImage("./image/juste prix/fond.jpg", (300, 100), [10, 500], fenetre)

                            printText("Points joueur 1 :  " + str(pointj1), 36, "black", (10, 500), fenetre)

                            printText("Points joueur 2 :  " + str(pointj2), 36, "black", (10, 550), fenetre)

                            printImage("./image/juste prix/fond.jpg", (1000, 200), [10, 70], fenetre)

                            printText("Perdu ! Vous n'avez plus d'essai", 62, "Red", (50, 110), fenetre, police="./police/Sketchzone.otf")

                            printText("Le nombre était : "+str(mon_nombre), 62, "Red", (210, 180), fenetre, police="./police/Sketchzone.otf")

                            printImage("./image/juste prix/rejouer.png", (300, 80.7), [680, 500], fenetre)

                            printImage("./image/juste prix/fleche.png", (50,34.35), [5, 40], fenetre, rotation=180)

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
                                            printImage("./image/juste prix/fond.jpg", (300, 82), [680, 500], fenetre)
                                            printImage("./image/juste prix/fond.jpg", (200, 50), [10, 500], fenetre)
                                            pygame.display.flip()
                                        if(x>21 and x<51 and y>50 and y<61) or (x>5 and x<20 and y>41 and y<71):
                                            fin=1
                                            restart=1
                                            end=1


                                    if (event.type == QUIT): 
                                        return 0
                                    
if __name__ == "__main__":
    justePrix()
                    


 
    