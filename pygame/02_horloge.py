import pygame
from pygame.locals import *

pygame.init()

# on crée l'horloge qui garde trace du temps qui passe
clock = pygame.time.Clock()

window = pygame.display.set_mode( (800,600) )

running = True
while running:
    # cette fonction vérifie depuis combien de temps elle a été exécutée pour la
    # dernière fois et attend si ce temps était plus court qu'1/60ème de seconde
    clock.tick(60)

    window.fill( (255,0,0) )

    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == QUIT or(event.type == KEYUP and event.key == K_ESCAPE):
            running = False

pygame.quit()
