from src.helper.label import Label
from src.helper.screen_base import ScreenBase
import pygame as py






class Minigame_4(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.background_image = py.image.load("resources/graphics/minigame_4/background3.jpg")
        self.player_image = py.image.load("resources/graphics/minigame_4/hourse.jpg")
        self.background_image_rect = self.background_image.get_rect()
        x = self.game.py_screen.get_width() / 2
        y = self.game.py_screen.get_height() / 1.3
        self.player_rect = self.player_image.get_rect()

        # Defines CACTUS, based on cactus.py
        self.cactus_img = py.image.load("resources/graphics/minigame_4/cactus.png")
        self.cactus = Cactus
        self.selected_location = self.cactus.get_location()
        self.cactus_rect = py.Rect(self.selected_location, [45, 70])
        py.draw.rect(self.game.py_screen, [0, 0, 0], self.cactus_rect)

        self.player_x = 640
        self.player_y = 360
        self.player_speed = 30
        self.player_rect = py.Rect([self.player_x, self.player_y], [40, 40])

        self.time = 0
        self.timer_label = Label(self.game.py_screen, "", [254, 254, 254], 50)

    def handle_key_input(self, keys):
        if keys[py.K_w] and keys[py.K_s]:
            pass
        elif keys[py.K_w]:
            self.player_rect.move_ip(0, -self.player_speed)
        elif keys[py.K_s]:
                self.player_rect.move_ip(0, +self.player_speed)

        if keys[py.K_a] and keys[py.K_d]:
            pass
        elif keys[py.K_a]:
            self.player_rect.move_ip(-self.player_speed, 0)
        elif keys[py.K_d]:
            self.player_rect.move_ip(+self.player_speed, 0)

    def handle_mouse_input(self, event):
        pass

    def handle_mouse_position(self, mouse_position):
        pass

    def on_events(self, events):
        pass

    def on_update(self):
        self.time += 1
        self.timer_label.text = str(self.time)
        pass

    def on_render(self):
        self.game.drawer.draw_canvas()
        self.game.py_screen.blit(self.background_image, self.background_image_rect)
        self.game.py_screen.blit(self.player_image, self.player_rect)
        self.timer_label.render(500, 100)
        py.display.update()