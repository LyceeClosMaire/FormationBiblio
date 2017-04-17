import pygame
import random
from pygame.locals import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, position, speed):
        super().__init__()

        self.speed = speed
        self.rect = pygame.rect.Rect( (0,0), (50,50) )
        self.rect.center = position
        self.image = pygame.Surface( (50,50), SRCALPHA )
        self.image.fill( (0,0,0,0) )
        pygame.draw.circle(self.image, (255,0,0), (25,25), 25)

    def update(self):
        self.rect.move_ip(self.speed)

class Player(pygame.sprite.Sprite):
    def __init__(self, position):
        super().__init__()

        self.speed = (0,0)
        self.image = pygame.image.load("p1_stand.png")
        self.rect = self.image.get_rect(center=position)

    def update(self):
        self.rect.move_ip(self.speed)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode( (800,600) )
winrect = window.get_rect()

player = Player(winrect.center)

# un groupe peut être créé vide ou contenant déjà des sprites
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

    # générons des balles au hasard
    if random.randint(1,5) == 1:
        # on ajoute la balle (dont la position et la vitesse sont aléatoires)
        # au groupe sans jamais lui donner de nom de variable
        balls.add( Ball( (random.randint(100,700), 0)
                        , (random.randint(-10,10), random.randint(1,10)) ) )

    player.update()
    # tous les sprites dans balls seront mis à jour
    balls.update()

    # vérifions si le joueur a été touché et supprimons la balle responsable (le True)
    if pygame.sprite.spritecollide(player, balls, True):
        score = score + 1
        print("Touché", score, "fois !")

    window.fill( (0,0,0) )

    player.draw(window)
    # toutes les balles peuvent être dessinées en un seul appel de méthode
    balls.draw(window)

    pygame.display.flip()

pygame.quit()