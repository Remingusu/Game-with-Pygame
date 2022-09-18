import pygame
import random
from monster import Mummy
from monster import Alien


# créer comète
class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event):
        super().__init__()
        self.comet_event = comet_event
        self.velocity = 0.4 * random.randint(5, 12)
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(1, 888)
        self.rect.y = - random.randint(0, 667)

    def remove(self):
        # supp bdf
        self.comet_event.all_comets.remove(self)
        # verif si aucunes comètes
        if len(self.comet_event.all_comets) == 0 and self.comet_event.game.is_playing:
            # remettre bar à zéro
            self.comet_event.reset_percent()
            # apparaitre 2 monstres
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster(Mummy)
            self.comet_event.game.spawn_monster(Alien)

    def fall(self):
        self.rect.y += self.velocity
        # tombe sur le sol
        if self.rect.y >= 500:
            # retirer bdf
            self.remove()

        # verif si bdf touche jouer
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            # infliger 20 dégâts
            self.comet_event.game.player.damage(20)
            self.remove()
