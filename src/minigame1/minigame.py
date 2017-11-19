from ..minigame_base import MinigameBase
from .fight import Fight
import pygame as py

class Minigame_1(MinigameBase):

    def __init__(self, game):
        super(Minigame_1, self)
        self.minigame_screen = Fight()

    def handle_mouse_input(self, event):
        return

    def handle_keyboard_input(self, keys):
        image = self.game.drawer.items[1]
        if keys[py.K_a]:
            image.move(-1, 0)
        if keys[py.K_d]:
            image.move(1, 0)
        if keys[py.K_w]:
            image.move(0, -1)
        if keys[py.K_s]:
            image.move(0, 1)

        return

    def handle_mouse_position(self, mouse_position):
        return

    def on_event(self, event):
        return

    def update(self):
        return

    def render(self):
        return
