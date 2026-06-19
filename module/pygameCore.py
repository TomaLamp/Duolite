import pygame

def initScreen(size : tuple[int, int], title : str, color : str, iconPath : str) -> pygame.Surface:
    """Créé une fenetre avec comme parametre la taille, le titre, la couleur de fond et une icon"""

    pygame.init()
    pygame.font.init()
    fenetre = pygame.display.set_mode(size)
    fenetre.fill(color)
    pygame.display.set_caption(title)
    pygame_icon = pygame.image.load(iconPath)
    pygame.display.set_icon(pygame_icon)

    return fenetre

def printImage(path : str, size : tuple[int, int], position : tuple[int, int], fenetre : pygame.Surface, rotation : int = 0, Alignement : str = "Left") -> pygame.Rect:
    """
    Affiche une image sur une fenetre
    - path : chemin relatif de l'image
    - size : la taille de l'image (sizex, sizey)
    - position : la position de l'image (x,y)
    - fenetre : la fenetre sur laquelle afficher l'image
    - rotation : la rotation de l'image
    - Alignement : A partir d'oû la position x va mettre l'image, Left / Center / Right
    """

    bille = pygame.image.load(path).convert_alpha()
    bille = pygame.transform.scale(bille, size)
    bille = pygame.transform.rotate(bille, rotation)
    rect = bille.get_rect()
    pos = [position[0], position[1]]

    if Alignement=="Left":
        pos = [position[0], position[1]]
    elif Alignement=="Center":
        pos = [position[0] - rect.width/2, position[1]]
    elif Alignement=="Right":
        pos = [position[0] - rect.width, position[1]]

    fenetre.blit(bille, pos)

    return rect

def printText(text : str, fontSize : int, color : str, position : tuple[int, int], fenetre : pygame.Surface, Alignement : str = "Left", police : str = None, underline : bool = False, Alignementy : str = "Bottom") -> pygame.Rect:
    """
    Affiche un texte sur une fenetre
    - text : Le texte à afficher
    - fontsize : la taille de police du texte
    - color : la couleur du texte
    - position : la position de l'image (x,y)
    - fenetre : la fenetre sur laquelle afficher l'image
    - Alignement : A partir d'oû la position x va mettre l'image, Left / Center / Right
    - police : la police d'écriture du texte
    - underline : si le texte est souligné
    - Alignementy : : A partir d'oû la position y va mettre l'image, Top / Center / Bottom
    """

    police = pygame.font.Font(police, fontSize)
    police.underline = underline
    texte = police.render(text,True,color)
    rect = texte.get_rect()
    rectwidth = rect.width
    rectheight = rect.height
    x = position[0]
    y = position[1]
    
    if Alignement=="Center":
        x = position[0] - rectwidth/2
    elif Alignement=="Right":
        x = position[0] - rectwidth
    
    if Alignementy=="Center":
        y = position[1] - rectheight/2
    elif Alignementy=="Top":
        y = position[1] - rectheight

    fenetre.blit(texte, [x, y])

    return rect


def get_pos() -> int:
    """Retourne la position du clique de la souris"""

    x=0
    y=0
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONUP):
                x = event.pos[0]
                y = event.pos[1]

        if (event.type == pygame.QUIT): 
                return "NULL", 0
    
    return x,y


def get_nom() -> str:
    """Retourne les noms qui sont dans le fichiers log.txt"""
    
    fichier = open("./annexes/log.txt", "r")
    log = fichier.read()   
    fichier.close()
    nom = log.split(';')

    return nom[0], nom[1]