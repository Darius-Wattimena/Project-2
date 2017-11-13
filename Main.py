""" Call this module when starting the game """
import pygame
from game import Game

gameInstance = Game(1280, 720)
gameInstance.start()