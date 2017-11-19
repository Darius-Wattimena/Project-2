""" Call this module when starting the game """
from src.game import Game
from src.game_config import GameConfig
import pygame as py

py.init()

CONFIG = GameConfig()

py.display.set_caption(CONFIG.title)
screen = py.display.set_mode([CONFIG.width, CONFIG.height])

GAME_INSTANCE = Game.Instance()
GAME_INSTANCE.start(screen)