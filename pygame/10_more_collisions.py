import pygame
import random
from pygame.locals import *


pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode( (800,600) )
winrect = window.get_rect()


# gestion simpliste des rebonds, une gestion correcte utiliserait la normale à la
# surface heurtée à la place
def rebound(speed, left_or_right, bottom_or_top):
    (x,y) = speed
    if left_or_right:
        x = -x
    if bottom_or_top:
        y = -y
    return (x,y)

# Encore un Sprite de balle, gérant cette fois-ci les rebonds contre les bords de
# l'écran, on crée également un masque pour affiner les collisions avec le joueur
class Ball(pygame.sprite.Sprite):
    def __init__(self, position, speed):
        super().__init__()

        self.speed = speed
        self.rect = pygame.rect.Rect( (0,0), (50,50) )
        self.rect.center = position
        self.image = pygame.Surface( (50,50), SRCALPHA )
        self.image.fill( (0,0,0,0) )
        pygame.draw.circle(self.image, (255,0,0), (25,25), 25)

        # si l'image contient des zones transparentes, cette fonction générera
        # un masque correct
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        # si la balle est en train de sortir de l'écran
        if not winrect.contains(self):
            rect = self.rect
            # on corrige le vecteur vitesse
            self.speed = rebound(self.speed
                                , winrect.left > rect.left or winrect.right < rect.right
                                , winrect.top > rect.top or winrect.bottom < rect.bottom )
        # de toute façon on déplace la balle du vecteur vitesse (éventuellement corrigé)
        self.rect.move_ip(self.speed)

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.speed = (0,0)
        self.image = pygame.image.load("p1_stand.png")
        self.rect = self.image.get_rect(center=position)
        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        if not winrect.contains(self):
            rect = self.rect
            self.speed = rebound(self.speed
                                , winrect.left > rect.left or winrect.right < rect.right
                                , winrect.top > rect.top or winrect.bottom < rect.bottom )
        self.rect.move_ip(self.speed)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


player = Player(winrect.center)
balls = pygame.sprite.Group()
score = 0

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT or(event.type == KEYUP and event.key == K_ESCAPE):
            running = False

        if event.type == KEYDOWN:
            if event.key == K_UP:
                player.speed = (0,-5)
            elif event.key == K_DOWN:
                player.speed = (0,5)
            elif event.key == K_LEFT:
                player.speed = (-5,0)
            elif event.key == K_RIGHT:
                player.speed = (5,0)

    if random.randint(1,100) == 1:
        balls.add( Ball( (winrect.centerx, 25)
                        , (random.randint(-10,10), random.randint(1,10)) ) )

    player.update()
    balls.update()

    # vérifions si le joueur a été touché et supprimons la balle responsable (le True)
    # le paramètre pygame.sprite.collide_mask indique comment les collisions seront
    # testée
    if pygame.sprite.spritecollide(player, balls, True, pygame.sprite.collide_mask):
        score = score + 1
        print("Touché", score, "fois !")

    window.fill( (0,0,0) )

    player.draw(window)
    balls.draw(window)

    pygame.display.flip()

pygame.quit()