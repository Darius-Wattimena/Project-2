from src.helper.image_button import ImageButton
from src.helper.screen_base import ScreenBase
from src.minigame1.minigame import Minigame_1
from src.minigame2.minigame import Minigame_2
from src.minigame3.minigame import Minigame_3
from src.minigame4.minigame import Minigame_4
from src.minigame5.minigame import Minigame_5
from src.helper.label import Label
import pygame as py


class PickMinigame(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        game.drawer.add_background_image("resources/graphics/main_menu_background.png")
        self.title = Label(game.py_screen, "Select a minigame!", [0, 0, 0], 75, "resources/fonts/Carnevalee Freakshow.ttf")
        self.btn = []
        self.btn.append(PickMinigameButton(game.py_screen, "Barfight!"))
        self.btn.append(PickMinigameButton(game.py_screen, "Whack an indian!"))
        self.btn.append(PickMinigameButton(game.py_screen, "Dodge Course!"))
        self.btn.append(PickMinigameButton(game.py_screen, "Horse Racing"))
        self.btn.append(PickMinigameButton(game.py_screen, "Shooting range"))
        self.btn.append(PickMinigameButton(game.py_screen, "Back"))
        self.mouse_position = None

    def on_events(self, events):
        for event in events:
            if event.type == py.MOUSEBUTTONDOWN:
                if self.btn[0].is_clicked(self.mouse_position):
                    self.start_minigame_1()
                elif self.btn[1].is_clicked(self.mouse_position):
                    self.start_minigame_2()
                elif self.btn[2].is_clicked(self.mouse_position):
                    self.start_minigame_3()
                elif self.btn[3].is_clicked(self.mouse_position):
                    self.start_minigame_4()
                elif self.btn[4].is_clicked(self.mouse_position):
                    self.start_minigame_5()
                elif self.btn[5].is_clicked(self.mouse_position):
                    self.back_to_main_menu()
        return

    def on_update(self):
        return

    def on_render(self):
        self.game.drawer.draw_canvas()
        screen_center_width = self.game.py_screen.get_width() / 2
        title_x = screen_center_width - (self.title.get_width() / 2)
        button_x = screen_center_width - (self.btn[0].width / 2)

        self.title.render(title_x, 80)
        self.btn[0].render(self.mouse_position, button_x, 180)
        self.btn[1].render(self.mouse_position, button_x, 260)
        self.btn[2].render(self.mouse_position, button_x, 340)
        self.btn[3].render(self.mouse_position, button_x, 420)
        self.btn[4].render(self.mouse_position, button_x, 500)
        self.btn[5].render(self.mouse_position, button_x, 600)
        py.display.update()

    def handle_mouse_input(self, mouse):
        return

    def handle_key_input(self, keys):
        return

    def handle_mouse_position(self, mouse_position):
        self.mouse_position = mouse_position

    def start_minigame_1(self):
        self.game.drawer.clear()
        Minigame_1(self.game)

    def start_minigame_2(self):
        self.game.drawer.clear()
        Minigame_2(self.game)

    def start_minigame_3(self):
        self.game.drawer.clear()
        Minigame_3(self.game)

    def start_minigame_4(self):
        self.game.drawer.clear()
        Minigame_4(self.game)

    def start_minigame_5(self):
        self.game.drawer.clear()
        Minigame_5(self.game)

    def back_to_main_menu(self):
        from src.global_screens.main_menu import MainMenu
        self.game.drawer.clear()
        MainMenu(self.game)


class PickMinigameButton(ImageButton):
    def __init__(self, screen, text):
        button_file = "resources/graphics/button_background.png"
        text_color = [0, 0, 0]
        text_color_hover = [255, 255, 255]
        text_size = 50
        button_width = 300
        button_height = 70
        super().__init__(screen, button_file, text, text_color, text_color_hover, text_size,
                         button_width, button_height)
