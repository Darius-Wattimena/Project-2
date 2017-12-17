import pygame as py


class Cactus:
    def __init__(self, screen, x, y, width, height, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen
        self.rect = py.Rect([x, y], [width, height])
        self.image = image

    # Move the rectangle of the cactus to the left
    def move_cactus_left(self, movement):
        self.rect.move_ip(-movement, 0)
        self.x = self.rect.x

    # Render a single cactus to the screen
    def render(self):
        self.screen.blit(self.image, self.rect)
