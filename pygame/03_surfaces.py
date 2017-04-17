import pygame
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

# window est du type Surface(), on peut donc utiliser blit(), fill() sur window
# et donc "dessiner sur l'écran" (attention cela se fait en réalité en mémoire, il
# faut appeler flip() pour que cela devienne visible)
window = pygame.display.set_mode( (800,600) )

# vous pouvez chargez n'importe quel fichier image, les png sont recommandés comme
# format (car ils gèrent bien la transparence)
image = pygame.image.load("p1_stand.png")

running = True
while running:
    clock.tick(60)

    # ATTENTION à l'ordre dans lequel vous manipulez window, commencez par le fond
    # puis dessinez par dessus sinon vous recouvrirez vos images par votre fond
    window.fill( (255,0,0) )

    # blit() permet de recopier une Surface dans une autre Surface à n'importe quelles
    # coordonnées (attention l'axe des ordonnées est orienté vers le bas et l'origine
    # est dans le coin en haut à gauche)
    window.blit( image, (10,10) )


    # il est possible de dessiner des formes géométriques simples avec pygame.draw :
    # comme un cercle sur window de couleur bleue, de centre (150,70)
    # et de rayon 50 (le 0 est l'épaisseur du bord, 0 déclenche le remplissement)
    pygame.draw.circle(window, (0,0,255), (150,70), 50, 0)

    # les transformations sont dans pygame.transform :
    # il est souvent utile de refléter une image horizontalement (autrement dit
    # autour de l'axe des ordonnées) :
    symetricH = pygame.transform.flip( image, True, False)
    window.blit( symetricH, (210,10) )
    # ou verticalement (autrement dit autour de l'axe des abscisses) :
    symetricV = pygame.transform.flip( image, False, True)
    window.blit( symetricV, (310,10) )
    # ou les deux :
    symetricVH = pygame.transform.flip( image, True, True)
    window.blit( symetricVH, (410,10) )

    # une autre opération très utile est la mise à l'échelle :
    # smoothscale permet de transformer les dimensions d'une image
    # commençons par récupérer les dimensions de notre image d'origine
    (width, height) = image.get_size()
    # attention les dimensions doivent être un nombre _entier_ de pixel donc // plutôt que /
    smaller = pygame.transform.smoothscale( image, (width // 2, height // 2) )
    bigger = pygame.transform.smoothscale( image, (width * 2, height * 2) )
    # on peut également utiliser des dimensions arbitraires
    squashed = pygame.transform.smoothscale( image, (100, 50) )
    window.blit( smaller, (10, 200) )
    window.blit( bigger, (60, 200) )
    window.blit( squashed, (260, 200) )
    # il existe une fonction scale() mais le résultat est moins bon et smoothscale()
    # est généralement accélérée par le matériel donc n'utilisez que smoothscale()
    bigger2 = pygame.transform.scale( image, (width * 2, height * 2) )
    window.blit( bigger2, (400, 200) )

    # il est également possible de faire tourner une image dans le sens direct
    # d'un certain angle (en degrés) ou de combiner mise à l'échelle et rotation
    # avec rotozoom()
    rotated = pygame.transform.rotate( image, 45 )
    window.blit( rotated, (10, 400) )
    # le résultat de rotozoom() est de meilleure qualité (même si vous choisissez
    # une échelle de 1) donc n'utilisez rotate() que si la vitesse est primordiale
    rotated_and_zoomed = pygame.transform.rotozoom( image, 45, 1 )
    window.blit( rotated_and_zoomed, (110, 400) )


    # avec Surface vous avez également accès à la couleur de chaque pixel
    # on va modifier une copie de notre image d'origine
    grey_levels = image.copy()
    # on parcourt chaque pixel de la surface
    (xmax, ymax) = image.get_size()
    for x in range(xmax):
        for y in range(ymax):
            # on récupère les composantes rouge, verte, bleue et alpha (opacité) d'un
            # pixel comme des entiers entre 0 et 255
            (red, green, blue, alpha) = image.get_at( (x,y) )
            mean = (red + green + blue) / 3
            # si vous souhaitez réellement mettre une image en niveaux de gris,
            # il existe des formules plus sophistiquées
            grey_levels.set_at((x,y), (mean, mean, mean, alpha))
    # notez qu'opérer pixel par pixel est trop lent si l'on doit le faire à chaque tour
    # de boucle en temps réel
    window.blit(grey_levels, (10, 500) )


    pygame.display.flip()

    for event in pygame.event.get():

        if event.type == QUIT or(event.type == KEYUP and event.key == K_ESCAPE):
            running = False

pygame.quit()
