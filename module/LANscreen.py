import pygame
from module.pygameCore import *
from module.connectLAN import *
from random import randint
import time

def LANscreen(fenetre, connexion=[None, None, None]):
    pygame.draw.rect(fenetre, "#272728", (205,105,600,400), border_radius=50)
    pygame.draw.rect(fenetre, "#001751", (200,100,600,400), border_radius=50)
    printText("Connexion LAN", 50, "black", (500, 110), fenetre, Alignement="Center")
    printImage("./image/close.png", (30, 30), (750, 115), fenetre)

    conn = None
    while True:
        if connexion[0]==None:
            pygame.draw.rect(fenetre, "#001751", (200,150,600,350), border_radius=50)
            pygame.draw.rect(fenetre, "#000000", (250,180,500,100))
            pygame.draw.rect(fenetre, "#000000", (250,345,500,100))
            printText("Créer une room", 50, "white", (500, 230), fenetre, Alignement="Center", Alignementy="Center")
            printText("Rejoindre une room", 50, "white", (500, 395), fenetre, Alignement="Center", Alignementy="Center")
        else:
            pygame.draw.rect(fenetre, "#001751", (200,150,600,350), border_radius=50)
            rectTextHeight = printText(connexion[1][2:-1], 80, "green", (500,300), fenetre, Alignement="Center", Alignementy="Center").height
            printText("Connexion établie avec :", 50, "green", (500, 300-rectTextHeight/2), fenetre, Alignement="Center", Alignementy="Top")
            pygame.draw.rect(fenetre, "#000000", (400,375,200,50))
            printText("Deconnexion", 40, "white", (500, 400), fenetre, Alignement="Center", Alignementy="Center")

        pygame.display.flip()

        x,y=get_pos()
        if x=="NULL":
            return sys.exit()

        if x>750 and x<780 and y>115 and y<145:
            return None
        elif x>250 and x<750 and y>180 and y<280 and connexion[0]==None:
            code = str(randint(1000, 9999))
            pygame.draw.rect(fenetre, "#001751", (200,150,600,350), border_radius=50)
            pygame.draw.rect(fenetre, "#000000", (250,250,500,100))
            printText(code, 80, "white", (500, 300), fenetre, Alignement="Center", Alignementy="Center")
            printText("Code de la Room", 40, "black", (500, 240), fenetre, Alignement="Center", Alignementy="Top")
            printText("En attente de connexion...", 40, "red", (500, 410), fenetre , Alignement="Center")
            pygame.display.flip()

            conn = createRoom(code)
            if conn != None:
                pygame.draw.rect(fenetre, "#001751", (200,400,600,50), border_radius=50)
                printText("Connexion reussie", 40, "green", (500, 410), fenetre , Alignement="Center")
                pygame.display.flip()
                pygame.time.wait(2000)

                nomj1 = get_nom()[0]
                conn.send(bytes(nomj1, "utf-8"))
                data = conn.recv(1024)
                nom = str(data)
                connexion[0]=conn
                connexion[1]=nom
                connexion[2]=True
        elif x>250 and x<750 and y>345 and y<445 and connexion[0]==None:
            code=""
            pygame.draw.rect(fenetre, "#001751", (200,150,600,350), border_radius=50)
            pygame.draw.rect(fenetre, "#000000", (400,375,200,50))
            printText("Rentrez un code", 40, "black", (500, 240), fenetre, Alignement="Center", Alignementy="Top")
            printText("Connexion", 32, "white", (500, 400), fenetre, Alignement="Center", Alignementy="Center")
            pygame.draw.rect(fenetre, "#334676", (250,250,500,100), border_radius=50)

            pygame.display.flip()

            wantConn = True
            end=0
            while end==0:
                for event in pygame.event.get():
                    letter=""
                    if (event.type == pygame.MOUSEBUTTONUP):
                        x = event.pos[0]
                        y = event.pos[1]

                        if x>750 and x<780 and y>115 and y<150:
                            end=1
                            wantConn = False
                        elif x>400 and x<600 and y>375 and y<415 and len(code)==4:
                            end=1

                    if event.type == KEYDOWN:
                        if pygame.key.get_pressed()[K_LSHIFT] and event.key<=57 and event.key>=48:
                            letter = str(event.key-48)
                        elif event.key==K_BACKSPACE:
                            letter = "<"
                        elif event.key>1073741912 and event.key<1073741922:
                            letter = str(event.key-1073741912)
                        elif event.key == 1073741922:
                            letter = "0"
                        elif event.key==13:
                            end=1
                    
                        if letter == "<":
                            code = code[:len(code)-1]
                        elif len(code)<4:
                            code += letter


                    if (event.type == pygame.QUIT): 
                            sys.exit()

                pygame.draw.rect(fenetre, "#334676", (250,250,500,100), border_radius=50)
                rectText = printText(code, 100, "white", (500, 300), fenetre, Alignement="Center", Alignementy="Center").width
                if time.time() % 1 > 0.5:
                    pygame.draw.rect(fenetre, "black", (rectText/2+500, 260, 2, 80))
                pygame.display.update()

            if wantConn:
                conn = joinRoom(code)
                if conn != None:
                    pygame.draw.rect(fenetre, "#001751", (200,450,600,30), border_radius=50)
                    printText("Connexion reussie", 40, "green", (500, 450), fenetre , Alignement="Center")
                    pygame.display.flip()
                    pygame.time.wait(2000)

                    nomj1 = get_nom()[0]
                    conn.send(nomj1)
                    data = str(conn.recv(1024), "utf-8", errors='ignore')
                    connexion[0]=conn
                    connexion[1]=data
                    connexion[2]=False
                else:
                    pygame.draw.rect(fenetre, "#001751", (200,450,600,30), border_radius=50)
                    printText("Aucune connexion trouvée", 40, "red", (500, 450), fenetre , Alignement="Center")
                    pygame.display.flip()
                    pygame.time.wait(3000)
        if x>400 and x<600 and y>375 and y<415 and connexion[0]!=None:
            connexion[0].close()
            connexion[0]=None