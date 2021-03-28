import pygame


class Unbreakable(pygame.sprite.Sprite):

    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load("assets/unbreakable.png")
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos)
