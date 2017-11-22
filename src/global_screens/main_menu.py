from ..helper.screen_base import ScreenBase
from ..minigame1.minigame import Minigame_1
from ..helper.button import Button
from ..helper.label import Label
import pygame as py


class MainMenu(ScreenBase):
    def __init__(self, game):
        self.game = game
        game.drawer.add_background_image("resources/graphics/main_menu_background.png")
        self.title = Label(game.py_screen, "Game Title", [0, 0, 0], 75)
        self.btn_1 = MainMenuButton(game.py_screen, "Minigame 1")
        self.btn_2 = MainMenuButton(game.py_screen, "Minigame 2")
        self.btn_3 = MainMenuButton(game.py_screen, "Minigame 3")
        self.btn_4 = MainMenuButton(game.py_screen, "Minigame 4")
        self.btn_5 = MainMenuButton(game.py_screen, "Minigame 5")
        self.btn_6 = MainMenuButton(game.py_screen, "Quit")

    def on_events(self, events):
        for event in events:
            if event.type == py.MOUSEBUTTONDOWN:
                if self.btn_1.is_clicked(self.mouse_position):
                    self.start_minigame_1()
                elif self.btn_2.is_clicked(self.mouse_position):
                    self.start_minigame_2()
                elif self.btn_3.is_clicked(self.mouse_position):
                    self.start_minigame_3()
                elif self.btn_4.is_clicked(self.mouse_position):
                    self.start_minigame_4()
                elif self.btn_5.is_clicked(self.mouse_position):
                    self.start_minigame_5()
                elif self.btn_6.is_clicked(self.mouse_position):
                    self.game.quit()

        return

    def on_update(self):
        return

    def on_render(self):
        self.game.drawer.draw_canvas()
        screen_center_width = self.game.py_screen.get_width() / 2
        title_x = screen_center_width - (self.title.get_width() / 2)
        button_x = screen_center_width - (self.btn_1.width / 2)

        self.title.render(title_x, 80)
        self.btn_1.render(self.mouse_position, button_x, 180)
        self.btn_2.render(self.mouse_position, button_x, 260)
        self.btn_3.render(self.mouse_position, button_x, 340)
        self.btn_4.render(self.mouse_position, button_x, 420)
        self.btn_5.render(self.mouse_position, button_x, 500)
        self.btn_6.render(self.mouse_position, button_x, 600)
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
            1: self.start_minigame_1,
            2: self.start_minigame_2,
            3: self.start_minigame_3,
            4: self.start_minigame_4,
            5: self.start_minigame_5,
        }
        minigames_dict[number]()

    def start_minigame_1(self):
        self.game.drawer.clear()
        Minigame_1(self.game)

    def start_minigame_2(self):
        pass

    def start_minigame_3(self):
        pass

    def start_minigame_4(self):
        pass

    def start_minigame_5(self):
        pass


class MainMenuButton(Button):
    def __init__(self, screen, text):
        button_color = [144, 144, 144]
        button_color_hover = [57, 57, 57]
        text_color = [0, 0, 0]
        text_color_hover = [255, 255, 255]
        text_size = 50
        button_width = 300
        button_height = 70
        super().__init__(screen, text, button_color, button_color_hover, text_color, text_color_hover, text_size,
                         button_width, button_height)
