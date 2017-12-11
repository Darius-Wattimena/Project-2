import pygame as py

from random import randint


class Indian():
    def __init__(self):
        return

    def get_location(self):
        random_number = randint(1,9)

        if  random_number == 1:
            return [100, 100]
        if  random_number == 2:
            return [100, 200]
        if  random_number == 3:
            return [100, 300]
        if  random_number == 4:
            return [200, 100]
        if  random_number == 5:
            return [200, 200]
        if  random_number == 6:
            return [200, 300]
        if  random_number == 7:
            return [300,100]
        if  random_number == 8:
            return [300,200]
        if  random_number == 9:
            return [300,300]