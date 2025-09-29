from pygame import *
import pygame


def bataille_naval():
    from dis import dis

    A1=["A2","B1"]
    A2=["A1","A3","B2"]
    A3=["A2","A4","B3"]
    A4=["A3","A5","B4"]
    A5=["A4","A6","B5"]
    A6=["A5","A7","B6"]
    A7=["A6","A8","B7"]
    A8=["A7","A9","B8"]
    A9=["A8","A10","B9"]
    A10=["A9","B10"]
    B1=["A1","B2","C1"]
    B2=["A2","B1","B3","C2"]
    B3=["A3","B2","B4","C3"]
    B4=["A4","C4","B5","B3"]
    B5=["A5","C5","B4","B6"]
    B6=["A6","C6","B7","B5"]
    B7=["A7","C7","B6","B8"]
    B8=["A8","C8","B7","B9"]
    B9=["A9","C9","B8","B10"]
    B10=["A10","B9","C10"]
    C1=["B1","C2","D1"]
    C2=["D2","B2","C1","C3"]
    C3=["B3","D3","C2","C4"]
    C4=["B4","D4","C3","C5"]
    C5=["B5","D5","C4","C6"]
    C6=["D6","B6","C5","C7"]
    C7=["D7","B7","C6","C8"]
    C8=["C7","C9","B8","D8"]
    C9=["C8","C10","B9","D9"]
    C10=["C9","B10","D10"]
    D1=["D2","C1","E1"]
    D2=["D1","C2","E2","D3"]
    D3=["D2","D4","C3","E3"]
    D4=["D3","D5","E4","C4"]
    D5=["D4","D5","C5","E5"]
    D6=["D5","D7","C6","E6"]
    D7=["D6","D8","C7","E7"]
    D8=["D7","D9","C8","E8"]
    D9=["D8","D10","C9","E9"]
    D10=["D9","C10","E10"]
    E1=["E2","D1","F1"]
    E2=["E1","E3","D2","C2"]
    E3=["E2","E4","D3","F3"]
    E4=["E3","E5","D4","F4"]
    E5=["E4","E6","F5","D5"]
    E6=["E5","E7","D6","F6"]
    E7=["E6","E8","D7","F7"]
    E8=["E7","E9","D8","F8"]
    E9=["E8","E10","F9","D9"]
    E10=["F10","D10","E9"]
    F1=["F2","E1","G1"]
    F2=["F1","F3","G2","E2"]
    F3=["F2","F4","G3","E3"]
    F4=["F3","F5","G4","E4"]
    F5=["F4","F6","G5","E5"]
    F6=["F5","F7","G6","E6"]
    F7=["F6","F8","G7","E7"]
    F8=["F7","F9","G8","E8"]
    F9=["F8","F10","G9","E9"]
    F10=["F9","G10","E10"]
    G1=["G2","F1","H1"]
    G2=["G1","G3","F2","H2"]
    G3=["G2","G4","F3","H3"]
    G4=["G3","G5","F4","H4"]
    G5=["G4","G6","F5","H5"]
    G6=["G5","G7","F6","H6"]
    G7=["G6","F8","F7","H7"]
    G8=["G7","G9","F8","H8"]
    G9=["G8","G10","F9","H9"]
    G10=["G9","F10","H10"]
    H1=["H2","G1","I1"]
    H2=["H1","H3","G2","I2"]
    H3=["H2","H4","G3","I3"]
    H4=["H3","H5","G4","I4"]
    H5=["H4","H6","G5","I5"]
    H6=["H5","H7","G6","I6"]
    H7=["H6","H8","G7","I7"]
    H8=["H7","H9","G8","I8"]
    H9=["H8","H10","G9","I9"]
    H10=["H9","G10","I10"]
    I1=["I2","H1","J1"]
    I2=["I3","I1","H2","J2"]
    I3=["I2","I4","H3","J3"]
    I4=["I3","I5","H4","J4"]
    I5=["I4","I6","H5","J5"]
    I6=["I5","I7","H6","J6"]
    I7=["I6","I8","H7","J7"]
    I8=["I7","I9","H8","J8"]
    I9=["I8","I10","H9","J9"]
    I10=["I9","H10","J10"]
    J1=["J2","I1"]
    J2=["J1","J3","I2"]
    J3=["J2","J4","I3"]
    J4=["J3","J5","I4"]
    J5=["J4","J6","I5"]
    J6=["J5","J7","I6"]
    J7=["J6","J8","I7"]
    J8=["J7","J9","I8"]
    J9=["J8","J10","I9"]
    J10=["J9","I10"]
    total=[A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,H1,H2,H3,H4,H5,H6,H7,H8,H9,H10,I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,J1,J2,J3,J4,J5,J6,J7,J8,J9,J10] 

    def get_case(kijou):
        end=0
        while end==0:
            pygame.init()
            for event in pygame.event.get():
                if (event.type == MOUSEBUTTONUP):
                    x = event.pos[0]
                    y = event.pos[1]
                    casey = (y - 176)//40
                    if kijou == 1:
                        if x>339:
                            casex = (x - 60)//40
                        elif x>110:
                            casex = (x - 65)//40
                        else:
                            casex = (x - 68)//40
                    else:
                        if x>879:
                            casex = (x - 560)//40
                        elif x>804:
                            casex = (x - 563)//40
                        else:
                            casex = (x - 568)//40
                    lettres = ['A','B','C','D','E','F','G','H',"I",'J']
                    if kijou==1 and x > 72 and x < 455 and y > 173 and y < 576:
                        case = str(lettres[casey]) + str(casex+1)
                        return case 
                    elif kijou==2 and x > 572 and x < 955 and y > 173 and y < 576:
                        case = str(lettres[casey]) + str(casex+1)
                        return case

                if(event.type == QUIT): 
                    return "NULL"

    def place_point(kijou, case, fenetre, image):
        if case[1] == "1":
            x = 70

        if case[1] == "2":
            x = 110

        if case[1] == "3":
            x = 148

        if case[1] == "4":
            x = 185

        if case[1] == "5":
            x = 225

        if case[1] == "6":
            x = 263

        if case[1] == "7":
            x = 302

        if case[1] == "8":
            x = 340

        if case[1] == "9":
            x = 380

        if case[1:3] == "10":
            x = 418

        
        if case[0:1] == "A":
            y = 177

        if case[0:1] == "B":
            y = 217

        if case[0:1] == "C":
            y = 262

        if case[0:1] == "D":
            y = 302

        if case[0:1] == "E":
            y = 342

        if case[0:1] == "F":
            y = 382

        if case[0:1] == "G":
            y = 427

        if case[0:1] == "H":
            y = 465

        if case[0:1] == "I":
            y = 507

        if case[0:1] == "J":
            y = 550

        if kijou == 2:
            x = x + 500
        
        pygame.init()
        bille = pygame.image.load(image).convert_alpha()
        bille = pygame.transform.scale(bille, (40, 40))
        position_bille = [x, y]
        fenetre.blit(bille, position_bille)
        pygame.display.flip()


    def printt(textes, fenetre, color):
        bille = pygame.image.load("./image/bataille_naval/fond texte.JPG").convert_alpha()
        bille = pygame.transform.scale(bille, (1005, 100))
        position_bille = [0, 0] 
        fenetre.blit(bille, position_bille)
        rectImage = bille.get_rect()
        pygame.display.flip()

        police = pygame.font.Font("./police/Modusa.ttf", 64)
        texte = police.render(textes,True,pygame.Color(color))
        rectTexte = texte.get_rect()
        rectTexte.center = rectImage.center
        fenetre.blit(texte, rectTexte)
        pygame.display.flip()

    def place_ship(kijou, bateau, fenetre):
        image = "./image/bataille_naval/bateau" + str(len(bateau)) + ".png"
        case = bateau[0]

        if case[1] == "1":
            x = 70

        if case[1] == "2":
            x = 110

        if case[1] == "3":
            x = 148

        if case[1] == "4":
            x = 185

        if case[1] == "5":
            x = 225

        if case[1] == "6":
            x = 263

        if case[1] == "7":
            x = 302

        if case[1] == "8":
            x = 340

        if case[1] == "9":
            x = 380

        if case[1:3] == "10":
            x = 418

        
        if case[0:1] == "A":
            y = 177

        if case[0:1] == "B":
            y = 217

        if case[0:1] == "C":
            y = 262

        if case[0:1] == "D":
            y = 302

        if case[0:1] == "E":
            y = 342

        if case[0:1] == "F":
            y = 382

        if case[0:1] == "G":
            y = 427

        if case[0:1] == "H":
            y = 465

        if case[0:1] == "I":
            y = 507

        if case[0:1] == "J":
            y = 550

        if kijou == 2:
            x = x + 500

        if len(bateau) == 1:
            bille = pygame.image.load(image).convert_alpha()
            bille = pygame.transform.scale(bille, (40, 40))
            position_bille = [x, y]
            fenetre.blit(bille, position_bille)
            pygame.display.flip()
        elif bateau[0][0] == bateau[1][0]:
            bille = pygame.image.load(image).convert_alpha()
            bille = pygame.transform.scale(bille, (40*len(bateau), 40))
            position_bille = [x, y]
            fenetre.blit(bille, position_bille)
            pygame.display.flip()
        else:
            bille = pygame.image.load(image).convert_alpha()
            bille = pygame.transform.scale(bille, (40*len(bateau), 40))
            bille = pygame.transform.rotate(bille, 90)
            position_bille = [x, y]
            fenetre.blit(bille, position_bille)
            pygame.display.flip()

    def place_Rship(kijou, bateau, fenetre):
        image = "./image/bataille_naval/bateau" + str(len(bateau)) + "R.png"
        case = bateau[0]

        if case[1] == "1":
            x = 70

        if case[1] == "2":
            x = 110

        if case[1] == "3":
            x = 148

        if case[1] == "4":
            x = 185

        if case[1] == "5":
            x = 225

        if case[1] == "6":
            x = 263

        if case[1] == "7":
            x = 302

        if case[1] == "8":
            x = 340

        if case[1] == "9":
            x = 380

        if case[1:3] == "10":
            x = 418

        
        if case[0:1] == "A":
            y = 177

        if case[0:1] == "B":
            y = 217

        if case[0:1] == "C":
            y = 262

        if case[0:1] == "D":
            y = 302

        if case[0:1] == "E":
            y = 342

        if case[0:1] == "F":
            y = 382

        if case[0:1] == "G":
            y = 427

        if case[0:1] == "H":
            y = 465

        if case[0:1] == "I":
            y = 507

        if case[0:1] == "J":
            y = 550

        if kijou == 2:
            x = x + 500

        if len(bateau) == 1:
            bille = pygame.image.load(image).convert_alpha()
            bille = pygame.transform.scale(bille, (40, 40))
            position_bille = [x, y]
            fenetre.blit(bille, position_bille)
            pygame.display.flip()
        elif bateau[0][0] == bateau[1][0]:
            bille = pygame.image.load(image).convert_alpha()
            bille = pygame.transform.scale(bille, (40*len(bateau), 40))
            position_bille = [x, y]
            fenetre.blit(bille, position_bille)
            pygame.display.flip()
        else:
            bille = pygame.image.load(image).convert_alpha()
            bille = pygame.transform.scale(bille, (40*len(bateau), 40))
            bille = pygame.transform.rotate(bille, 90)
            position_bille = [x, y]
            fenetre.blit(bille, position_bille)
            pygame.display.flip()

    def place_line(kijou, bateau, fenetre):
        image = "./image/bataille_naval/red line.png"
        case = bateau[0]

        if case[1] == "1":
            x = 70

        if case[1] == "2":
            x = 110

        if case[1] == "3":
            x = 148

        if case[1] == "4":
            x = 185

        if case[1] == "5":
            x = 225

        if case[1] == "6":
            x = 263

        if case[1] == "7":
            x = 302

        if case[1] == "8":
            x = 340

        if case[1] == "9":
            x = 380

        if case[1:3] == "10":
            x = 418

        
        if case[0:1] == "A":
            y = 177

        if case[0:1] == "B":
            y = 217

        if case[0:1] == "C":
            y = 262

        if case[0:1] == "D":
            y = 302

        if case[0:1] == "E":
            y = 342

        if case[0:1] == "F":
            y = 382

        if case[0:1] == "G":
            y = 427

        if case[0:1] == "H":
            y = 465

        if case[0:1] == "I":
            y = 507

        if case[0:1] == "J":
            y = 550

        if kijou == 2:
            x = x + 500

        if len(bateau) == 1:
            bille = pygame.image.load(image).convert_alpha()
            bille = pygame.transform.scale(bille, (40-2, 40))
            position_bille = [x+2, y]
            fenetre.blit(bille, position_bille)
            pygame.display.flip()
        elif bateau[0][0] == bateau[1][0]:
            bille = pygame.image.load(image).convert_alpha()
            bille = pygame.transform.scale(bille, (40*len(bateau)-10, 40))
            position_bille = [x+2, y]
            fenetre.blit(bille, position_bille)
            pygame.display.flip()
        else:
            bille = pygame.image.load(image).convert_alpha()
            bille = pygame.transform.scale(bille, (40*len(bateau)-2, 40))
            bille = pygame.transform.rotate(bille, 90)
            position_bille = [x, y]
            fenetre.blit(bille, position_bille)
            pygame.display.flip()

    def copie_bateau(bateau):
        copie = []
        lettre = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        if bateau[0][0] == bateau[1][0]:
            for i in range(len(bateau)):
                place = 0
                for j in range(len(copie)):
                    if int(bateau[i][1:len(bateau[i])]) > int(copie[j][1:len(copie[j])]):
                        place += 1
                copie.insert(place, bateau[i])
            return copie

        else:
            for i in range(len(bateau)):
                place = 0
                for j in range(len(copie)):
                    if lettre.index(bateau[i][0]) > lettre.index(copie[j][0]):
                        place += 1
                copie.insert(place, bateau[i])
            return copie


    def acote(lettre, choix):
        case = 0
        end = 0
        verif = 0
        if lettre[0:1] == "A":
            case = 0
        
        if lettre[0:1] == "B":
            case = 10

        if lettre[0:1] == "C":
            case = 20

        if lettre[0:1] == "D":
            case = 30

        if lettre[0:1] == "E":
            case = 40

        if lettre[0:1] == "F":
            case = 50

        if lettre[0:1] == "G":
            case = 60

        if lettre[0:1] == "H":
            case = 70

        if lettre[0:1] == "I":
            case = 80

        if lettre[0:1] == "J":
            case = 90  

        chiffre = lettre[1:2]
        chiffre = int(chiffre)
        

        d10 = ["A10","B10","C10","D10","E10","F10","G10","H10","I10","J10"]
        entier = [1,2,3,4,5,6,7,8,9,10]
        if lettre in d10 :
            while(end==0): 
                if choix not in total[(chiffre + case) + 8]:
                    return False
                else:
                    end += 1
                    return True
        else:
            while(end==0): 
                if choix not in total[(chiffre + case) - 1]:
                    return False
                else:
                    end += 1
                    return True

    def suite(case1, case2, choix, nbrcase):
        end = 0
        verifinverse = 0
        verif = 0
        result1 = 0
        result2 = 0
        lettres = ['A','B','C','D','E','F','G','H',"I",'J']
        if case2[0:1] == "A":
            case = 0
        
        if case2[0:1] == "B":
            case = 1

        if case2[0:1] == "C":
            case = 2

        if case2[0:1] == "D":
            case = 3

        if case2[0:1] == "E":
            case = 4

        if case2[0:1] == "F":
            case = 5

        if case2[0:1] == "G":
            case = 6

        if case2[0:1] == "H":
            case = 7

        if case2[0:1] == "I":
            case = 8

        if case2[0:1] == "J":
            case = 9 

        ret = 0
        if nbrcase == 3:
            ret = 1
        if nbrcase == 4:
            ret = 2

        d10 = ["A10","B10","C10","D10","E10","F10","G10","H10","I10","J10"]
        if case1[0:1] == choix[0:1] and case2[0:1] == choix[0:1] :
            verif = case2[0:1]
            if int(case1[1:2]) < int(case2[1:2]):
                if int(case2[1:2]) + 1 <= 10: #lui il marche 
                    verifinverse = int(case2[1:2]) + 1
                    result1 = verif + str(verifinverse)
                if int(case2[1:2]) - nbrcase > 0: #lui il marche
                    result2 = verif + str(int(case2[1:2]) - nbrcase)
                if case1 in d10:
                    verifinverse = int(case2[1:2]) + 1
                    result2 = verif + str(8 - ret)
                    result1 = 0
            else:
                if int(case2[1:2]) - nbrcase + 1 + ret > 0: #lui il marche
                    verifinverse = int(case2[1:2]) - nbrcase + 1 + ret
                    result1 = verif + str(verifinverse)
                if int(case2[1:2]) + 1 < 10: #lui il marche
                    verifinverse = int(case2[1:2]) + 1 + ret
                    result2 = verif + str(verifinverse+1)
                if case2 in d10:
                    verifinverse = int(case2[1:2]) + 6 - ret
                    result2 = verif + str(verifinverse+1)
        

        if case1[1:2] == choix[1:2] and case2[1:2] == choix[1:2] :
            verif = case2[1:2]
            if case1 < case2:
                if case + 1  < 10:
                    verifinverse = lettres[case+1]
                    result1 = verifinverse + verif
                if case - nbrcase > -1:
                    verifinverse = lettres[case-nbrcase]
                    result2 = verifinverse + verif
                if case2 in d10 and case1 in d10:
                    result2 = 0
                    result1 = 0
                    if case-nbrcase > -1:
                        verifinverse = lettres[case-nbrcase]
                        result1 = verifinverse + str(10)
                    if case+1 < 10:
                        verif = lettres[case+1]
                        result2 = verif + str(10)

            else:
                if case > 0:
                    verifinverse = lettres[case-1]
                    result1 =  verifinverse + verif
                if case + nbrcase < 10:
                    verifinverse = lettres[case+nbrcase]
                    result2 = verifinverse + verif
                if case2 in d10 and case1 in d10:
                    result2 = 0
                    result1 = 0
                    if case-nbrcase+1 > -1:
                        if nbrcase == 2:
                            verifinverse = lettres[case-nbrcase+1]
                    if case-nbrcase+2 > -1:
                        if nbrcase == 3:
                            verifinverse = lettres[case-nbrcase+2]
                    if case-nbrcase+3 > -1:
                        if nbrcase == 4:
                            verifinverse = lettres[case-nbrcase+3]
                        result1 = verifinverse + str(10)
                    if case+nbrcase < 10:
                        verif = lettres[case+nbrcase]
                        result2 = verif + str(10)                  

        while(end==0): 
            if choix != result1 and choix != result2: 
                
                return False
                
            else:
                end += 1
                return True


    def previsual(case2, case3, nbrcase, bateau):
        end = 0
        sortie = 0
        while (end==0):
            droite = 0
            gauche = 0
            haut = 0
            bas = 0
            lettres = ['A','B','C','D','E','F','G','H',"I",'J']
            if case2[0:1] == "A":
                case = 0
            
            if case2[0:1] == "B":
                case = 1

            if case2[0:1] == "C":
                case = 2

            if case2[0:1] == "D":
                case = 3

            if case2[0:1] == "E":
                case = 4

            if case2[0:1] == "F":
                case = 5

            if case2[0:1] == "G":
                case = 6

            if case2[0:1] == "H":
                case = 7

            if case2[0:1] == "I":
                case = 8

            if case2[0:1] == "J":
                case = 9


            if case3 != 0:
                if case3[0:1] == "A":
                    case1 = 0
                
                if case3[0:1] == "B":
                    case1 = 1

                if case3[0:1] == "C":
                    case1 = 2

                if case3[0:1] == "D":
                    case1 = 3

                if case3[0:1] == "E":
                    case1 = 4

                if case3[0:1] == "F":
                    case1 = 5

                if case3[0:1] == "G":
                    case1 = 6

                if case3[0:1] == "H":
                    case1 = 7

                if case3[0:1] == "I":
                    case1 = 8

                if case3[0:1] == "J":
                    case1 = 9

            droite = [20, 20, 20, 20, 20]
            gauche = [20, 20, 20, 20, 20]
            haut = [20, 20, 20, 20, 20]
            bas = [20, 20, 20, 20, 20]
            verifdroite = 0
            verifgauche = 0
            verifhaut = 0
            verifbas = 0
            ordre = 0
            ordreinverse = 0


            if case3 == 0 or case2[0] == case3[0]:
                if case3 != 0:
                    if int(case2[1:len(case2)]) < int(case3[1:len(case2)]):
                        ordre = 1
                        ordreinverse = 0
                    if int(case2[1:len(case2)]) > int(case3[1:len(case2)]):
                        ordre = 0
                        ordreinverse = 1
                for i in range(nbrcase):
                    if case3 == 0:
                        if (int(case2[1:len(case2)]) + 1 + i + ordre < 11):
                            droite[i] = int(case2[1:len(case2)]) + 1 + i + ordre
                    else:
                        if (int(case2[1:len(case2)]) + 1 + i + ordre < 11):
                            droite[i] = int(case2[1:len(case2)]) + 1 + i + ordre 
                for i in range(nbrcase):
                    if case3 == 0:
                        if (int(case2[1:len(case2)]) - 1 - i - ordreinverse > 0):
                            gauche[i] = int(case2[1:len(case2)]) - 1 - i - ordreinverse   
                    else:
                        if (int(case2[1:len(case2)]) - 1 - i - ordreinverse + 1 > 0):
                            gauche[i] = int(case2[1:len(case2)]) - 1 - i - ordreinverse +1

            
            if case3 == 0 or case2[1] == case3[1]:
                if case3 != 0:
                    if case < case1:
                        ordre = 1
                        ordreinverse = 0
                    if case > case1:
                        ordre = 0
                        ordreinverse = 1
                for i in range(nbrcase):
                    if case3 == 0:
                        if (case - 1 - i - ordreinverse> -1):
                            haut[i] = case - 1 - i - ordreinverse 
                    else:
                        if (case - 1 - i - ordreinverse > -1):
                            haut[i] = case - 1 - i - ordreinverse + 1
                for i in range(nbrcase):
                    if case3 == 0 :
                        if (case + 1 + i + ordre < 10):
                            bas[i] = case + i + 1 + ordre 
                    else:
                        if (case + 1 + i + ordre < 10):
                            bas[i] = case + i + 1 + ordre -1

            
            for i in range(nbrcase):
                if (droite[i] == 20 or str(case2[0]) + str(droite[i]) in bateau) and (droite[i] == 20 or str(case2[0]) + str(droite[i]) != case2):
                    break
                verifdroite += 1
            for i in range(nbrcase):
                if (gauche[i] == 20 or str(case2[0]) + str(gauche[i]) in bateau) and (gauche[i] == 20 or str(case2[0]) + str(gauche[i]) != case2):
                    break
                verifgauche += 1
                
                
                
            for i in range(nbrcase):
                if (haut[i] == 20 or (str(lettres[haut[i]]) + str(case2[1:len(case2)])) in bateau) and (haut[i] == 20 or str(lettres[haut[i]]) + str(case2[1:len(case2)]) != case2):
                    break
                verifhaut += 1
            for i in range(nbrcase):
                if (bas[i] == 20 or (str(lettres[bas[i]]) + str(case2[1:len(case2)])) in bateau) and (bas[i] == 20 or str(lettres[bas[i]]) + str(case2[1:len(case2)]) != case2):
                    break
                verifbas += 1
                
                    
            
            ligne = verifdroite + verifgauche
            colonne = verifhaut + verifbas

        
            if ligne < nbrcase and colonne < nbrcase:
                if case3 == 0:
                    return False
                else:
                    
                    return False
                
            elif ligne >= nbrcase or colonne >= nbrcase:
                return True

                

    def notdouble(c, bateau, bateauA):
        end = 0
        grille=["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","B1","B2","B3","B4","B5","B6","B7","B8","B9","B10","C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","E1","E2","E3","E4","E5","E6","E7","E8","E9","E10","F1","F2","F3","F4","F5","F6","F7","F8","F9","F10","G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","H1","H2","H3","H4","H5","H6","H7","H8","H9","H10","I1","I2","I3","I4","I5","I6","I7","I8","I9","I10","J1","J2","J3","J4","J5","J6","J7","J8","J9","J10"]
        while (end==0):
            if c in bateau or c not in grille:
                
                return False
            else:
                end += 1
                return True

        

    pygame.init()
    pygame.font.init()
    fenetre = pygame.display.set_mode((1000,600))
    fond = pygame.image.load("./image/bataille_naval/fond.jpg").convert()
    fenetre.blit(fond, (0,0))
    pygame.display.flip()
    pygame.display.set_caption("bataille navale")
    pygame_icon = pygame.image.load("./image/bataille_naval/bateau1.png")
    pygame.display.set_icon(pygame_icon)

    bille = pygame.image.load("./image/bataille_naval/play.png").convert_alpha()
    bille = pygame.transform.scale(bille, (700, 420))
    fenetre.blit(bille, (160,66))
    pygame.display.flip()
    

    fin = 0
    while fin == 0:
        for event in pygame.event.get():
            if (event.type == MOUSEBUTTONUP):
                    x = event.pos[0]
                    y = event.pos[1]
                    if x > 161 and x < 859 and y > 298 and y < 485:
                        fin = 1 
                
            if (event.type == KEYDOWN) or (event.type == QUIT): 
                    return 0

    start = 0
    while start==0:  
        end=0
        bateau=[]
        bateau1=[]
        bateau2=[]
        bateau3=[]
        bateau33=[]
        bateau4=[]
        bateau5=[]
        coule5 = 4
        coule4 = 3
        coule33 = 2
        coule3 = 2
        coule2 = 1

        b2teau=[]
        b2teau1=[]
        b2teau2=[]
        b2teau3=[]
        b2teau33=[]
        b2teau4=[]
        b2teau5=[]
        cou2e5 = 4
        cou2e4 = 3
        cou2e33 = 2
        cou2e3 = 2
        cou2e2 = 1

        


        bille = pygame.image.load("./image/bataille_naval/grille4.png").convert_alpha()
        bille = pygame.transform.scale(bille, (1000, 600))
        position_bille = [0, 0] 
        fenetre.blit(bille, position_bille)
        pygame.display.flip()

        police = pygame.font.Font(None, 44)
        texte = police.render("Joueur 1 ",True,pygame.Color("yellow"))
        rectTexte = texte.get_rect()
        fenetre.blit(texte, (10, 100))
        pygame.display.flip()

        printt("BATEAU DE 1", fenetre, "black")
        c1=get_case(1)
        if c1=="NULL":
            return 0
        end = 0
        while end==0:
            if notdouble(c1, bateau, bateau1) == False:
                printt("case deja prise", fenetre, "red")
                c1=get_case(1)
                if c1=="NULL":
                    return 0  
                continue
            end = 1
        bateau1.append(c1)
        bateau.append(c1)
        place_point(1, c1, fenetre, "./image/bataille_naval/point.png")
        bateauc1 = list(bateau1)

        printt("BATEAU DE 2", fenetre, "black")
        c2=get_case(1)
        if c2=="NULL":
            return 0
        end = 0
        while end==0:
            if notdouble(c2, bateau, bateau2) == False:
                printt("case deja prise", fenetre, "red") 
                c2=get_case(1) 
                if c2=="NULL":
                    return 0
                continue
            end = 1
        bateau2.append(c2)
        bateau.append(c2)
        place_point(1, c2, fenetre, "./image/bataille_naval/point.png")
        c21=get_case(1)
        if c21=="NULL":
            return 0
        end = 0
        while end==0:
            if acote(c2, c21) == False:
                printt("choisissez a coté", fenetre, "red")
                c21=get_case(1)
                if c21=="NULL":
                    return 0
                continue
            if notdouble(c21, bateau, bateau2) == False:
                printt("case deja prise", fenetre, "red")
                c21=get_case(1)
                if c21=="NULL":
                    return 0
                continue
            end = 1
        bateau2.append(c21)
        bateau.append(c21)
        place_point(1, c21, fenetre, "./image/bataille_naval/point.png")
        bateauc2 = copie_bateau(bateau2)
        place_line(1, bateauc2, fenetre)


        printt("BATEAU DE 3", fenetre, "black")
        c3=get_case(1)
        if c3=="NULL":
            return 0
        end = 0
        while end==0:
            if previsual(c3, 0, 2, bateau) == False:
                printt("vous ne pouvez pas placer ici", fenetre, "red")
                c3=get_case(1)
                if c3=="NULL":
                    return 0
                continue
            if notdouble(c3, bateau, bateau3) == False:
                printt("case deja prise", fenetre, "red")
                c3=get_case(1)
                if c3=="NULL":
                    return 0
                continue
            end = 1
        bateau3.append(c3)
        bateau.append(c3)
        place_point(1, c3, fenetre, "./image/bataille_naval/point.png")
        c31=get_case(1)
        if c31=="NULL":
            return 0
        end = 0
        while end==0:
            if acote(c3, c31) == False:
                printt("choisissez a coté", fenetre, "red")
                c31=get_case(1)
                if c31=="NULL":
                    return 0
                continue
            if previsual(c3, c31, 2, bateau) == False:
                printt("vous ne pouvez pas placer ici", fenetre, "red")
                c31=get_case(1)
                if c31=="NULL":
                    return 0
                continue
            if notdouble(c31, bateau, bateau3) == False:
                printt("case deja prise", fenetre, "red")
                c31=get_case(1)
                if c31=="NULL":
                    return 0
                continue
            end = 1
        bateau3.append(c31)
        bateau.append(c31)
        place_point(1, c31, fenetre, "./image/bataille_naval/point.png")
        c32=get_case(1)
        if c32=="NULL":
            return 0
        end = 0
        while end==0:
            if suite(c3, c31, c32, 2) == False:
                printt("choisissez a coté", fenetre, "red")
                c32=get_case(1)
                if c32=="NULL":
                    return 0
                continue
            if notdouble(c32, bateau, bateau3) == False:
                printt("case deja prise", fenetre, "red")
                c32=get_case(1)
                if c32=="NULL":
                    return 0
                continue
            end = 1
        bateau3.append(c32)
        bateau.append(c32)
        place_point(1, c32, fenetre, "./image/bataille_naval/point.png")
        bateauc3 = copie_bateau(bateau3)
        place_line(1, bateauc3, fenetre)



        printt("2e BATEAU DE 3", fenetre, "black")
        c33=get_case(1)
        if c33=="NULL":
            return 0
        end = 0
        while end==0:
            if previsual(c33, 0, 2, bateau) == False:
                printt("vous ne pouvez pas placer ici", fenetre, "red")
                c33=get_case(1)
                if c33=="NULL":
                    return 0
                continue
            if notdouble(c33, bateau, bateau33) == False:
                printt("case deja prise", fenetre, "red")
                c33=get_case(1)
                if c33=="NULL":
                    return 0
                continue
            end = 1
        bateau33.append(c33)
        bateau.append(c33)
        place_point(1, c33, fenetre, "./image/bataille_naval/point.png")
        c331=get_case(1)
        if c331=="NULL":
            return 0
        end = 0
        while end==0:
            if acote(c33, c331) == False:
                printt("choisissez a coté", fenetre, "red")
                c331=get_case(1)
                if c331=="NULL":
                    return 0
                continue
            if previsual(c33, c331, 2, bateau) == False:
                printt("vous ne pouvez pas placer ici", fenetre, "red")
                c331=get_case(1)
                if c331=="NULL":
                    return 0
                continue
            if notdouble(c331, bateau, bateau33) == False:
                printt("case deja prise", fenetre, "red")
                c331=get_case(1)
                if c331=="NULL":
                    return 0
                continue
            end = 1
        bateau33.append(c331)
        bateau.append(c331)
        place_point(1, c331, fenetre, "./image/bataille_naval/point.png")
        c332=get_case(1)
        if c332=="NULL":
            return 0
        end = 0
        while end==0:
            if suite(c33, c331, c332, 2) == False:
                printt("choisissez a coté", fenetre, "red")
                c332=get_case(1)
                if c332=="NULL":
                    return 0
                continue
            if notdouble(c332, bateau, bateau33) == False:
                printt("case deja prise", fenetre, "red")
                c332=get_case(1)
                if c332=="NULL":
                    return 0
                continue
            end = 1
        bateau33.append(c332)
        bateau.append(c332)
        place_point(1, c332, fenetre, "./image/bataille_naval/point.png")
        bateauc33 = copie_bateau(bateau33)
        place_line(1, bateauc33, fenetre)


        printt("BATEAU DE 4", fenetre, "black")
        c4=get_case(1)
        if c4=="NULL":
            return 0
        end = 0
        while end==0:
            if previsual(c4, 0, 3, bateau) == False:
                printt("vous ne pouvez pas placer ici", fenetre, "red")
                c4=get_case(1)
                if c4=="NULL":
                    return 0
                continue
            if notdouble(c4, bateau, bateau4) == False:
                printt("case deja prise", fenetre, "red")
                c4=get_case(1)
                if c4=="NULL":
                    return 0
                continue
            end = 1
        bateau4.append(c4)
        bateau.append(c4)
        place_point(1, c4, fenetre, "./image/bataille_naval/point.png")
        c41=get_case(1)
        if c41=="NULL":
            return 0
        end = 0
        while end==0:
            if acote(c4, c41) == False:
                printt("choisissez a coté", fenetre, "red")
                c41=get_case(1)
                if c41=="NULL":
                    return 0
                continue
            if previsual(c4, c41, 3, bateau) == False:
                printt("vous ne pouvez pas placer ici", fenetre, "red")
                c41=get_case(1)
                if c41=="NULL":
                    return 0
                continue
            if notdouble(c41, bateau, bateau4) == False:
                printt("case deja prise", fenetre, "red")
                c41=get_case(1)
                if c41=="NULL":
                    return 0
                continue
            end = 1
        bateau4.append(c41)
        bateau.append(c41)
        place_point(1, c41, fenetre, "./image/bataille_naval/point.png")
        c42=get_case(1)
        if c42=="NULL":
            return 0
        end = 0
        while end==0:
            if suite(c4, c41, c42, 2) == False:
                printt("choisissez a coté", fenetre, "red")
                c42=get_case(1)
                if c42=="NULL":
                    return 0
                continue
            if notdouble(c42, bateau, bateau4) == False:
                printt("case deja prise", fenetre, "red")
                c42=get_case(1)
                if c42=="NULL":
                    return 0
                continue
            end = 1
        bateau4.append(c42)
        bateau.append(c42)
        place_point(1, c42, fenetre, "./image/bataille_naval/point.png")
        c43=get_case(1)
        if c43=="NULL":
            return 0
        end = 0
        while end==0:
            if suite(c4, c42, c43, 3) == False:
                printt("choisissez a coté", fenetre, "red")
                c43=get_case(1)
                if c43=="NULL":
                    return 0
                continue
            if notdouble(c43, bateau, bateau4) == False:
                printt("case deja prise", fenetre, "red")
                c43=get_case(1)
                if c43=="NULL":
                    return 0
                continue
            end = 1
        bateau4.append(c43)
        bateau.append(c43)
        place_point(1, c43, fenetre, "./image/bataille_naval/point.png")
        bateauc4 = copie_bateau(bateau4)
        place_line(1, bateauc4, fenetre)


        printt("BATEAU DE 5", fenetre, "black")
        c5=get_case(1)
        if c5=="NULL":
            return 0
        end = 0
        while end==0:
            if previsual(c5, 0, 4, bateau) == False:
                printt("vous ne pouvez pas placer ici", fenetre, "red")
                c5=get_case(1)
                if c5=="NULL":
                    return 0
                continue
            if notdouble(c5, bateau, bateau5) == False:
                printt("case deja prise", fenetre, "red")
                c5=get_case(1)
                if c5=="NULL":
                    return 0
                continue
            end = 1
        bateau5.append(c5)
        bateau.append(c5)
        place_point(1, c5, fenetre, "./image/bataille_naval/point.png")
        c51=get_case(1)
        if c51=="NULL":
            return 0
        end = 0
        while end==0:
            if acote(c5, c51) == False:
                printt("choisissez a coté", fenetre, "red")
                c51=get_case(1)
                if c51=="NULL":
                    return 0
                continue
            if previsual(c5, c51, 4, bateau) == False:
                printt("vous ne pouvez pas placer ici", fenetre, "red")
                c51=get_case(1)
                if c51=="NULL":
                    return 0
                continue
            if notdouble(c51, bateau, bateau5) == False:
                printt("case deja prise", fenetre, "red")
                c51=get_case(1)
                if c51=="NULL":
                    return 0
                continue
            end = 1
        bateau5.append(c51)
        bateau.append(c51)
        place_point(1, c51, fenetre, "./image/bataille_naval/point.png")
        c52=get_case(1)
        if c52=="NULL":
            return 0
        end = 0
        while end==0:
            if suite(c5, c51, c52, 2) == False:
                printt("choisissez a coté", fenetre, "red")
                c52=get_case(1)
                if c52=="NULL":
                    return 0
                continue
            if notdouble(c52, bateau, bateau5) == False:
                printt("case deja prise", fenetre, "red")
                c52=get_case(1)
                if c52=="NULL":
                    return 0
                continue
            end = 1
        bateau5.append(c52)
        bateau.append(c52)
        place_point(1, c52, fenetre, "./image/bataille_naval/point.png")
        c53=get_case(1)
        if c53=="NULL":
            return 0
        end = 0
        while end==0:
            if suite(c5, c52, c53, 3) == False:
                printt("choisissez a coté", fenetre, "red")
                c53=get_case(1)
                if c53=="NULL":
                    return 0
                continue
            if notdouble(c53, bateau, bateau5) == False:
                printt("case deja prise", fenetre, "red")
                c53=get_case(1)
                if c53=="NULL":
                    return 0
                continue
            end = 1
        bateau5.append(c53)
        bateau.append(c53)
        place_point(1, c53, fenetre, "./image/bataille_naval/point.png")
        c54=get_case(1)
        if c54=="NULL":
            return 0
        suite(c5, c53, c54, 4)
        notdouble(c54, bateau, bateau5)
        end = 0
        while end==0:
            if suite(c5, c53, c54, 4) == False:
                printt("choisissez a coté", fenetre, "red")
                c54=get_case(1)
                if c54=="NULL":
                    return 0
                continue
            if notdouble(c54, bateau, bateau5) == False:
                printt("case deja prise", fenetre, "red")
                c54=get_case(1)
                if c54=="NULL":
                    return 0
                continue
            end = 1
        bateau5.append(c54)
        bateau.append(c54)
        place_point(1, c54, fenetre, "./image/bataille_naval/point.png")
        bateauc5 = copie_bateau(bateau5)
        place_line(1, bateauc5, fenetre)


        bille = pygame.image.load("./image/bataille_naval/grille4.png").convert_alpha()
        bille = pygame.transform.scale(bille, (1000, 600))
        position_bille = [0, 0] 
        fenetre.blit(bille, position_bille)
        pygame.display.flip()

        police = pygame.font.Font(None, 44)
        texte = police.render("Joueur 2",True,pygame.Color("orange"))
        rectTexte = texte.get_rect()
        fenetre.blit(texte, (870, 100))
        pygame.display.flip()


        printt("joueur 2", fenetre, "orange")


        printt("BATEAU DE 1", fenetre, "black")
        cc1=get_case(2)
        if cc1=="NULL":
            return 0
        end = 0
        while end==0:
            if notdouble(cc1, b2teau, b2teau1) == False:
                printt("case deja prise", fenetre, "red")
                cc1=get_case(2)
                if cc1=="NULL":
                    return 0  
                continue
            end = 1
        b2teau1.append(cc1)
        b2teau.append(cc1)
        place_point(2, cc1, fenetre, "./image/bataille_naval/point.png")
        b2teauc1 = list(b2teau1)

        printt("BATEAU DE 2", fenetre, "black")
        cc2=get_case(2)
        if cc2=="NULL":
            return 0
        end = 0
        while end==0:
            if notdouble(cc2, b2teau, b2teau2) == False:
                printt("case deja prise", fenetre, "red") 
                cc2=get_case(2) 
                if cc2=="NULL":
                    return 0
                continue
            end = 1
        b2teau2.append(cc2)
        b2teau.append(cc2)
        place_point(2, cc2, fenetre, "./image/bataille_naval/point.png")
        cc21=get_case(2)
        if cc21=="NULL":
            return 0
        end = 0
        while end==0:
            if acote(cc2, cc21) == False:
                printt("choisissez a coté", fenetre, "red")
                cc21=get_case(2)
                if cc21=="NULL":
                    return 0
                continue
            if notdouble(cc21, b2teau, b2teau2) == False:
                printt("case deja prise", fenetre, "red")
                cc21=get_case(2)
                if cc21=="NULL":
                    return 0
                continue
            end = 1
        b2teau2.append(cc21)
        b2teau.append(cc21)
        place_point(2, cc21, fenetre, "./image/bataille_naval/point.png")
        b2teauc2 = copie_bateau(b2teau2)
        place_line(2, b2teauc2, fenetre)


        printt("BATEAU DE 3", fenetre, "black")
        cc3=get_case(2)
        if cc3=="NULL":
            return 0
        end = 0
        while end==0:
            if previsual(cc3, 0, 2, b2teau) == False:
                printt("vous ne pouvez pas placer ici", fenetre, "red")
                cc3=get_case(2)
                if cc3=="NULL":
                    return 0
                continue
            if notdouble(cc3, b2teau, b2teau3) == False:
                printt("case deja prise", fenetre, "red")
                cc3=get_case(2)
                if cc3=="NULL":
                    return 0
                continue
            end = 1
        b2teau3.append(cc3)
        b2teau.append(cc3)
        place_point(2, cc3, fenetre, "./image/bataille_naval/point.png")
        cc31=get_case(2)
        if cc31=="NULL":
            return 0
        end = 0
        while end==0:
            if acote(cc3, cc31) == False:
                printt("choisissez a coté", fenetre, "red")
                cc31=get_case(2)
                if cc31=="NULL":
                    return 0
                continue
            if previsual(cc3, cc31, 2, b2teau) == False:
                printt("vous ne pouvez pas placer ici", fenetre, "red")
                cc31=get_case(2)
                if cc31=="NULL":
                    return 0
                continue
            if notdouble(cc31, b2teau, b2teau3) == False:
                printt("case deja prise", fenetre, "red")
                cc31=get_case(2)
                if cc31=="NULL":
                    return 0
                continue
            end = 1
        b2teau3.append(cc31)
        b2teau.append(cc31)
        place_point(2, cc31, fenetre, "./image/bataille_naval/point.png")
        cc32=get_case(2)
        if cc2=="NULL":
            return 0
        end = 0
        while end==0:
            if suite(cc3, cc31, cc32, 2) == False:
                printt("choisissez a coté", fenetre, "red")
                cc32=get_case(2)
                if cc2=="NULL":
                    return 0
                continue
            if notdouble(cc32, b2teau, b2teau3) == False:
                printt("case deja prise", fenetre, "red")
                cc32=get_case(2)
                if cc2=="NULL":
                    return 0
                continue
            end = 1
        b2teau3.append(cc32)
        b2teau.append(cc32)
        place_point(2, cc32, fenetre, "./image/bataille_naval/point.png")
        b2teauc3 = copie_bateau(b2teau3)
        place_line(2, b2teauc3, fenetre)



        printt("2e BATEAU DE 3", fenetre, "black")
        cc33=get_case(2)
        if cc33=="NULL":
            return 0
        end = 0
        while end==0:
            if previsual(cc33, 0, 2, b2teau) == False:
                printt("vous ne pouvez pas placer ici", fenetre, "red")
                cc33=get_case(2)
                if cc33=="NULL":
                    return 0
                continue
            if notdouble(cc33, b2teau, b2teau33) == False:
                printt("case deja prise", fenetre, "red")
                cc33=get_case(2)
                if cc33=="NULL":
                    return 0
                continue
            end = 1
        b2teau33.append(cc33)
        b2teau.append(cc33)
        place_point(2, cc33, fenetre, "./image/bataille_naval/point.png")
        cc331=get_case(2)
        if cc331=="NULL":
            return 0
        end = 0
        while end==0:
            if acote(cc33, cc331) == False:
                printt("choisissez a coté", fenetre, "red")
                cc331=get_case(2)
                if cc331=="NULL":
                    return 0
                continue
            if previsual(cc33, cc331, 2, b2teau) == False:
                printt("vous ne pouvez pas placer ici", fenetre, "red")
                cc331=get_case(2)
                if cc331=="NULL":
                    return 0
                continue
            if notdouble(cc331, b2teau, b2teau33) == False:
                printt("case deja prise", fenetre, "red")
                cc331=get_case(2)
                if cc331=="NULL":
                    return 0
                continue
            end = 1
        b2teau33.append(cc331)
        b2teau.append(cc331)
        place_point(2, cc331, fenetre, "./image/bataille_naval/point.png")
        cc332=get_case(2)
        if cc332=="NULL":
            return 0
        end = 0
        while end==0:
            if suite(cc33, cc331, cc332, 2) == False:
                printt("choisissez a coté", fenetre, "red")
                cc332=get_case(2)
                if cc332=="NULL":
                    return 0
                continue
            if notdouble(cc332, b2teau, b2teau33) == False:
                printt("case deja prise", fenetre, "red")
                cc332=get_case(2)
                if cc32=="NULL":
                    return 0
                continue
            end = 1
        b2teau33.append(cc332)
        b2teau.append(cc332)
        place_point(2, cc332, fenetre, "./image/bataille_naval/point.png")
        b2teauc33 = copie_bateau(b2teau33)
        place_line(2, b2teauc33, fenetre)


        printt("BATEAU DE 4", fenetre, "black")
        cc4=get_case(2)
        if cc4=="NULL":
            return 0
        end = 0
        while end==0:
            if previsual(cc4, 0, 3, b2teau) == False:
                printt("vous ne pouvez pas placer ici", fenetre, "red")
                cc4=get_case(2)
                if cc4=="NULL":
                    return 0
                continue
            if notdouble(cc4, b2teau, b2teau4) == False:
                printt("case deja prise", fenetre, "red")
                cc4=get_case(2)
                if cc4=="NULL":
                    return 0
                continue
            end = 1
        b2teau4.append(cc4)
        b2teau.append(cc4)
        place_point(2, cc4, fenetre, "./image/bataille_naval/point.png")
        cc41=get_case(2)
        if cc41=="NULL":
            return 0
        end = 0
        while end==0:
            if acote(cc4, cc41) == False:
                printt("choisissez a coté", fenetre, "red")
                cc41=get_case(2)
                if cc41=="NULL":
                    return 0
                continue
            if previsual(cc4, cc41, 3, b2teau) == False:
                printt("vous ne pouvez pas placer ici", fenetre, "red")
                cc41=get_case(2)
                if cc41=="NULL":
                    return 0
                continue
            if notdouble(cc41, b2teau, b2teau4) == False:
                printt("case deja prise", fenetre, "red")
                cc41=get_case(2)
                if cc41=="NULL":
                    return 0
                continue
            end = 1
        b2teau4.append(cc41)
        b2teau.append(cc41)
        place_point(2, cc41, fenetre, "./image/bataille_naval/point.png")
        cc42=get_case(2)
        if cc42=="NULL":
            return 0
        end = 0
        while end==0:
            if suite(cc4, cc41, cc42, 2) == False:
                printt("choisissez a coté", fenetre, "red")
                cc42=get_case(2)
                if cc42=="NULL":
                    return 0
                continue
            if notdouble(cc42, b2teau, b2teau4) == False:
                printt("case deja prise", fenetre, "red")
                cc42=get_case(2)
                if cc42=="NULL":
                    return 0
                continue
            end = 1
        b2teau4.append(cc42)
        b2teau.append(cc42)
        place_point(2, cc42, fenetre, "./image/bataille_naval/point.png")
        cc43=get_case(2)
        if cc43=="NULL":
            return 0
        end = 0
        while end==0:
            if suite(cc4, cc42, cc43, 3) == False:
                printt("choisissez a coté", fenetre, "red")
                cc43=get_case(2)
                if cc43=="NULL":
                    return 0
                continue
            if notdouble(cc43, b2teau, b2teau4) == False:
                printt("case deja prise", fenetre, "red")
                cc43=get_case(2)
                if cc43=="NULL":
                    return 0
                continue
            end = 1
        b2teau4.append(cc43)
        b2teau.append(cc43)
        place_point(2, cc43, fenetre, "./image/bataille_naval/point.png")
        b2teauc4 = copie_bateau(b2teau4)
        place_line(2, b2teauc4, fenetre)


        printt("BATEAU DE 5", fenetre, "black")
        cc5=get_case(2)
        if cc5=="NULL":
            return 0
        end = 0
        while end==0:
            if previsual(cc5, 0, 4, b2teau) == False:
                printt("vous ne pouvez pas placer ici", fenetre, "red")
                cc5=get_case(2)
                if cc5=="NULL":
                    return 0
                continue
            if notdouble(cc5, b2teau, b2teau5) == False:
                printt("case deja prise", fenetre, "red")
                cc5=get_case(2)
                if cc5=="NULL":
                    return 0
                continue
            end = 1
        b2teau5.append(cc5)
        b2teau.append(cc5)
        place_point(2, cc5, fenetre, "./image/bataille_naval/point.png")
        cc51=get_case(2)
        if cc51=="NULL":
            return 0
        end = 0
        while end==0:
            if acote(cc5, cc51) == False:
                printt("choisissez a coté", fenetre, "red")
                cc51=get_case(2)
                if cc51=="NULL":
                    return 0
                continue
            if previsual(cc5, cc51, 4, b2teau) == False:
                printt("vous ne pouvez pas placer ici", fenetre, "red")
                cc51=get_case(2)
                if cc51=="NULL":
                    return 0
                continue
            if notdouble(cc51, b2teau, b2teau5) == False:
                printt("case deja prise", fenetre, "red")
                cc51=get_case(2)
                if cc51=="NULL":
                    return 0
                continue
            end = 1
        b2teau5.append(cc51)
        b2teau.append(cc51)
        place_point(2, cc51, fenetre, "./image/bataille_naval/point.png")
        cc52=get_case(2)
        if cc52=="NULL":
            return 0
        end = 0
        while end==0:
            if suite(cc5, cc51, cc52, 2) == False:
                printt("choisissez a coté", fenetre, "red")
                cc52=get_case(2)
                if cc52=="NULL":
                    return 0
                continue
            if notdouble(cc52, b2teau, b2teau5) == False:
                printt("case deja prise", fenetre, "red")
                cc52=get_case(2)
                if cc52=="NULL":
                    return 0
                continue
            end = 1
        b2teau5.append(cc52)
        b2teau.append(cc52)
        place_point(2, cc52, fenetre, "./image/bataille_naval/point.png")
        cc53=get_case(2)
        if cc53=="NULL":
            return 0
        end = 0
        while end==0:
            if suite(cc5, cc52, cc53, 3) == False:
                printt("choisissez a coté", fenetre, "red")
                cc53=get_case(2)
                if cc53=="NULL":
                    return 0
                continue
            if notdouble(cc53, b2teau, b2teau5) == False:
                printt("case deja prise", fenetre, "red")
                cc53=get_case(2)
                if cc53=="NULL":
                    return 0
                continue
            end = 1
        b2teau5.append(cc53)
        b2teau.append(cc53)
        place_point(2, cc53, fenetre, "./image/bataille_naval/point.png")
        cc54=get_case(2)
        if cc54=="NULL":
            return 0
        suite(cc5, cc53, cc54, 4)
        notdouble(cc54, b2teau, b2teau5)
        end = 0
        while end==0:
            if suite(cc5, cc53, cc54, 4) == False:
                printt("choisissez a coté", fenetre, "red")
                cc54=get_case(2)
                if cc54=="NULL":
                    return 0
                continue
            if notdouble(cc54, b2teau, b2teau5) == False:
                printt("case deja prise", fenetre, "red")
                cc54=get_case(2)
                if cc54=="NULL":
                    return 0
                continue
            end = 1
        b2teau5.append(cc54)
        b2teau.append(cc54)
        place_point(2, cc54, fenetre, "./image/bataille_naval/point.png")
        b2teauc5 = copie_bateau(b2teau5)
        place_line(2, b2teauc5, fenetre)


        bille = pygame.image.load("./image/bataille_naval/grille4.png").convert_alpha()
        bille = pygame.transform.scale(bille, (1000, 600))
        position_bille = [0, 0] 
        fenetre.blit(bille, position_bille)
        pygame.display.flip()

        police = pygame.font.Font(None, 44)
        texte = police.render("Joueur 1",True,pygame.Color("yellow"))
        rectTexte = texte.get_rect()
        fenetre.blit(texte, (10, 100))
        pygame.display.flip()

        police = pygame.font.Font(None, 44)
        texte = police.render("Joueur 2",True,pygame.Color("orange"))
        rectTexte = texte.get_rect()
        fenetre.blit(texte, (870, 100))
        pygame.display.flip()


        end = 0
        kijou = 1
        while(end==0):
            if kijou == 1:
                printt("Au joueur 2 de tirer", fenetre, "gold")
                tir = get_case(1)
                if tir in bateau:
                
                    if tir in bateau5 and coule5 > 0:
                        coule5 -= 1
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        del bateau5[bateau5.index(tir)]
                    elif tir in bateau5 and coule5==0:
                        del bateau5[bateau5.index(tir)]
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        place_ship(kijou, bateauc5, fenetre)
                        #end += 1

                    if tir in bateau4 and coule4 > 0:
                        coule4 -= 1
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        del bateau4[bateau4.index(tir)]
                    elif tir in bateau4 and coule4==0:
                        del bateau4[bateau4.index(tir)]
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        place_ship(kijou, bateauc4, fenetre)
                        #end += 1

                    if tir in bateau33 and coule33 > 0:
                        coule33 -= 1
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        del bateau33[bateau33.index(tir)]
                    elif tir in bateau33 and coule33==0:
                        del bateau33[bateau33.index(tir)]
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        place_ship(kijou, bateauc33, fenetre)
                        #end += 1

                    if tir in bateau3 and coule3 > 0:
                        coule3 -= 1
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        del bateau3[bateau3.index(tir)]
                    elif tir in bateau3 and coule3==0:
                        del bateau3[bateau3.index(tir)]
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        place_ship(kijou, bateauc3, fenetre)
                        #end += 1
                        
                    if tir in bateau2 and coule2 > 0:
                        coule2 -= 1
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        del bateau2[bateau2.index(tir)]
                    elif tir in bateau2 and coule2==0:
                        del bateau2[bateau2.index(tir)]
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        place_ship(kijou, bateauc2, fenetre)
                        #end += 1
                        
                    if tir in bateau1:
                        del bateau1[bateau1.index(tir)]
                        place_point(1, tir, fenetre, "./image/bataille_naval/touche.png")
                        place_ship(kijou, bateauc1, fenetre)
                        #end += 1

                    if len(bateau1) == 0 and len(bateau2) == 0 and len(bateau3) == 0 and len(bateau33) == 0 and len(bateau4) == 0 and len(bateau5) == 0:
                        printt("Victoire du joueur 2", fenetre, "green")
                        end += 1
                        if len(b2teau1) !=0:
                            place_Rship(2, b2teauc1, fenetre)
                        if len(b2teau2) !=0:
                            place_Rship(2, b2teauc2, fenetre)
                        if len(b2teau3) !=0:
                            place_Rship(2, b2teauc3, fenetre)
                        if len(b2teau33) !=0:
                            place_Rship(2, b2teauc33, fenetre)
                        if len(b2teau4) !=0:
                            place_Rship(2, b2teauc4, fenetre)
                        if len(b2teau5) !=0:
                            place_Rship(2, b2teauc5, fenetre)
                        bille = pygame.image.load("./image/bataille_naval/rejouer.png").convert_alpha()
                        bille = pygame.transform.scale(bille, (40, 40))
                        position_bille = [10,10] 
                        fenetre.blit(bille, position_bille)
                        pygame.display.flip()
                        
                        
                else:
                    place_point(kijou, tir, fenetre, "./image/bataille_naval/cross.png")
                    kijou = 2



            else:
                printt("Au joueur 1 de tirer", fenetre, "orange")
                tir = get_case(2)
                if tir in b2teau:
                        
                    if tir in b2teau5 and cou2e5 > 0:
                        cou2e5 -= 1
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        del b2teau5[b2teau5.index(tir)]
                    elif tir in b2teau5 and cou2e5==0:
                        del b2teau5[b2teau5.index(tir)]
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        place_ship(kijou, b2teauc5, fenetre)
                            

                    if tir in b2teau4 and cou2e4 > 0:
                        cou2e4 -= 1
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        del b2teau4[b2teau4.index(tir)]
                    elif tir in b2teau4 and cou2e4==0:
                        del b2teau4[b2teau4.index(tir)]
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        place_ship(kijou, b2teauc4, fenetre)
                            

                    if tir in b2teau33 and cou2e33 > 0:
                        cou2e33 -= 1
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        del b2teau33[b2teau33.index(tir)]
                    elif tir in b2teau33 and cou2e33==0:
                        del b2teau33[b2teau33.index(tir)]
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        place_ship(kijou, b2teauc33, fenetre)
                        

                    if tir in b2teau3 and cou2e3 > 0:
                        cou2e3 -= 1
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        del b2teau3[b2teau3.index(tir)]
                    elif tir in b2teau3 and cou2e3==0:
                        del b2teau3[b2teau3.index(tir)]
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        place_ship(kijou, b2teauc3, fenetre)
                            
                            
                    if tir in b2teau2 and cou2e2 > 0:
                        cou2e2 -= 1
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        del b2teau2[b2teau2.index(tir)]
                    elif tir in b2teau2 and cou2e2==0:
                        del b2teau2[b2teau2.index(tir)]
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        place_ship(kijou, b2teauc2, fenetre)
                            
                            
                    if tir in b2teau1:
                        del b2teau1[b2teau1.index(tir)]
                        place_point(kijou, tir, fenetre, "./image/bataille_naval/touche.png")
                        place_ship(kijou, b2teauc1, fenetre)
                        

                    if len(b2teau1) == 0 and len(b2teau2) == 0 and len(b2teau3) == 0 and len(b2teau33) == 0 and len(b2teau4) == 0 and len(b2teau5) == 0:
                        printt("Victoire du joueur 1", fenetre, "green")
                        end += 1
                        if len(bateau1) !=0:
                            place_Rship(1, bateauc1, fenetre)
                        if len(bateau2) !=0:
                            place_Rship(1, bateauc2, fenetre)
                        if len(bateau3) !=0:
                            place_Rship(1, bateauc3, fenetre)
                        if len(bateau33) !=0:
                            place_Rship(1, bateauc33, fenetre)
                        if len(bateau4) !=0:
                            place_Rship(1, bateauc4, fenetre)
                        if len(bateau5) !=0:
                            place_Rship(1, bateauc5, fenetre)
                        bille = pygame.image.load("./image/bataille_naval/rejouer.png").convert_alpha()
                        bille = pygame.transform.scale(bille, (40, 40))
                        position_bille = [10,10] 
                        fenetre.blit(bille, position_bille)
                        pygame.display.flip()
                            
                            
                else:
                    place_point(kijou, tir, fenetre, "./image/bataille_naval/cross.png")
                    kijou = 1
                

        end = 0
        while end==0:
            pygame.init()
            for event in pygame.event.get():
                if(event.type == QUIT): 
                        return 0
                if (event.type == MOUSEBUTTONUP):
                    x = event.pos[0]
                    y = event.pos[1]
                    if y > 10 and y < 50 and x > 10 and x < 50:
                        end = 1




            
    