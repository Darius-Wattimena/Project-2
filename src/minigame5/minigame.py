import pygame as py
from ..helper.screen_base import ScreenBase
from .Target import Target
from random import *

class Minigame_5(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.game.drawer.clear()

        # Define background and buildings
        self.background_img = py.image.load("resources/graphics/minigame_5/background.png")
        self.building_exterior_img = py.image.load("resources/graphics/minigame_5/building_exterior.png")
        self.building_interior_img = py.image.load("resources/graphics/minigame_5/building_interior.png")

        # Define target
        self.target_img = py.image.load("resources/graphics/minigame_5/target.png")
        self.spawn_location = Target.random_location(self)
        self.target_rect = py.Rect(self.spawn_location, [40, 70])
        py.draw.rect(self.game.py_screen, [0, 0, 0], self.target_rect)

        # Define crosshair
        self.crosshair_img = py.image.load("resources/graphics/minigame_5/crosshair_white_and_red_40.png")
        self.crosshair_x = 640
        self.crosshair_y = 360
        self.crosshair_speed = 30
        self.crosshair_rect = py.Rect([self.crosshair_x, self.crosshair_y], [40, 40])

        # Define events
        self.spawn_event = py.USEREVENT + 1
        self.spawn_time = 3000
        py.time.set_timer(self.spawn_event, self.spawn_time)

        self.game_end_event = py.USEREVENT + 2
        self.game_time = 10000
        py.time.set_timer(self.game_end_event, self.game_time)

    def on_events(self, events):
        return

    def on_update(self):
        for e in py.event.get():
            if e.type == self.game_end_event:
                py.QUIT()
        return

    def on_render(self):
        self.game.drawer.draw_canvas()
        self.game.py_screen.blit(self.background_img, [0, 0])
        self.game.py_screen.blit(self.building_interior_img, [0, 0])

        for e in py.event.get():
            if e.type == self.spawn_event:
                self.selected_location = Target.random_location(self)
                self.target_rect.x = self.selected_location[0]
                self.target_rect.y = self.selected_location[1]
                py.time.set_timer(self.spawn_event, self.spawn_time)


        py.draw.rect(self.game.py_screen, [0, 0, 0], self.target_rect)
        self.game.py_screen.blit(self.target_img, self.target_rect)

        self.game.py_screen.blit(self.building_exterior_img, [0, 0])

        # Draws crosshair, clamps it to screen, sets it's collision
        self.game.py_screen.blit(self.crosshair_img, self.crosshair_rect)
        self.crosshair_rect.clamp_ip(self.game.py_screen.get_rect())
        # todo self.crosshair_rect.colliderect()

        py.display.update()

    def handle_mouse_input(self, mouse):
        return

    def handle_key_input(self, keys):
        py.key.set_repeat(1, 1)
        if keys[py.K_w]:
            self.crosshair_rect.move_ip(0, -self.crosshair_speed)
        elif keys[py.K_a]:
            self.crosshair_rect.move_ip(-self.crosshair_speed, 0)
        elif keys[py.K_s]:
            self.crosshair_rect.move_ip(0, +self.crosshair_speed)
        elif keys[py.K_d]:
            self.crosshair_rect.move_ip(+self.crosshair_speed, 0)
        return

    def handle_mouse_position(self, mouse_position):
        return