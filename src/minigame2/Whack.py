from random import randint

import pygame as py
import os.path as path

from src.helper.label import Label
from src.helper.screen_base import ScreenBase
from src.minigame1.fight import PauseScreenButton
from src.minigame1.ui.header_label import HeaderLabel
from src.minigame1.ui.text_label import TextLabel
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
        self.lives = 1
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
        self.StartGame = False
        self.PointsLabel.text = "Points: " + str(self.points)
        self.LivesLabel.text = "Lives: " + str(self.lives)
        self.EndGame = False
        self.EndGameLabel = Label(self.game.py_screen, "", [0, 0, 0], 50)
        self.highscore = 0
        self.NewHighscore = False
        self.ScoreLabel = Label(self.game.py_screen, "", [0,0,0], 50)
        self.HighscoreLabel = Label(self.game.py_screen, "", [0,0,0], 50)

        if path.isfile("highscores.txt"):
            self.highscore = self.get_highscore()
        else:
            self.set_highscore()

        self.dark_surface = py.Surface((1280, 720))
        self.dark_surface.set_alpha(170)

        self.objective_text = ["Game Objective",
                               "Use your mouse to click and defeat the Indians!",
                               "Hitting an indian grants you 1 point,",
                               "while hitting a cowboy loses you a life."]
        self.objective_label_header = HeaderLabel(self.game.py_screen, self.objective_text[0])
        self.objective_label_text_1 = TextLabel(self.game.py_screen, self.objective_text[1])
        self.objective_label_text_2 = TextLabel(self.game.py_screen, self.objective_text[2])
        self.objective_label_text_3 = TextLabel(self.game.py_screen, self.objective_text[3])

        self.controls_text = ["Controls",
                              "Move your mouse around and use Left Click"
                              "to hit the targets!"]

        self.controls_label_header = HeaderLabel(self.game.py_screen, self.controls_text[0])
        self.controls_label_text_1 = TextLabel(self.game.py_screen, self.controls_text[1])

        self.btn = []
        self.btn.append(PauseScreenButton(game.py_screen, "Start new game"))
        self.btn.append(PauseScreenButton(game.py_screen, "Back to menu"))
        self.btn.append(PauseScreenButton(game.py_screen, "Restart"))


        screen_center_width = self.game.py_screen.get_width() / 2
        self.button_x = screen_center_width - (self.btn[0].width / 2)



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
            if event.type == py.MOUSEBUTTONDOWN:
                self.game.logger.info(str(self.mouse_position) + " " + str(self.btn.__len__()))
                if self.btn[0].is_clicked(self.mouse_position):
                    self.__init__(self.game)
                    self.StartGame = True
                    self.EndGame = False
                elif self.btn[1].is_clicked(self.mouse_position):
                    from src.global_screens.pick_minigame import PickMinigame
                    self.game.drawer.clear()
                    PickMinigame(self.game)
        return

    def updatePlayerPoints(self):
        self.ShowHitLabel = True
        self.points += 1
        self.PointsLabel.text = "Points: " + str(self.points)
        self.rect = None

    def updatePlayerLives(self):
        self.ShowLivesLostLabel = True
        if self.lives >0:
            self.lives -= 1
            if self.lives == 0:
                self.EndGameLabel.text = "You are dead!"
                self.ScoreLabel.text = "Points: " + str(self.points)
                self.EndGame = True
                self.game.logger.info("points: " + str(self.points))
        self.LivesLabel.text = "Lives: " + str(self.lives)
        self.rect = None

    def on_update(self):
        self.passed_time += self.game.clock.get_time()
        return

    def on_render(self):
        if self.StartGame:
            self.game.drawer.draw_canvas()
            if self.EndGame:
                self.EndGameLabel.render(520, 250)
                if self.points > self.get_highscore():
                    self.set_highscore()
                    self.NewHighscore = True

                if self.NewHighscore:
                    self.HighscoreLabel.text = "You've beaten the previous Highscore! " + "New Highscore: " + str(self.points)
                    self.HighscoreLabel.render(200, 300)
                else:
                    self.HighscoreLabel.text = "Current Highscore: " + str(self.highscore)
                    self.ScoreLabel.render(520, 300)

                self.btn[1].render(self.mouse_position, self.button_x, 640)
                self.btn[0].render(self.mouse_position, self.button_x, 560)
                py.display.update()
                return

            if self.passed_time > self.get_speed_in_miliseconds():
                self.passed_time = 0
                self.location = Indian.get_location(self)
                self.change_color()
                self.setNewTarget(False)
                self.ShowHitLabel = False
                self.ShowLivesLostLabel = False
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

        else:
            self.game.drawer.draw_canvas()
            # Draw an dark surface on the screen
            self.game.py_screen.blit(self.dark_surface, [0, 0])

            # Draw objective
            self.objective_label_header.render(465, 190)
            self.objective_label_text_1.render(465, 240)
            self.objective_label_text_2.render(465, 260)
            self.objective_label_text_3.render(465, 280)

            # Draw controlls
            self.controls_label_header.render(465, 320)
            self.controls_label_text_1.render(465, 370)

            self.btn[1].render(self.mouse_position, self.button_x, 640)
            self.btn[0].render(self.mouse_position, self.button_x, 560)

        py.display.update()

    def handle_mouse_input(self, mouse):
        return

    def handle_key_input(self, keys):
        if self.EndGame == True:
            if keys[py.K_ESCAPE]:
                return
                #todo
            if keys[py.K_r]:
                self.__init__(self.game) #bad practice! but it works

        return

    def handle_mouse_position(self, mouse_position):
        self.mouse_position = mouse_position
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
        if self.points > 10:
            return 1000
        if self.points > 25:
            return 500
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

    def set_highscore(self):
        with open("highscores.txt", "w") as file:
            file.write(str(self.points))

    def get_highscore(self):
        with open("highscores.txt", "r") as file:
            data = file.read()
            if data != "":
                return int(data)
            else:
                return 0
