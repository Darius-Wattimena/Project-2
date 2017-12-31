import pygame as py


class Animation:
    def __init__(self, py_screen, image, animation_count, width, height):
        self.py_screen = py_screen
        self.image = image
        self.rect = py.Rect([0, 0], [width, height])
        self.animation_count = animation_count
        self.current_animation = 1
        self.width = width
        self.height = height
        self.scopes = []

    def add_scope(self, x, y):
        self.scopes.append([x, y])

    def on_render(self, location):
        if self.current_animation > self.animation_count:
            self.current_animation = 1
        animation_index = self.current_animation - 1
        self.rect.x = self.scopes[animation_index][0]
        self.rect.y = self.scopes[animation_index][1]
        self.py_screen.blit(self.image, location, self.rect)
        self.current_animation += 1

    def on_old_render(self, location):
        if self.current_animation > self.animation_count:
            self.current_animation = 1
        animation_index = self.current_animation - 1
        self.rect.x = self.scopes[animation_index][0]
        self.rect.y = self.scopes[animation_index][1]
        self.py_screen.blit(self.image, location, self.rect)
