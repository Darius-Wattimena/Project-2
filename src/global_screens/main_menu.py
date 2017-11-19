from ..helper.screen_base import ScreenBase
from ..minigame1.minigame import Minigame_1
from src.game import Game
import pygame as py

class MainMenu(ScreenBase):

    def __init__(self):
        self.game = Game.Instance()

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
        if keys[py.K_1]:
            self.start_minigame(1)

        return

    def handle_mouse_position(self, mouse_position):
        return

    def start_minigame(self, number):
        minigames_dict = {
            1 : self.start_minigame_1,
            2 : self.start_minigame_2,
            3 : self.start_minigame_3,
            4 : self.start_minigame_4,
            5 : self.start_minigame_5,
        }
        minigames_dict[number]()

    def start_minigame_1(self):
        self.screen = Minigame_1()

    def start_minigame_2(self):
        pass

    def start_minigame_3(self):
        pass

    def start_minigame_4(self):
        pass

    def start_minigame_5(self):
        pass
