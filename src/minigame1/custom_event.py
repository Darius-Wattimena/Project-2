from random import randint

import pygame as py
from pygame.locals import *


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

        from src.minigame1.player import PlayerState
        from src.minigame1.ai import AIState

        player_blocking = self.player.state == PlayerState.BLOCKING
        if player_blocking:
            if behaviour < 30:
                self.ai.set_state(AIState.BLOCKING)
            else:
                if hit_gap > self.ai.hit_range:
                    self.ai.set_state(AIState.WALKING)
                elif hit_gap < self.ai.hit_range:
                    self.ai.set_state(AIState.WALKING_REVERSE)
                else:
                    self.ai.set_state(AIState.IDLE)
        elif hit_gap < self.ai.hit_range:
            if behaviour < 75:
                self.ai.punching = True
            else:
                self.ai.state = AIState.WALKING_REVERSE
        elif hit_gap > self.ai.hit_range:
            self.ai.state = AIState.WALKING
        else:
            self.ai.state = AIState.IDLE


class FightDoneEvent:
    def __init__(self, loser):
        self.loser = loser
        self.code = "FIGHTDONE"
        self.name = "FightWinner"
        self.type = USEREVENT + 2

    def get_event(self):
        return py.event.Event(self.type, code=self.code, name=self.name, instance=self)

    def execute(self, fight):
        from src.minigame1.ai import AI
        from src.minigame1.player import Player
        if type(self.loser) is AI:
            fight.player.won_fight = True
            fight.fight_paused = True
            fight.winner_label.text = "Player Won!"
        elif type(self.loser) is Player:
            fight.player.won_fight = False
            fight.fight_paused = True
            fight.winner_label.text = "Enemy Won!"
