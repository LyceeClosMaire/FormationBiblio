import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode( (800,600) )

# on peut charger des sons pour les utiliser à tout moment
jingle = pygame.mixer.Sound("jingle_sncf.ogg")

# on peut charger _une_ musique (on peut en changer par la suite)
pygame.mixer.music.load("battement.ogg")
# on lance la musique (le premier argument est le nombre de répétition après la première,
# ici -1 est une valeur spéciale qui répète indéfiniment le morceau)
pygame.mixer.music.play(-1)


running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_p:
                # un son peut-être joué en même temps que la musique et les autres sons
                jingle.play()
            elif event.key == K_s:
                # on peut interrompre le son
                jingle.stop()

        if event.type == QUIT or(event.type == KEYUP and event.key == K_ESCAPE):
            running = False

    pygame.display.flip()

pygame.quit()
