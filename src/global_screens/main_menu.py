from ..helper.screen_base import ScreenBase
from ..minigame1.minigame import Minigame_1
from ..helper.button import Button
import pygame as py

class MainMenu(ScreenBase):

    def __init__(self, game):
        self.game = game
        self.minigame_1_button = Button(self.game.py_screen, "Minigame 1", [144,144,144], [57,57,57], [0, 0, 0], [255,255,255], 50)
        self.minigame_2_button = Button(self.game.py_screen, "Minigame 2", [144,144,144], [57,57,57], [0, 0, 0], [255,255,255], 50)
        self.minigame_3_button = Button(self.game.py_screen, "Minigame 3", [144,144,144], [57,57,57], [0, 0, 0], [255,255,255], 50)
        self.minigame_4_button = Button(self.game.py_screen, "Minigame 4", [144,144,144], [57,57,57], [0, 0, 0], [255,255,255], 50)
        self.minigame_5_button = Button(self.game.py_screen, "Minigame 5", [144,144,144], [57,57,57], [0, 0, 0], [255,255,255], 50)
        self.quit_button = Button(self.game.py_screen, "Quit", [144,144,144], [57,57,57], [0, 0, 0], [255,255,255], 50)

    def on_events(self, events):
        return

    def on_update(self):
        return

    def on_render(self):
        self.game.drawer.draw_canvas()
        self.minigame_1_button.render(self.mouse_position, [370, 100, 300, 70])
        self.minigame_2_button.render(self.mouse_position, [370, 200, 300, 70])
        self.minigame_3_button.render(self.mouse_position, [370, 300, 300, 70])
        self.minigame_4_button.render(self.mouse_position, [370, 400, 300, 70])
        self.minigame_5_button.render(self.mouse_position, [370, 500, 300, 70])
        py.display.update()

    def handle_mouse_input(self, mouse):
        return

    def handle_key_input(self, keys):
        if keys[py.K_1]:
            self.start_minigame(1)

        return

    def handle_mouse_position(self, mouse_position):
        self.mouse_position = mouse_position
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
        self.screen = Minigame_1(self.game)

    def start_minigame_2(self):
        pass

    def start_minigame_3(self):
        pass

    def start_minigame_4(self):
        pass

    def start_minigame_5(self):
        pass
