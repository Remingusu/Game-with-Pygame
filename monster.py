import pygame
import random
import animation


# créer class du monstre
class Monster(animation.Animation):
    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.max_health = 100
        self.health = 100
        self.attack = 0.2

        self.rect = self.image.get_rect()
        self.rect.x = 925 + random.randint(0, 25)
        self.rect.y = 500 - offset
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = 0.4 * random.randint(1, speed)

    def damage(self, amount):
        # subir dégâts
        self.health -= amount
        # verif si pv <= 0
        if self.health <= 0:
            # Respawn comme new monstre
            self.velocity = 0.4 * random.randint(1, self.default_speed)
            self.rect.x = 925 + random.randint(0, 25)
            self.health = self.max_health
            # si barre is full
            if self.game.comet_event.is_full_loaded():
                # supp du jeu
                self.game.all_monsters.remove(self)
                # essayer déclenchée pluie
                self.game.comet_event.attempt_fall()

    def update_monster(self, surface):
        # dessiner arrière_plan
        pygame.draw.rect(surface, (50, 50, 50), [self.rect.x + 12, self.rect.y - 5, self.max_health, 4])
        # dessiner jauge vie
        pygame.draw.rect(surface, (0, 250, 0), [self.rect.x + 12, self.rect.y - 5, self.health, 4])
        # update animation
        self.animate(loop=True)

    def forward(self):
        # déplacement si pas de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        else:
            # Infliger dégât joueur
            self.game.player.damage(self.attack)


# def class momie
class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(6)


# def class alien
class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 141)
        self.max_health = 250
        self.health = 250
        self.attack = 0.8
        self.set_speed(1)
