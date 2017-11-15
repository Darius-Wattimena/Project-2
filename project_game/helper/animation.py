from .image import Image
import pygame

class Animation(pygame.sprite.Sprite):
    def __init__(self):
        self.images = []
        self.index = 0
        self.image = None
        self.rect = None

    def add_image(self, image: Image):
        self.images.append(image)
        if self.rect == None:
            self.rect = image.rect

    def update(self):
        self.index += 1
        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index].data        
    