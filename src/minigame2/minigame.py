import pygame as py

from src.helper.screen_base import ScreenBase
from src.minigame2.Whack import Whack


class Minigame_2(ScreenBase):

    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.start_whack()

    def start_whack(self):
        Whack(self.game)

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
        return

    def handle_mouse_position(self, mouse_position):
        return
        