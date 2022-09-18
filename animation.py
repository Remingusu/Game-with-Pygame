import pygame


# def class animation
class Animation(pygame.sprite.Sprite):
    def __init__(self, name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images_list = animation.get(name)
        self.animation_status = False

    # def méthode start animation
    def start_animation(self):
        self.animation_status = True

    # def méthode animée sprite
    def animate(self, loop=False):
        # verif si animation active
        if self.animation_status:
            # pass image suivante
            self.current_image += 1
            # verif si fin anim
            if self.current_image >= len(self.images_list):
                # remettre anim au départ
                self.current_image = 0
                # verif si pas boucle
                if loop is False:
                    # désactiver animation
                    self.animation_status = False
            # modif image courante → suivante
            self.image = self.images_list[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)


# def fonction charger images sprite
def load_animation(name):
    # charger images sprite
    images_dico = []
    # récup chemin dossier sprite
    path = f'assets/{name}/{name}'
    # boucler chaque image dans dossier
    for num in range(1, 24):
        images_path = path + str(num) + '.png'
        images_dico.append(pygame.image.load(images_path))
    # return list images
    return images_dico


# def dico contiendra images sprites
animation = {'mummy': load_animation('mummy'), 'player': load_animation('player'), 'alien': load_animation('alien')}
