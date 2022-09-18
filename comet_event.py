import pygame
from comet import Comet


# créer class event interval régulier
class CometFallEvent:
    # créer compteur
    def __init__(self, game):
        self.game = game
        self.percent = 0
        self.percent_speed = 5
        # def groupe comètes
        self.all_comets = pygame.sprite.Group()
        self.fall_mode = False

    def add_percent(self):
        self.percent += self.percent_speed/100

    def reset_percent(self):
        self.percent = 0

    def is_full_loaded(self):
        return self.percent >= 100

    def meteor_fall(self):
        # boucle valeur 1 - 10
        for i in range(1, 10):
            # spawn 1 comète
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # jauge est plaine
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()
            self.fall_mode = True

    def update_bar(self, surface):
        # ajouter pourcentage
        self.add_percent()
        # barre grise arrière-plan
        pygame.draw.rect(surface, (50, 50, 50), [0, surface.get_height()-10, surface.get_width(), 10])
        # barre rouge actualiser
        pygame.draw.rect(surface, (250, 0, 0), [0, surface.get_height()-10, (surface.get_width()/100)*self.percent, 10])
