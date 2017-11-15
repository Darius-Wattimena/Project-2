""" Drawer module """
import pygame as py
from .image import Image

class Drawer:
    """ Drawer class used when drawing an image to the screen """   
    def __init__(self, screen):
        self.items = []
        self.screen = screen

    def addImage(self, name):
        """ Add a new image to the items list """
        data = py.image.load(name)
        rect = data.get_rect()
        image = Image(data, rect)

        self.items.append(image)

    def drawCanvas(self):
        """ Make the screen empty so we can add new images on the screen """
        self.screen.fill(0, 0, 0) # RGB
        for item in self.items:
            self.screen.blit(item.data, item.rect)            
