from random import randint

import pygame as py

from src.helper.screen_base import ScreenBase
from .Indian import Indian


class Whack(ScreenBase):

    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.game.drawer.clear()
        self.game.drawer.add_background_image("resources/graphics/minigame_2/background.jpg")
        self.points = 0
        self.lives = 1000
        self.DisplayNewIndian = True;
        self.passed_time = 0
        self.location = Indian.get_location(self)
        self.rect = py.Rect(self.location, [100,100])
        self.mouse_position = None
        self.color = [255, 0, 0]

        py.draw.rect(self.game.py_screen, [255, 0, 0], self.rect)


    def on_events(self, events):
        for event in events:
            if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                self.mouse_position = py.mouse.get_pos()
                self.game.logger.info(str(self.mouse_position) + " lives: " + str(self.lives) + " points: " + str(self.points))
                if self.rect != None:
                    if self.rect.collidepoint(self.mouse_position):
                        if self.color == [255, 0, 0]:
                            self.points += 1
                            self.rect = None
                        else:
                            self.lives -= 1
                            self.rect = None
                    else:
                        if self.lives > 0:
                            self.lives -= 1
                            if self.lives == 0:
                                self.points = 9999 #TODO engame
                                self.game.logger.info("points: " + str(self.points))

        return

    def on_update(self):
        self.passed_time += self.game.clock.get_time()
       # if self.lives == 0:

        return

    def on_render(self):
        self.game.drawer.draw_canvas()
        if self.passed_time > self.get_speed_in_miliseconds():
            self.passed_time = 0
            self.location = Indian.get_location(self)
            self.rect = py.Rect(self.location, [100, 100])
            self.change_color()
        if self.rect != None:
            py.draw.rect(self.game.py_screen, self.color, self.rect)

        py.display.update()

    def handle_mouse_input(self, mouse):
        return

    def handle_key_input(self, keys):
        return

    def handle_mouse_position(self, mouse_position):
        return

    def display_Indian(self):
        if self.DisplayNewIndian == True:
            self.DisplayNewIndian = False
        elif self.DisplayNewIndian == False:
            self.DisplayNewIndian == True
        return

    def get_speed_in_miliseconds(self):
        if self.points > 2:
            return 500
        return 3000

    def change_color(self):
        random_number = randint(1, 2)
        if random_number == 1:
            self.color = [0, 255, 0]
        else:
            self.color = [255, 0 ,0]
        return