import pygame
from pygame.locals import *

# les définitions de classes sont introduites par le mot clé class
# puis le nom de la classe, puis entre parenthèses la classe dont elle hérite
class Ball(pygame.sprite.Sprite):

    # la méthode __init__ (avec des doubles tirets bas des deux côtés) est très
    # importante, c'est celle qui est appelée lorsqu'on construit un objet de
    # la classe.
    # notez le premier paramètre, conventionnellement appelé "self" ("soi-même")
    # il désigne l'objet qu'on est en train de construire
    def __init__(self, position, speed):

        # lorsque l'on hérite d'une classe, il est préférable de commencer le constructeur
        # par un appel au constructeur de la classe parente que l'on retrouve avec super()
        super().__init__()

        # les attributs de l'objet (les données qui lui sont attachées) doivent
        # être initialisée, généralement dans __init__()

        self.speed = speed
        # rect est un attribut standard des Sprites, vous devez toujours l'initialiser
        # pour que vos sprites marchent correctement avec les fonctions de collision
        self.rect = pygame.rect.Rect( (0,0), (50,50) )
        self.rect.center = position
        # de même image est un attribut standard, utilisé par draw() sur un Group
        self.image = pygame.Surface( (50,50), SRCALPHA )
        self.image.fill( (0,0,0,0) )
        pygame.draw.circle(self.image, (255,0,0), (25,25), 25)


    # la méthode update() est celle qui sera appelée à chaque tour de boucle pour
    # mettre à jour l'état interne de votre Sprite qui est toujours le premier paramètre
    # de toute méthode (fonction attachée à un objet)
    def update(self):
        self.rect.move_ip(self.speed)


    # la méthode draw() sera appelée pour dessiner le sprite sur une surface
    def draw(self, surface):
        # voici ce que fait Group par défaut :
        surface.blit( self.image, self.rect )


# les définitions de classes ou fonctions se font généralement dans un module
# à part mais ici pour l'exemple tout est réuni dans un même programme
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode( (800,600) )
winrect = window.get_rect()


# il est possible de créer autant d'objets de la classe Ball que l'on souhaite
ball1 = Ball( (10,10), (3,3) )
ball2 = Ball( (500,500), (-1,-4) )


running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT or(event.type == KEYUP and event.key == K_ESCAPE):
            running = False

    # les Sprites doivent être mis à jour manuellement, ou par l'intermédiaire d'un
    # Group comme nous le verrons
    # Notez que le paramètre "self" n'est pas passé entre parenthèse mais automatiquement
    # à cause de la syntaxe objet.méthode()
    ball1.update()
    ball2.update()

    window.fill( (0,0,0) )

    # le détail du dessin peut être ignoré mais il nous faut encore dessiner les balles
    # une par une, Group palliera à ceci. Nous dessinons directement sur window.
    ball1.draw(window)
    ball2.draw(window)

    pygame.display.flip()

pygame.quit()