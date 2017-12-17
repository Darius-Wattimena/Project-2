from src.helper.label import Label
from src.helper.screen_base import ScreenBase
import pygame as py

from src.minigame4.cactus import Cactus
from src.minigame4.cactus_row import CactusRow


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

        self.player_x = 640
        self.player_y = 360
        self.player_speed = 10
        self.player_rect = py.Rect([self.player_x, self.player_y], [40, 40])

        self.time = 0
        self.timer_label = Label(self.game.py_screen, "", [254, 254, 254], 50)

        #https://www.pygame.org/docs/ref/time.html#pygame.time.set_timer
        self.spawn_cactus_event = py.USEREVENT + 1
        self.move_cactus_event = py.USEREVENT + 2

        self.cactus_image = py.image.load("resources/graphics/minigame_4/cactus.png")
        self.cactus_rows = []

        # hiermee roepen we de spawn cactus event aan elke 500ms en de move event elke 100 ms
        py.time.set_timer(self.spawn_cactus_event, 2000)
        py.time.set_timer(self.move_cactus_event, 20)

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
        pass

    def on_events(self, events):
        for event in events:
            # Als er een nieuwe cactuse spawn event wordt aangeroepen maak dan een nieuwe cactus row aan en zet die in de bestaande rijën
            if event.type == self.spawn_cactus_event:
                new_cactus_row = CactusRow(self.game.py_screen, self.cactus_image)
                new_cactus_row.create_row()
                self.cactus_rows.append(new_cactus_row)
            elif event.type == self.move_cactus_event:
                for cactus_row in self.cactus_rows:
                    cactus_row.move_row_left()

    def on_update(self):
        for cactus_row in self.cactus_rows:
            # Als de cactus row uit het scherm zit remove hem dan uit de current rows
            if cactus_row.rect.right < 0:
                self.cactus_rows.remove(cactus_row)
        self.time += 1
        self.timer_label.text = str(self.time)
        pass

    def on_render(self):
        self.game.drawer.draw_canvas()
        self.game.py_screen.blit(self.background_image, self.background_image_rect)
        for cactus_row in self.cactus_rows:
            cactus_row.render()
        self.game.py_screen.blit(self.player_image, self.player_rect)
        self.timer_label.render(500, 100)
        py.display.update()