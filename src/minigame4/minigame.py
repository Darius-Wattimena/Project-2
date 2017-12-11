from src.helper.label import Label
from src.helper.screen_base import ScreenBase
import pygame as py


class Minigame_4(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.background_image = py.image.load("resources/graphics/minigame_4/background3.jpg")
        self.player_image = py.image.load("resources/graphics/minigame_4/player.jpg")
        self.background_image_rect = self.background_image.get_rect()
        x = self.game.py_screen.get_width() / 2
        y = self.game.py_screen.get_height() / 2
        self.player_rect = self.player_image.get_rect()
        self.player_rect.centerx = x
        self.player_rect.centery = y
        self.time = 1000000
        self.timer_label = Label(self.game.py_screen, "", [254, 254, 254], 50)

    def handle_key_input(self, keys):
        if keys[py.K_a]:
            self.background_image_rect.move_ip(5, 0)
        elif keys[py.K_d]:
            self.background_image_rect.move_ip(-5, 0)

    def handle_mouse_input(self, event):
        pass

    def handle_mouse_position(self, mouse_position):
        pass

    def on_events(self, events):
        pass

    def on_update(self):
        self.time -= 1
        self.timer_label.text = str(self.time)
        pass

    def on_render(self):
        self.game.drawer.draw_canvas()
        self.game.py_screen.blit(self.background_image, self.background_image_rect)
        self.game.py_screen.blit(self.player_image, self.player_rect)
        self.timer_label.render(100, 500)
        py.display.update()