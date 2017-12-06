from src.helper.checkbox import CheckBox
from src.helper.image_button import ImageButton
from src.helper.label import Label
from src.helper.screen_base import ScreenBase

import pygame as py


class Options(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.mouse_position = None
        self.btn = []
        game.drawer.add_background_image("resources/graphics/main_menu_background.png")
        self.btn.append(OptionsButton(game.py_screen, "Back"))
        self.title = OptionsLabel(game.py_screen, "Options", 75)
        self.resolution_label = OptionsLabel(game.py_screen, "Resolution :", 50)
        self.full_screen_label = OptionsLabel(game.py_screen, "Full Screen :", 50)
        self.full_screen_checkbox = CheckBox(game.py_screen, [0, 0, 0], 50, self.game.FULLSCREEN, 2, [254, 0, 0])

    def handle_key_input(self, keys):
        pass

    def handle_mouse_input(self, event):
        pass

    def handle_mouse_position(self, mouse_position):
        self.mouse_position = mouse_position

    def on_events(self, events):
        for event in events:
            if event.type == py.MOUSEBUTTONDOWN:
                if self.btn[0].is_clicked(self.mouse_position):
                    self.back_to_main_menu()
                elif self.full_screen_checkbox.is_clicked(self.mouse_position):
                    self.toggle_fullscreen()

    def on_render(self):
        self.game.drawer.draw_canvas()
        screen_center_width = self.game.py_screen.get_width() / 2
        title_x = screen_center_width - (self.title.get_width() / 2)
        button_x = screen_center_width - (self.btn[0].width / 2)
        options_label_right = screen_center_width - 70

        self.title.render(title_x, 80)
        self.resolution_label.render(y=180, right=options_label_right)
        self.full_screen_label.render(y=260, right=options_label_right)
        self.full_screen_checkbox.render(self.mouse_position, options_label_right + 20, 265)
        self.btn[0].render(self.mouse_position, button_x, 600)
        py.display.update()

    def on_update(self):
        pass

    def back_to_main_menu(self):
        from src.global_screens.main_menu import MainMenu
        self.game.drawer.clear()
        MainMenu(self.game)

    def toggle_fullscreen(self):
        is_checked = self.full_screen_checkbox.is_checked
        if is_checked:
            self.full_screen_checkbox.is_checked = False
            self.game.py_screen = py.display.set_mode([self.game.config.width, self.game.config.height])
            self.game.FULLSCREEN = False
        else:
            self.full_screen_checkbox.is_checked = True
            self.game.py_screen = py.display.set_mode([self.game.config.width, self.game.config.height], py.FULLSCREEN)
            self.game.FULLSCREEN = True
        pass


class OptionsButton(ImageButton):
    def __init__(self, screen, text):
        button_file = "resources/graphics/button_background.png"
        text_color = [0, 0, 0]
        text_color_hover = [255, 255, 255]
        text_size = 45
        button_width = 300
        button_height = 70
        super().__init__(screen, button_file, text, text_color, text_color_hover, text_size,
                         button_width, button_height)


class OptionsLabel(Label):
    def __init__(self, screen, text, size):
        color = [0, 0, 0]
        font = "resources/fonts/Carnevalee Freakshow.ttf"
        super().__init__(screen, text, color, size, font)

    def render(self, x=None, y=None, right=None):
        if right is None:
            super().render(x, y)
        else:
            font = py.font.Font(self.font, self.size)
            text = font.render(self.text, True, self.color)
            text_rect = text.get_rect(y=y, right=right)
            self.screen.blit(text, text_rect)

