import pygame
import animation


# créer classe du projectile
class Projectile(animation.Animation):
    # constructeur
    def __init__(self, player):
        super().__init__("projectile")
        self.velocity = 6.4
        self.player = player
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 128
        self.rect.y = player.rect.y + 97
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        # tourner projectile quand move
        self.angle += 3
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        # supprimer projectile en dehors de l'écran
        self.player.all_projectiles.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()
        # verif si projectile est absent de l'écran
        if self.rect.x > 1000:
            self.remove()
        # verif si projectile collision monstre
        for monster in self.player.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            # Infliger dégâts
            monster.damage(self.player.attack)
