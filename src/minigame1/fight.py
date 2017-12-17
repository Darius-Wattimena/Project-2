from src.helper.label import Label
from src.helper.screen_base import ScreenBase
from src.helper.game_object_group import GameObjectGroup
from src.minigame1.ai import AI
from src.minigame1.custom_event import AIEvent
from .player import Player, PlayerState
import pygame as py


class Fight(ScreenBase):
    def __init__(self, game):
        self.game = game
        self.game.set_screen(self)
        self.game_object_group = GameObjectGroup()
        self.game.drawer.clear()
        self.game.drawer.add_image("resources/graphics/minigame_1/background.png")
        self.player = Player(self.game_object_group, self.game.py_screen, self)
        self.ai = AI(self.game_object_group, self.game.py_screen, self)
        self.first = True
        self.passed_time = 0
        self.player_health_label = Label(self.game.py_screen, "Player Health: " + str(self.player.health), [254, 254, 254], 50)
        self.ai_health_label = Label(self.game.py_screen, "AI Health: " + str(self.ai.health), [254, 254, 254], 50)
        self.winner_label = Label(self.game.py_screen, "", [254, 254, 254], 100)
        self.fight_paused_label = Label(self.game.py_screen, "Paused", [254, 254, 254], 100)
        self.fight_paused = False
        self.ai_event = AIEvent(self.ai, self.player)
        py.time.set_timer(self.ai_event.type, 600)

    def on_events(self, events):
        for event in events:
            if event.type == py.KEYDOWN:
                if not self.player.punch_animation_running:
                    if event.key == py.K_j:
                        self.player.punching = True
                elif event.key == py.K_ESCAPE:
                    if self.winner_label is not None:
                        from src.global_screens.pick_minigame import PickMinigame
                        self.game.drawer.clear()
                        PickMinigame(self.game)
                    else:
                        self.fight_paused = not self.fight_paused
            elif event.type == self.ai_event.type:
                self.ai_event.execute()
            elif event.type == py.USEREVENT + 2:
                event.instance.execute(self)
        return

    def on_render(self):
        if not self.fight_paused and (self.player.is_rendering() or self.ai.is_rendering()):
            self.game.drawer.draw_canvas()
            self.player.on_render()
            self.ai.on_render()

            if self.player.is_hitting_punch(self.ai):
                remaining_health = self.ai.on_hit(self.player)
                self.ai_health_label.text = "AI Health: " + str(remaining_health)
            if self.ai.is_hitting_punch(self.player):
                remaining_health = self.player.on_hit(self.ai)
                self.player_health_label.text = "Player Health: " + str(remaining_health)

            self.player_health_label.render(100, 400)
            self.ai_health_label.render(500, 400)
        elif self.fight_paused:
            x = (self.game.py_screen.get_width() / 2) - (self.winner_label.get_width() / 2)
            y = (self.game.py_screen.get_height() / 2) - 100
            if self.player.won_fight is not None:
                self.winner_label.render(x, y)
            else:
                self.fight_paused_label.render(x, y)
        py.display.update()

    def on_update(self):
        if self.player.won_fight is not None:
            self.fight_paused = True
        else:
            self.passed_time += self.game.clock.get_time()
            if self.passed_time > 500:
                # self.ai.on_update(self.player.state == PlayerState.BLOCKING)
                self.passed_time = 0

    def handle_mouse_position(self, mouse_position):
        return

    def handle_mouse_input(self, event):
        return

    def handle_key_input(self, keys):
        if not self.fight_paused:
            self.player.blocking = False
            if keys[py.K_k] and not self.player.punch_animation_running:
                self.player.set_state(PlayerState.BLOCKING)
            elif keys[py.K_d]:
                self.player.set_state(PlayerState.WALKING)
            elif keys[py.K_a]:
                self.player.set_state(PlayerState.WALKING_REVERSE)
            else:
                self.player.set_state(PlayerState.IDLE)
        return
