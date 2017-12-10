""" Drawer module """
import pygame as py
from .image import Image
from .singleton import Singleton


@Singleton
class Drawer():
    """ Drawer class used when drawing an image to the screen """

    def __init__(self):
        self.items = []
        self.game_object_items = []
        self.screen = None

    def set_screen(self, screen):
        self.screen = screen

    def add_loaded_image(self, image, rect):
        image = Image(image, rect)
        self.items.append(image)

    def add_image(self, name):
        """ Add a new image to the items list """
        data = self.load_image(name)
        rect = data.get_rect()
        image = Image(data, rect)

        self.items.append(image)

    def add_background_image(self, name):
        data = self.load_image(name)
        data = py.transform.scale(data, (self.screen.get_width(), self.screen.get_height()))
        rect = data.get_rect()
        image = Image(data, rect)

        self.items.append(image)

    def add_game_object(self, name, game_object):
        """" Use this to load static things that do not move like a wall or a fence """
        data = self.load_image(name)
        rect = data.get_rect()
        game_object.set_rect(rect)
        self.game_object_items.append(game_object)

    def draw_canvas(self):
        """ Make the screen empty so we can add new images on the screen """
        self.screen.fill((0, 0, 0))  # RGB
        for item in self.items:
            self.screen.blit(item.data, item.rect)

        for item in self.game_object_items:
            self.screen.blit(item.data, item.rect)

    def load_image(self, file):
        """ loads an image, prepares it for play """
        try:
            surface = py.image.load(file)
        except py.error:
            raise SystemExit('Could not load image "%s" %s' % (file, py.get_error()))
        return surface.convert()

    def clear(self):
        self.items = []
