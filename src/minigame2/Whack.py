from random import randint

import pygame as py

from src.helper.label import Label
from src.helper.screen_base import ScreenBase
from .Indian import Indian


class Whack(ScreenBase):

    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.game.drawer.clear()
        self.game.drawer.add_background_image("resources/graphics/minigame_2/background.jpg")
        self.points = 0
        self.indianImage = py.image.load("resources/graphics/minigame_2/rsz_indian.png")
        self.cowboyImage = py.image.load("resources/graphics/minigame_2/rsz_mccree.png")
        self.lives = 3
        self.DisplayNewIndian = True;
        self.passed_time = 0
        self.location = Indian.get_location(self)
        self.rect = self.indianImage.get_rect() #py.Rect(self.location, [100,100])
        self.rect.center = self.location
        self.mouse_position = None
        self.ShowIndian = True;
        self.color = [255, 0, 0]
        self.livesLostLabel = Label(self.game.py_screen, "Ouch!", [255,0,0], 40)
        self.hitLabel = Label(self.game.py_screen, "Hit!", [0,255,0], 40)
        self.ShowTimer = 30
        self.ShowHitLabel = False
        self.ShowLivesLostLabel = False
        self.LivesLabel = Label(self.game.py_screen, "", [0,0,255], 50)
        self.PointsLabel = Label(self.game.py_screen, "", [0, 0, 255], 50)
        self.PointsLabel.text = "Points: " + str(self.points)
        self.LivesLabel.text = "Lives: " + str(self.lives)
        self.EndGame = False
        self.EndGameLabel = Label(self.game.py_screen, "You are dead! " + "Points: " + str(self.points), [255, 255, 255], 50)



    def on_events(self, events):
        for event in events:
            if event.type == py.MOUSEBUTTONDOWN and event.button == 1:
                self.mouse_position = py.mouse.get_pos()
                if self.rect is not None:
                    if self.rect.collidepoint(self.mouse_position):
                        if self.ShowIndian:
                            self.updatePlayerPoints()
                        else:
                            self.updatePlayerLives()
                    else:
                        if self.lives > 0:
                            self.lives -= 1
                            if self.lives == 0:
                                self.EndGame = True;
                                self.game.logger.info("points: " + str(self.points))
        return

    def updatePlayerPoints(self):
        self.ShowHitLabel = True
        self.points += 1
        self.PointsLabel.text = "Points: " + str(self.points)
        self.rect = None

    def updatePlayerLives(self):
        self.ShowLivesLostLabel = True
        self.lives -= 1
        self.LivesLabel.text = "Lives: " + str(self.lives)
        self.rect = None

    def on_update(self):
        self.passed_time += self.game.clock.get_time()
        return

    def on_render(self):
        self.game.drawer.draw_canvas()
        if self.EndGame:
            self.EndGameLabel.render(500, 500)

        if self.passed_time > self.get_speed_in_miliseconds():
            self.passed_time = 0
            self.location = Indian.get_location(self)
            self.change_color()
            self.setNewTarget(False)
        elif self.rect is not None:
            self.setNewTarget(True)

        if self.ShowHitLabel:
            self.ShowTimer -= 1
            self.hitLabel.render(self.location[0], self.location[1])

        if self.ShowLivesLostLabel:
            self.ShowTimer -= 1
            self.livesLostLabel.render(self.location[0], self.location[1])

        if self.ShowTimer == 0:
            self.ShowHitLabel = False
            self.ShowLivesLostLabel = False
            self.ShowTimer = 30

        self.LivesLabel.render(900, 100)
        self.PointsLabel.render(900, 200)
        py.display.update()

    def handle_mouse_input(self, mouse):
        return

    def handle_key_input(self, keys):
        return

    def handle_mouse_position(self, mouse_position):
        return

    def setNewTarget(self, requiredBlit):
        if self.ShowIndian:
            if requiredBlit:
                self.game.py_screen.blit(self.indianImage, self.location)
            self.rect = self.indianImage.get_rect()
        else:
            if requiredBlit:
                self.game.py_screen.blit(self.cowboyImage, self.location)
            self.rect = self.cowboyImage.get_rect()

        self.rect.y = self.location[1]
        self.rect.x = self.location[0]
        return

    def display_Indian(self):
        if self.DisplayNewIndian is True:
            self.DisplayNewIndian = False
        elif self.DisplayNewIndian is False:
            self.DisplayNewIndian == True
        return

    def get_speed_in_miliseconds(self):
        if self.points > 3:
            return 1500
        return 3000

    def change_color(self):
        random_number = randint(1, 2)
        if random_number == 1:
            self.ShowIndian = False;
            self.color = [0, 255, 0]
        else:
            self.ShowIndian = True;
            self.color = [255, 0 ,0]
        return