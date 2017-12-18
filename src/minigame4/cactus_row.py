from random import randint
import pygame as py

from src.minigame4.cactus import Cactus


class CactusRow:
    def __init__(self, screen, cactus_images):
        self.items = []
        self.x = screen.get_width()
        self.cactus_width = 100
        self.cactus_height = 100
        self.row_speed = 1
        self.cactus_images = cactus_images
        self.screen = screen
        self.rect = py.Rect([self.x, 0], [self.cactus_width, screen.get_height()])

    # Hier maken we de row met cactusen aan. Hier bepalen we ook welke cactusen waar spawnen en hoeveel
    def create_row(self):
        # TODO spawn meerdere cactusen

        random_integer = randint(1, 13)
        random_cactus_image_index = randint(1, 3)
        random_cactus_image_index -= 1
        random_cactus_image = self.cactus_images[random_cactus_image_index]

        cactus_spawn_map = [
            0,
            40,
            60,
            100,
            160,
            220,
            280,
            340,
            380,
            500,
            520,
            640,
            680
        ]
        random_index = random_integer - 1
        cactus_y = cactus_spawn_map[random_index]
        cactus = Cactus(self.screen, self.x, cactus_y, self.cactus_width, self.cactus_height, random_cactus_image)
        self.items.append(cactus)

    def move_row_left(self):
        new_x = self.x
        for cactus in self.items:
            cactus.move_cactus_left(self.row_speed)
            new_x = cactus.x
        self.x = new_x
        self.rect.x = new_x

    # Render alle cactusen van de row naar het scherm
    def render(self):
        for cactus in self.items:
            cactus.render()