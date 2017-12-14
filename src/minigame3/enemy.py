import pygame as py

from random import randint

class enemy():
    def __init__(self):
        return

    def get_location(self):
        random_number = randint(1,8)

        if  random_number == 1:
            return [0,250]
        if  random_number == 2:
            return [160,250]
        if  random_number == 3:
            return [320,250]
        if  random_number == 4:
            return [480,250]
        if  random_number == 5:
            return [640,250]
        if  random_number == 6:
            return [800,250]
        if  random_number == 7:
            return [960,250]
        if  random_number == 8:
            return [1120,250]