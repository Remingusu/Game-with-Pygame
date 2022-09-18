import pygame
import animation
from projectile import Projectile


# créer classe joueur
class Player(animation.Animation):
    def __init__(self, game):
        super().__init__("player")
        self.game = game
        self.max_health = 100
        self.health = 100
        self.attack = 12
        self.velocity = 3.2
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 410
        self.rect.y = 460

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            # si jouer meurt
            self.game.game_over()

    def update_player(self, surface):
        # dessiner arrière_plan
        pygame.draw.rect(surface, (50, 50, 50), [self.rect.x + 50, self.rect.y + 25, self.max_health, 4])
        # dessiner jauge vie
        pygame.draw.rect(surface, (0, 250, 0), [self.rect.x + 50, self.rect.y + 25, self.health, 4])
        # update animation
        self.animate()

    def launch_projectile(self):
        # créer une instance du projectile
        self.all_projectiles.add(Projectile(self))
        # start animation lancer
        self.start_animation()

    def move_right(self):
        # si pas de collision
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
