from ..minigame_base import MinigameBase
import pygame as py

class Minigame_1(MinigameBase):

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

    def handle_mouse_down(self, event):
        return

    def handle_mouse_up(self, event):
        return

    def handle_keyboard_down(self, event):
        return

    def handle_keyboard_up(self, event):
        return
