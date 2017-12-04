import pygame as py
from ..helper.screen_base import ScreenBase

class Minigame_5(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)

        self.skycolor = (0, 0, 255)
        self.groundcolor = (240, 230, 140)
        self.targetcolor = (0, 0, 0)
        self.buildingcolor = (255, 255, 255)

        self.skyrect = py.Rect([0, 0], [1280, 720])
        self.groundrect = py.Rect([0, 250], [1280, 720])
        self.targetrect = py.Rect([200, 100], [200, 200])
        self.buildingrect = py.Rect([100, 100], [200, 300])

        self.crosshair = self.game.drawer.add_image("resources/graphics/minigame_5/59595-200.png")

    def on_events(self, events):
        return

    def on_update(self):
        return

    def on_render(self):
        self.game.drawer.draw_canvas()
        py.draw.rect(self.game.py_screen, self.skycolor, self.skyrect)
        py.draw.rect(self.game.py_screen, self.groundcolor, self.groundrect)
        py.draw.rect(self.game.py_screen, self.targetcolor, self.targetrect)
        py.draw.rect(self.game.py_screen, self.buildingcolor, self.buildingrect)
        py.draw.rect(self.game.py_screen, self.buildingcolor, self.buildingrect)
        py.display.update()

    def handle_mouse_input(self, mouse):
        return

    def handle_key_input(self, keys):
        return

    def handle_mouse_position(self, mouse_position):
        return
