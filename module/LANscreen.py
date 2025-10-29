import pygame
from module.pygameCore import *
from module.connectLAN import *
from random import randint
import time
import pickle

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
            rectTextHeight = printText(connexion[1], 80, "green", (500,300), fenetre, Alignement="Center", Alignementy="Center").height
            printText("Connexion établie avec :", 50, "green", (500, 300-rectTextHeight/2), fenetre, Alignement="Center", Alignementy="Top")
            pygame.draw.rect(fenetre, "#000000", (400,375,200,50))
            printText("Deconnexion", 40, "white", (500, 400), fenetre, Alignement="Center", Alignementy="Center")

        pygame.display.flip()

        x,y=get_pos()
        if x=="NULL":
            if connexion[0]!=None:
                connexion[0].close()
            exit()

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
                nom = str(data)[2:-1]
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
                        if connexion[0]!=None:
                            connexion[0].close()    
                        exit()

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
                    conn.send(bytes(nomj1, "utf-8"))
                    data = str(conn.recv(1024))[2:-1]
                    connexion[0]=conn
                    connexion[1]=data
                    connexion[2]=False
                else:
                    pygame.draw.rect(fenetre, "#001751", (200,450,600,30), border_radius=50)
                    printText("Aucune connexion trouvée", 40, "red", (500, 450), fenetre , Alignement="Center")
                    pygame.display.flip()
                    pygame.time.wait(3000)
        elif x>400 and x<600 and y>375 and y<415 and connexion[0]!=None:
            connexion[0].close()
            connexion[0]=None


def decoScreen(fenetre, connexion):
    pygame.draw.rect(fenetre, "#272728", (305,205,400,200), border_radius=50)
    pygame.draw.rect(fenetre, "#001751", (300,200,400,200), border_radius=50)
    printImage("./image/close.png", (30, 30), (650, 215), fenetre)
    printText("La connexion avec", 50, "red", (500, 230), fenetre, Alignement="Center")
    printText(connexion[1], 70, "red", (500, 300), fenetre, Alignement="Center", Alignementy="Center")
    printText("a été interrompue", 50, "red", (500, 340), fenetre, Alignement="Center")
    pygame.display.flip()

    while True:
        x,y = get_pos()
        if x=="NULL":
            exit()
        if x>650 and x<680 and y>215 and y<245:
            return 0
        
def quitScreen(screen, connexion, color, subcolor):
    pygame.draw.rect(screen, subcolor, (305,205,400,200), border_radius=50)
    pygame.draw.rect(screen, color, (300,200,400,200), border_radius=50)
    printImage("./image/close.png", (30, 30), (650, 215), screen)
    printText(connexion[1], 70, "red", (500, 255), screen, Alignement="Center", Alignementy="Center")
    printText("a quité la partie", 50, "red", (500, 325), screen, Alignement="Center")
    pygame.display.flip()

    while True:
        x,y = get_pos()
        if x=="NULL":
            return "NULL"
        
def waitScreen(screen, connexion, color, subcolor, text):
    pygame.draw.rect(screen, subcolor, (305,205,400,200), border_radius=50)
    pygame.draw.rect(screen, color, (300,200,400,200), border_radius=50)
    printImage("./image/close.png", (30, 30), (650, 215), screen)
    printText(connexion[1], 100, "red", (500, 320), screen, Alignement="Center", Alignementy="Center")
    printText("En attente de", 50, "red", (500, 235), screen, Alignement="Center")
    pygame.display.flip()

    connexion[0].send(bytes(text, "utf-8"))
    connexion[0].setblocking(False)
    data=b""

    while True:
        x,y = get_pos()

        try:
            data = connexion[0].recv(1024)
        except BlockingIOError:
            pass

        if x=="NULL":
            return "NULL"
        if x>650 and x<680 and y>215 and y<245:
            return 0
        if data==bytes(text, "utf-8"):
            connexion[0].send(bytes(text+"2", "utf-8"))
            return 1
        if data==bytes(text+"2", "utf-8"):
            return 1
        

def recv_int_data(connexion, fenetre, color, subcolor, nbError=404):
    conn = connexion[0]
    while True:
        try:
            data = conn.recv(1024)
            prop = int.from_bytes(data, "big")
            if prop==nbError:
                result = quitScreen(fenetre, connexion, color, subcolor)
                if result=="NULL":
                    return "NULL"
            else:
                return prop
        except BlockingIOError:
            pass
                        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT): 
                conn.send(nbError.to_bytes(2))
                return "NULL"
            

def recv_str_data(connexion, fenetre, color, subcolor, nbError="404"):
    conn = connexion[0]
    while True:
        try:
            data = conn.recv(1024)
            prop = str(data, "utf-8")
            if prop==nbError:
                result = quitScreen(fenetre, connexion, color, subcolor)
                if result=="NULL":
                    return "NULL"
            else:
                return prop
        except BlockingIOError:
            pass
                        
        for event in pygame.event.get():
            if (event.type == pygame.QUIT): 
                conn.send(bytes(nbError, "utf-8"))
                return "NULL"
            
def recv_list_data(connexion, fenetre, color, subcolor, nbError="404"):
    conn = connexion[0]
    while True:
        try:
            data = pickle.loads(conn.recv(1024))
            if len(data)!=0 and data[0]=="404":
                result = quitScreen(fenetre, connexion, "#E3C400", "#BE9F02")
                if result=="NULL":
                    return ["NULL"]
            else:
                return data
        except BlockingIOError:
            pass 

        for event in pygame.event.get():
            if (event.type == pygame.QUIT): 
                conn.send(pickle.dumps([nbError]))
                return 0


def send_data(connexion, data, fenetre, color, subcolor):
    if isConnClose(connexion[0]):
        result = quitScreen(fenetre, connexion, color, subcolor)
        if result=="NULL":
            return "NULL"
    else:
        connexion[0].send(data)
        return "OK"