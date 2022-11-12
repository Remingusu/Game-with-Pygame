import pygame
from game import Game
import math
pygame.init()

# gen la fenêtre
pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1000, 667))
# arrière-plan
background = pygame.image.load('assets/bg.jpg')
# bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4)
# bouton
button = pygame.image.load('assets/button.png')
button = pygame.transform.scale(button, (400, 150))
button_rect = button.get_rect()
button_rect.x = math.ceil(screen.get_width() / 3.24)
button_rect.y = math.ceil(screen.get_height() / 1.90)

# charger jeu
game = Game()
running = True
# boucle si True
while running:
    # set arrière-plan
    screen.blit(background, (0, -250))
    # verif si jeu commence
    if game.is_playing:
        # déclenche instructions parties
        game.update_(screen)
    # verif si jeu non commencer
    else:
        # add button
        screen.blit(button, button_rect)
        # add bannière
        screen.blit(banner, banner_rect)
    # update écran
    pygame.display.flip()
    # si joueur ferme fenêtre
    for event in pygame.event.get():
        # verif si fermeture
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        # detect si touche pressée
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
            # verif si "espace" appuyer
            if event.key == pygame.K_SPACE and game.is_playing:
                game.player.launch_projectile()
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # verif si souris collision avec bouton jouer
            if button_rect.collidepoint(event.pos) and game.is_playing == False:
                # lancer le jeu
                game.start()
    # fix fps sur clock
    pygame.time.Clock().tick(60)
