# on importe la librairie pygame
import pygame
# pour plus de clarté, on importe les constantes dans notre espace de nom
from pygame.locals import *

# on initialise pygame (système de son, polices, graphismes...)
pygame.init()

# on crée une fenêtre (ou un plein écran avec l'option FULLSCREEN)
# pygame a des sous parties comme display qui s'occupe de l'affichage
window = pygame.display.set_mode( (800,600) )

# une variable pour indiquer si le programme est en train de tourner
running = True
# la boucle principalequi tourne en permanence pour modifier l'affichage
# et gérer les évènements
while running:
    # ici on modifie l'affichage si nécessaire, par exemple en remplissant la
    # fenêtre d'une couleur unie (en rvb) :
    window.fill( (255,0,0) )

    # ATTENTION : par défaut pygame est en mode double buffer, ce qui veut dire
    # que toute vos manipulation de window sont uniquement faite en mémoire,
    # pour envoyer votre window modifiée sur l'écran il faut utiliser flip()
    pygame.display.flip()

    # à chaque tour de boucle, on inspecte les événements (clavier, souris, ...)
    for event in pygame.event.get(): # get() renvoie et vide la liste des événements

        # event.type indique le type d'événement :
        # - KEYDOWN : appui sur une touche
        # - KEYUP : relache d'une touche
        # ...
        # QUIT : un événement spécial émis par l'OS lorsque l'on clique sur la croix
        # ou l'on appuie sur Alt+F4 (sous Windows)
        if event.type == QUIT or(event.type == KEYUP and event.key == K_ESCAPE):
            # on met fin à la boucle
            running = False

# on arrête proprement les systèmes pygame (uniquement nécessaire si le programme
# n'est pas tout à fait fini)
pygame.quit()
