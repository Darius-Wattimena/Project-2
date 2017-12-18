from src.helper.image_button import ImageButton
from src.helper.screen_base import ScreenBase
from src.helper.label import Label
import pygame as py


class MainMenu(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.mouse_position = None
        game.drawer.add_background_image("resources/graphics/main_menu_background.png")
        self.title = Label(game.py_screen, "Game Title", [0, 0, 0], 75, "resources/fonts/Carnevalee Freakshow.ttf")
        self.btn = []
        self.btn.append(MainMenuButton(game.py_screen, "Start"))
        self.btn.append(MainMenuButton(game.py_screen, "Options"))
        self.btn.append(MainMenuButton(game.py_screen, "Quit"))

    def handle_mouse_position(self, mouse_position):
        self.mouse_position = mouse_position

    def handle_mouse_input(self, event):
        pass

    def on_render(self):
        self.game.drawer.draw_canvas()
        screen_center_width = self.game.py_screen.get_width() / 2
        title_x = screen_center_width - (self.title.get_width() / 2)
        button_x = screen_center_width - (self.btn[0].width / 2)

        self.title.render(title_x, 80)
        self.btn[0].render(self.mouse_position, button_x, 180)
        self.btn[1].render(self.mouse_position, button_x, 260)
        self.btn[2].render(self.mouse_position, button_x, 600)
        py.display.update()

    def handle_key_input(self, keys):
        return

    def on_events(self, events):
        for event in events:
            if event.type == py.MOUSEBUTTONDOWN:
                if self.btn[0].is_clicked(self.mouse_position):
                    self.show_pick_minigame()
                elif self.btn[1].is_clicked(self.mouse_position):
                    self.show_options()
                elif self.btn[2].is_clicked(self.mouse_position):
                    self.game.quit()

    def on_update(self):
        pass

    def show_pick_minigame(self):
        from src.global_screens.pick_minigame import PickMinigame
        self.game.drawer.clear()
        PickMinigame(self.game)

    def show_options(self):
        from src.global_screens.options import Options
        self.game.drawer.clear()
        Options(self.game)

class MainMenuButton(ImageButton):
    def __init__(self, screen, text):
        button_file = "resources/graphics/button_background_v3.png"
        text_color = [0, 0, 0]
        text_color_hover = [225, 225, 225]
        text_size = 45
        button_width = 350
        button_height = 70
        super().__init__(screen, button_file, text, text_color, text_color_hover, text_size,
                         button_width, button_height)