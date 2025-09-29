import pygame

def initScreen(size, title, color, iconPath):
    pygame.init()
    pygame.font.init()
    fenetre = pygame.display.set_mode(size)
    fenetre.fill(color)
    pygame.display.set_caption(title)
    pygame_icon = pygame.image.load(iconPath)
    pygame.display.set_icon(pygame_icon)

    return fenetre

def printImage(path, size, position, fenetre, rotation=0, Alignement="Left"):
    bille = pygame.image.load(path).convert_alpha()
    bille = pygame.transform.scale(bille, size)
    bille = pygame.transform.rotate(bille, rotation)
    rect = bille.get_rect()
    pos = [0,0]

    if Alignement=="Left":
        pos = [position[0], position[1]]
    elif Alignement=="Center":
        pos = [position[0] - rect.width/2, position[1]]
    elif Alignement=="Right":
        pos = [position[0] - rect.width, position[1]]

    position_bille = pos
    fenetre.blit(bille, position_bille)

    return rect

def printText(text, fontSize, color, position, fenetre, Alignement="Left", police=None, underline=False):
    if Alignement=="Left":
        police = pygame.font.Font(police, fontSize)
        police.underline = underline
        texte = police.render(text,True,color)
        fenetre.blit(texte, position)
    
    elif Alignement=="Center":
        police = pygame.font.Font(police, fontSize)
        police.underline = underline
        texte = police.render(text,True,color)
        rectTexte = texte.get_rect().width
        fenetre.blit(texte, (position[0] - rectTexte/2, position[1]))
    
    elif Alignement=="Right":
        police = pygame.font.Font(police, fontSize)
        police.underline = underline
        texte = police.render(text,True,color)
        rectTexte = texte.get_rect().width
        fenetre.blit(texte, (position[0] - rectTexte, position[1]))