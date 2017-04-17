import pygame
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode( (800,600) )
winrect = window.get_rect()


# initialisation d'une image controllable par le joueur et de sa position
player = pygame.image.load("p1_stand.png")
playerRect = player.get_rect(center = winrect.center)


# image de l'objectif, construit à partir de 2 tuiles
door = pygame.Surface( (64,128) )
door.blit( pygame.image.load("doorRed_top.png"), (0,0) )
door.blit( pygame.image.load("doorRed_lock.png"), (0,64) )
doorRect = door.get_rect(bottom = playerRect.bottom, right = winrect.right - 50)
# rectangle autour de la porte, dépassant un peu pour détecter quand on est raisonnablement "sur" la porte
goal = doorRect.inflate(20,20)


# obstacle mouvant avec lequel le joueur pourra entrer en collision
block = pygame.image.load("blockBrown_broken.png")
blockRect = block.get_rect(bottom = winrect.bottom, centerx = 150)
blockSpeed = (0,-5)


running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT or(event.type == KEYUP and event.key == K_ESCAPE):
            running = False

        # en cas de clic gauche
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            # collidepoint() est très pratique pour détecter si un clic a été fait
            # dans une certaine zone
            if playerRect.collidepoint(event.pos):
                print("Clic sur le joueur.")
            if doorRect.collidepoint(event.pos):
                print("Clic sur la porte.")

    # il est possible de détecter si une touche est couramment enfoncée :
    keys = pygame.key.get_pressed()
    # si la flèche gauche est enfoncée et que le joueur n'est pas au bord de la fenêtre
    if keys[K_LEFT] and playerRect.left > 0:
        # on déplace le joueur vers la gauche
        playerRect.move_ip(-5,0)
    # notez comme on utilise les rectangles pour comparer les positions sans calculs
    if keys[K_RIGHT] and playerRect.right < winrect.right:
        playerRect.move_ip(5,0)

    # si le bloc sort de l'écran, on le renvoie dans l'autre sens
    if blockRect.top < 0:
        blockSpeed = (0,5)
    elif blockRect.bottom > winrect.bottom:
        blockSpeed = (0,-5)

    # move() et move_ip() peuvent prendre un couple en paramètre,
    # ce qui est très pratique pour traiter un vecteur vitesse
    blockRect.move_ip(blockSpeed)

    # si le joueur et le bloc sont en collision
    if playerRect.colliderect(blockRect):
        # on corrige la position du joueur
        if playerRect.centerx < blockRect.centerx: # le joueur est à gauche du bloc
            playerRect.right = blockRect.left
        else: # le joueur est à droite du bloc
            playerRect.left = blockRect.right

    # on peut tester si le joueur est "sur" la porte, prêt à y entrer
    if goal.contains(playerRect):
        running = False
        print("Victoire !!")

    window.fill( (0,0,0) )

    window.blit( door, doorRect )
    window.blit( block, blockRect )
    window.blit( player, playerRect )

    pygame.display.flip()

pygame.quit()
