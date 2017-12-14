import pygame as py
from ..helper.screen_base import ScreenBase
from .enemy import enemy
from src.helper.drawer import Drawer

class Minigame_3(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.enemy_is_spawned = True
        self.groundcolor = (240, 230, 140)
        self.skycolor = (20, 20, 255)
        self.player()
        self.enemy_image = py.image.load("resources/graphics/minigame_3/testimage.png")
        self.enemy_location = enemy.get_location(self)
        self.enemy_rect = py.Rect(self.enemy_location, [100, 100])
        self.groundrect = py.Rect([0, 250], [1280, 720])
        self.skyrect = py.Rect([0, 0], [1280, 250])

        self.spawn_event = py.USEREVENT + 1
        self.enemy_move_down = self.enemy_rect.move_ip(0, 10)
        self.time_between_movement = 100
        self.time_between_spawn = 3000


    def player(self):
        self.loadchar = py.image.load("resources/graphics/minigame_3/testimage.png")
        self.char_rect = self.loadchar.get_rect()
        self.player_rect = py.Rect([640, 650], [100,100])

    def on_events(self, events):
        for event in events:
            if event.type == self.spawn_event:
                self.enemy_is_spawned = True
                self.selected_location = enemy.get_location(self)
                self.enemy_rect.x = self.selected_location[0]
                self.enemy_rect.y = self.selected_location[1]
                py.time.set_timer(self.enemy_move_down, self.time_between_movement)
                py.time.set_timer(self.spawn_event, self.time_between_spawn)

    def on_update(self):
        return

    def on_render(self):
        self.game.drawer.draw_canvas()
        py.draw.rect(self.game.py_screen, self.groundcolor, self.groundrect)
        py.draw.rect(self.game.py_screen, self.skycolor, self.skyrect)
        self.game.py_screen.blit(self.loadchar, self.player_rect)

        if self.enemy_is_spawned == True:
            py.draw.rect(self.game.py_screen, [0, 0, 0], self.enemy_rect)
            self.game.py_screen.blit(self.enemy_image, self.enemy_rect)
        py.display.update()

    def handle_mouse_input(self, mouse):
        return

    def handle_key_input(self, keys):
        if keys[py.K_a]:
            self.player_rect.move_ip(-10, 0)
        elif keys[py.K_d]:
            self.player_rect.move_ip(10, 0)
        elif keys[py.K_w]:
            self.player_rect.move_ip(0, -10)
        elif keys[py.K_s]:
            self.player_rect.move_ip(0, 10)
        return

    def handle_mouse_position(self, mouse_position):
        return