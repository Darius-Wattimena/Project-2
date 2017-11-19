from ..helper.screen_base import ScreenBase
from src.game import Game
from .fight import Fight
import pygame as py

class Minigame_1(ScreenBase):

    def __init__(self):
        self.game = Game.Instance()
        self.game.set_screen(self)
        self.minigame_screen = Fight()
        self.game.drawer.add_image("resources/graphics/pygame_tiny.png")
        self.game.drawer.add_image("resources/graphics/1327.jpg")    

    def on_events(self, events):


        return

    def on_update(self):
        return

    def on_render(self):
        self.game.drawer.draw_canvas()
        py.display.update()

    def handle_mouse_input(self, mouse):
        return

    def handle_key_input(self, keys):
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
