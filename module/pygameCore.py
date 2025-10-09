import pygame
import sys


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
    pos = [position[0], position[1]]

    if Alignement=="Left":
        pos = [position[0], position[1]]
    elif Alignement=="Center":
        pos = [position[0] - rect.width/2, position[1]]
    elif Alignement=="Right":
        pos = [position[0] - rect.width, position[1]]

    fenetre.blit(bille, pos)

    return rect

def printText(text, fontSize, color, position, fenetre, Alignement="Left", police=None, underline=False, Alignementy="Bottom"):
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


def get_pos():
    x=0
    y=0
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONUP):
                x = event.pos[0]
                y = event.pos[1]

        if (event.type == pygame.QUIT): 
                return "NULL", 0
    
    return x,y


def get_nom():
    fichier = open("./annexes/log.txt", "r")
    log = fichier.read()   
    fichier.close()
    nom = log.split(';')

    return nom[0], nom[1]