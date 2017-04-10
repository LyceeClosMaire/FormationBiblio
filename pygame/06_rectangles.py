import pygame
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode( (800,600) )


# on peut récupérer un Rect de bonne dimension à partir d'une surface :
winrect = window.get_rect()


image = pygame.image.load("p1_stand.png")
# lorsqu'on récupère le Rect d'une image, on peut lui indiquer la position (pas la
# taille) souhaitée :
rightrect = image.get_rect(right = 800)
# ceci est encore plus puissant si l'on utilise un autre Rect pour récupérer les
# coordonnées souhaitées, ainsi voici comment obtenir un Rect des dimensions de
# image mais centré sur la fenêtre :
centerrect = image.get_rect(center = winrect.center)


# un exemple de positionnement de texte :
# pour dessiner du texte, il faut charger la police
font = pygame.font.SysFont("Comic Sans MS", 20)
# puis dessiner une string dans sa propre image, antialiasée (True) et en
# couleur bleue
text = font.render( "Ceci est du texte !!", True, (0,0,255) )
# on veut placer ce texte à 100 pixels du bas de la fenêtre, centré
# on commence par récupérer un rectangle de bonne taille centré en bas de fenêtre
textrect = text.get_rect(midbottom = winrect.midbottom)
# puis on le remonte de 100 pixels avec move_ip() (ip = in place, modifiant le Rect
# plutôt que d'en créer un nouveau ajusté)
textrect.move_ip(0,-100)


running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT or(event.type == KEYUP and event.key == K_ESCAPE):
            running = False

    window.fill( (0,0,0) )

    # il est possible de remplir seulement une partie d'une Surface en utilisant
    # un Rect comme deuxième argument.
    # ici j'utilise inflate() pour obtenir un rectangle de même centre mais réduit
    # de 50 pixels en largeur et 100 en hauteur.
    window.fill( (255,0,0) , winrect.inflate(-50,-100) )

    # voyez comment on peut utiliser des Rect pour positionner nos images
    window.blit(image, rightrect)
    window.blit(image, centerrect)
    window.blit(text, textrect)

    pygame.display.flip()

pygame.quit()
