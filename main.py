""" Call this module when starting the game """
from project_game.game import Game

GAME_INSTANCE = Game("Game", 1280, 720)
GAME_INSTANCE.start()