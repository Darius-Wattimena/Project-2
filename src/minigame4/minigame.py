from src.helper.label import Label
from src.helper.screen_base import ScreenBase
import pygame as py
import time
import logging

from src.minigame1.fight import PauseScreenButton
from src.minigame1.ui.header_label import HeaderLabel
from src.minigame1.ui.text_label import TextLabel
from src.minigame4.cactus import Cactus
from src.minigame4.cactus_row import CactusRow


class Minigame_4(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.background_image = py.image.load("resources/graphics/minigame_4/background3.jpg")
        self.player_image = py.image.load("resources/graphics/minigame_4/cowboyhorse.png").convert_alpha()
        self.background_image_rect = self.background_image.get_rect()

        self.player_x = 640
        self.player_y = 360
        self.player_speed = 30
        self.player_rect = py.Rect([self.player_x, self.player_y], [100, 100])

        self.starting_timer = None
        self.timer_label = Label(self.game.py_screen, "", [254, 254, 254], 50)
        self.game_duration = 120
        self.time = self.game_duration

        # Dit zijn eigen events die we aanroepen via de timer class en handelen in de on_events methode
        self.spawn_cactus_event = py.USEREVENT + 1
        self.move_cactus_event = py.USEREVENT + 2

        # Laad de cactus image in die we later aan elke cactus class meegeven
        self.cactus_images = []
        self.cactus_images.append(py.image.load("resources/graphics/minigame_4/cactus.png"))
        self.cactus_images.append(py.image.load("resources/graphics/minigame_4/cactus3.png"))
        self.cactus_images.append(py.image.load("resources/graphics/minigame_4/cactus4.png"))
        # Maak een array aan waar we elke cactus_rij instoppen
        self.cactus_rows = []
        self.cactus_speed = 20
        self.total_cactus_spawned = 0
        finish_x = self.game.py_screen.get_width()
        finish_y = 0
        finish_width = 100
        finish_height = self.game.py_screen.get_height()
        self.finish_line_rect = py.Rect([finish_x, finish_y], [finish_width, finish_height])
        self.spawn_finish_line = False
        self.mouse_position = None
        self.StartGame = False
        self.finished_time = -1
        self.won = None

        # Hiermee roepen we de spawn cactus event aan elke 2000ms en de move event elke 20 ms
        # https://www.pygame.org/docs/ref/time.html#pygame.time.set_timer
        py.time.set_timer(self.spawn_cactus_event, 2000)
        py.time.set_timer(self.move_cactus_event, 20)

        self.dark_surface = py.Surface((1280, 720))
        self.dark_surface.set_alpha(170)

        self.finished_label = HeaderLabel(self.game.py_screen, "")

        self.objective_text = ["Game Objective",
                               "Take your horse and race",
                               "Try not to touch the cuctus",
                               "You will lose if your finish time is 0!"]
        self.objective_label_header = HeaderLabel(self.game.py_screen, self.objective_text[0])
        self.objective_label_text_1 = TextLabel(self.game.py_screen, self.objective_text[1])
        self.objective_label_text_2 = TextLabel(self.game.py_screen, self.objective_text[2])
        self.objective_label_text_3 = TextLabel(self.game.py_screen, self.objective_text[3])

        self.controls_text = ["Controls",
                              "A and D",
                              "Move to the left and right",
                              "W and S ",
                              "Move up and down",
                              "",
                              "",
                              "",
                              ""]

        self.controls_label_header = HeaderLabel(self.game.py_screen, self.controls_text[0])
        self.controls_label_text_1 = TextLabel(self.game.py_screen, self.controls_text[1])
        self.controls_label_text_2 = TextLabel(self.game.py_screen, self.controls_text[2])
        self.controls_label_text_3 = TextLabel(self.game.py_screen, self.controls_text[3])
        self.controls_label_text_4 = TextLabel(self.game.py_screen, self.controls_text[4])
        self.controls_label_text_5 = TextLabel(self.game.py_screen, self.controls_text[5])
        self.controls_label_text_6 = TextLabel(self.game.py_screen, self.controls_text[6])
        self.controls_label_text_7 = TextLabel(self.game.py_screen, self.controls_text[7])
        self.controls_label_text_8 = TextLabel(self.game.py_screen, self.controls_text[8])

        self.btn = []
        self.btn.append(PauseScreenButton(game.py_screen, "Start"))
        self.btn.append(PauseScreenButton(game.py_screen, "Back"))

        screen_center_width = self.game.py_screen.get_width() / 2
        self.button_x = screen_center_width - (self.btn[0].width / 2)

    def handle_key_input(self, keys):
        if keys[py.K_w] and keys[py.K_s]:
            pass
        elif keys[py.K_w]:
            self.player_rect.move_ip(0, -self.player_speed)
        elif keys[py.K_s]:
            self.player_rect.move_ip(0, self.player_speed)

        if keys[py.K_a] and keys[py.K_d]:
            pass
        elif keys[py.K_a]:
            self.player_rect.move_ip(-self.player_speed, 0)
        elif keys[py.K_d]:
            self.player_rect.move_ip(self.player_speed, 0)

    def handle_mouse_input(self, event):
            pass

    def handle_mouse_position(self, mouse_position):
        self.mouse_position = mouse_position
        pass

    def on_events(self, events):
        for event in events:
            # Als er een nieuwe cactuse spawn event wordt aangeroepen maak dan een nieuwe cactus row aan en zet die in de bestaande rijën
            if event.type == self.spawn_cactus_event and self.StartGame:
                if self.total_cactus_spawned == -1:
                    pass
                elif self.total_cactus_spawned >= 30:
                    self.total_cactus_spawned = -1
                    self.spawn_finish_line = True
                else:
                    self.total_cactus_spawned += 1
                    new_cactus_row = CactusRow(self.game.py_screen, self.cactus_images)
                    new_cactus_row.create_row()
                    self.cactus_rows.append(new_cactus_row)
            elif event.type == self.move_cactus_event and self.StartGame:
                for cactus_row in self.cactus_rows:
                    cactus_row.move_row_left()
                if self.spawn_finish_line:
                    self.finish_line_rect.move_ip(-1, 0)
            if event.type == py.MOUSEBUTTONDOWN:
                if self.btn[0].is_clicked(self.mouse_position):
                    self.StartGame = True
                    self.starting_timer = time.time()
                elif self.btn[1].is_clicked(self.mouse_position):
                    from src.global_screens.pick_minigame import PickMinigame
                    self.game.drawer.clear()
                    PickMinigame(self.game)

    def on_update(self):
        if self.StartGame:
            # TODO check of de player een cactus raakt. Zo ja geef een penalty en verwijder de cactus van het scherm.

            for cactus_row in self.cactus_rows:
                # Als de cactus row uit het scherm zit remove hem dan uit de current rows
                if cactus_row.rect.right < 0:
                    self.cactus_rows.remove(cactus_row)
                for cactus in cactus_row.items:
                    if self.player_rect.colliderect(cactus.rect):
                        cactus_row.items.remove(cactus)
                        self.time -= 10
            if self.spawn_finish_line:
                if self.player_rect.colliderect(self.finish_line_rect):
                    self.won = True
                    self.StartGame = False
                    if self.finished_time == -1:
                        self.finished_time = self.time_left

            # Kijk of de player rect collied met de finish line rect
            # TODO rework timer
            if self.finished_time != -1:
                self.timer_label.text = "Finished with: " + str(self.finished_time)
            else:
                # timer
                if self.StartGame:
                    self.check_time = time.time()
                    self.time_left = self.time - int(self.check_time - self.starting_timer)
                    self.time_left -= 1
                    if self.time_left <= 0:
                        self.won = False
                        self.StartGame = False
                    #time_to_seconds = self.time // 50
                    self.timer_label.text = "Time left: " + str(self.time_left) + " sec."

    def on_render(self):
        self.game.drawer.draw_canvas()
        self.game.py_screen.blit(self.background_image, self.background_image_rect)

        if self.StartGame:

            # Render elke cactus_rows die we hebben
            for cactus_row in self.cactus_rows:
                cactus_row.render()
            if self.spawn_finish_line:
                py.draw.rect(self.game.py_screen, [127, 255, 212], self.finish_line_rect)
            # self.game.py_screen.blit(self.player_image, self.player_rect)
            self.game.py_screen.blit(self.player_image, self.player_rect)
            self.player_rect.clamp_ip(self.game.py_screen.get_rect())
            self.timer_label.render(500, 100)
        else:
            # Draw an dark surface on the screen
            self.game.py_screen.blit(self.dark_surface, [0, 0])

            if self.won is not None:
                if self.won:
                    self.finished_label.text = "You won with the time: " + str(self.finished_time)
                else:
                    self.finished_label.text = "You lost"
                self.finished_label.render(465, 100)

            # Draw objective
            self.objective_label_header.render(465, 190)
            self.objective_label_text_1.render(465, 240)
            self.objective_label_text_2.render(465, 260)
            self.objective_label_text_3.render(465, 280)

            # Draw controlls
            self.controls_label_header.render(465, 320)
            self.controls_label_text_1.render(465, 370)
            self.controls_label_text_2.render(585, 370)
            self.controls_label_text_3.render(465, 390)
            self.controls_label_text_4.render(585, 390)
            self.controls_label_text_5.render(465, 410)
            self.controls_label_text_6.render(585, 410)
            self.controls_label_text_7.render(465, 430)
            self.controls_label_text_8.render(585, 430)
            self.btn[1].render(self.mouse_position, self.button_x, 640)
            self.btn[0].render(self.mouse_position, self.button_x, 560)

        py.display.update()