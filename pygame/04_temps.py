import pygame
from pygame.locals import *

pygame.init()

# l'horloge doit être initialisée au début du jeu
clock = pygame.time.Clock()
# il est possible de déclencher un événement à intervalle régulier, utilisez
# USEREVENT + un nombre pour différencier ces événements :
# - un événement par seconde
pygame.time.set_timer(USEREVENT+1, 1000)
# - un événement toutes les 3 secondes
pygame.time.set_timer(USEREVENT+2, 3000)



window = pygame.display.set_mode( (800,600) )

# vous pouvez utilisez des variables pour savoir si certaines action ont déjà été
# exécutées (ou compter combien de fois elles l'ont été)
disabled_event = False

# il est possible de stocker un temps dans une variable
since = pygame.time.get_ticks()

running = True
while running:
    # tick(60) assure que la boucle sera exécutée au plus 60 fois par seconde, si
    # un tour de boucle a été trop rapide (moins d'1/60ème de seconde), elle bloque
    # jusqu'à ce que le temps soit écoulée
    clock.tick(60)

    for event in pygame.event.get():

        # les événements créés par set_timer() sont distingués par leur type :
        if event.type == USEREVENT+1:
            print("Chaque seconde !")
        if event.type == USEREVENT+2:
            print("Toutes les 3 secondes !")

        if event.type == QUIT or(event.type == KEYUP and event.key == K_ESCAPE):
            running = False


    # on peut utiliser le temps écoulé depuis le début du jeu
    if pygame.time.get_ticks() < 2000:
        # rouge pour les deux premières secondes
        window.fill( (255,0,0) )

    if pygame.time.get_ticks() - since > 1000:
        # met à jour la variable toutes les secondes
        since = pygame.time.get_ticks()

    if pygame.time.get_ticks() > 2000 and pygame.time.get_ticks() - since < 500:
        # vert pendant une demi-seconde
        window.fill( (0, 255, 0) )
    if pygame.time.get_ticks() > 2000 and pygame.time.get_ticks() - since > 500:
        # bleu pendant une demi-seconde
        window.fill( (0, 0, 255) )


    # après 10 secondes et une seule fois
    if disabled_event == False and pygame.time.get_ticks() > 10000:
        # assure que cette action ne sera pas exécutée une deuxième fois
        disabled_event = True
        # pour désactiver un événement périodique, utilisez set_timer() avec un délai de 0
        pygame.time.set_timer(USEREVENT+1, 0)
        print("Evénement désactivé.")

    pygame.display.flip()

pygame.quit()
