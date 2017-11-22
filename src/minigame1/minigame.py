from ..helper.screen_base import ScreenBase
from ..helper.game_object import GameObject
from ..helper.game_object_group import GameObjectGroup
from .fight import Fight
import pygame as py


class Minigame_1(ScreenBase):
    # TODO add help screen here for now just start the fight screen.
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.start_fight()

    def start_fight(self):
        Fight(self.game)

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
