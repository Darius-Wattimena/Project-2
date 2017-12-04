import pygame as py

from random import randint


class Indian():
    def __init__(self):
        return

    def get_location(self):
        random_number = randint(1,9)

        if  random_number == 1:
            return [50,50]
        if  random_number == 2:
            return [50,100]
        if  random_number == 3:
            return [50,150]
        if  random_number == 4:
            return [100,50]
        if  random_number == 5:
            return [100,100]
        if  random_number == 6:
            return [100,150]
        if  random_number == 7:
            return [150,50]
        if  random_number == 8:
            return [150,100]
        if  random_number == 9:
            return [150,150]