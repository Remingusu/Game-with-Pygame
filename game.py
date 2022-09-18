import pygame
from player import Player
from monster import Monster
from monster import Mummy
from monster import Alien
from comet_event import CometFallEvent


# class lancement jeu
class Game:
    def __init__(self):
        self.pressed = {}
        # def si jeu commence
        self.is_playing = False
        # charger player
        self.all_players = pygame.sprite.Group()
        # générer event
        self.comet_event = CometFallEvent(self)
        # groupe de monstre
        self.all_monsters = pygame.sprite.Group()

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)
        self.player = Player(self)
        self.all_players.add(self.player)

    def game_over(self):
        # remettre le jeu à neuf (retirer monstres, remettre pv au max, mettre jeu attente
        self.comet_event.reset_percent()
        self.all_monsters = pygame.sprite.Group()
        self.all_players = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.is_playing = False

    def update_(self, screen):
        # set player
        screen.blit(self.player.image, self.player.rect)
        # set groupe projectiles
        self.player.all_projectiles.draw(screen)
        # set groupe monstres
        self.all_monsters.draw(screen)
        # set comètes
        self.comet_event.all_comets.draw(screen)
        # update jauge vie joueur + animation
        self.player.update_player(screen)
        # update bar event jeu
        self.comet_event.update_bar(screen)
        # récupérer projectiles joueur
        for projectile in self.player.all_projectiles:
            projectile.move()
        # déplacer monstres + update jauge vie + animation
        for monsters in self.all_monsters:
            monsters.forward()
            monsters.update_monster(screen)
        # chute de comètes
        for comet in self.comet_event.all_comets:
            comet.fall()
        # verif si joueur aller gauche ou droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def spawn_monster(self, monster_name):
        self.all_monsters.add(monster_name.__call__(self))

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
