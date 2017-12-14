import pygame as py
from random import *

class Target():
    def __init__(self):
        return

    def random_location(self):
        random_number = randint(1, 22)

        if  random_number == 1:
            return [30,250]
        if  random_number == 2:
            return [130,250]
        if  random_number == 3:
            return [180,250]
        if  random_number == 4:
            return [305,310]
        if  random_number == 5:
            return [430,270]
        if  random_number == 6:
            return [620,280]
        if  random_number == 7:
            return [790,250]
        if  random_number == 8:
            return [910,280]
        if  random_number == 9:
            return [965,290]
        if  random_number == 10:
            return [1025,280]
        if  random_number == 11:
            return [1100,270]
        if  random_number == 12:
            return [1160,270]
        if  random_number == 13:
            return [1230,242]
        if  random_number == 14:
            return [5,450]
        if  random_number == 15:
            return [137,433]
        if  random_number == 16:
            return [250,410]
        if  random_number == 17:
            return [340,410]
        if  random_number == 18:
            return [420,385]
        if  random_number == 19:
            return [795,385]
        if  random_number == 20:
            return [910,380]
        if  random_number == 21:
            return [990,415]
        if  random_number == 22:
            return [1165,490]