from random import randint

import pygame as py
from pygame.locals import *

from src.minigame1.ai import AIState
from src.minigame1.player import PlayerState


class AIEvent:
    def __init__(self, ai, player):
        self.ai = ai
        self.player = player
        self.code = "AIEVENT"
        self.name = "AIEvent"
        self.type = USEREVENT + 1

    # For testing
    def get_event(self):
        return py.event.Event(USEREVENT, code=self.code, name=self.name)

    def execute(self):
        self.ai.blocking = False
        self.ai.distance_gap = self.ai.object_group.distance_to_left(self.ai)
        hit_gap = self.ai.distance_gap - self.ai.hit_range

        behaviour = randint(1, 100)

        player_blocking = self.player.state == PlayerState.BLOCKING
        if player_blocking:
            if behaviour < 30:
                self.ai.state = AIState.BLOCKING
            else:
                if hit_gap > 20:
                    self.ai.state = AIState.WALKING
                elif hit_gap < 20:
                    self.ai.state = AIState.WALKING_REVERSE
                else:
                    self.ai.state = AIState.IDLE
        elif hit_gap < 20:
            if behaviour < 75:
                self.ai.punching = True
            else:
                self.ai.state = AIState.WALKING_REVERSE
        elif hit_gap > 20:
            self.ai.state = AIState.WALKING
        else:
            self.ai.state = AIState.IDLE
