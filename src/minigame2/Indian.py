import pygame as py

from random import randint


class Indian():
    def __init__(self):
        return

    def get_location(self):
        random_number = randint(1,9)

        if  random_number == 1:
            return [150, 150]
        if  random_number == 2:
            return [150, 300]
        if  random_number == 3:
            return [150, 450]
        if  random_number == 4:
            return [300, 150]
        if  random_number == 5:
            return [300, 300]
        if  random_number == 6:
            return [300, 450]
        if  random_number == 7:
            return [450, 150]
        if  random_number == 8:
            return [450, 300]
        if  random_number == 9:
            return [450, 450]