import pygame as py
from random import *

class Target():
    def __init__(self):
        return

    def random_location(self):
        random_number = randint(1,22)

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
            return [600,335]
        if  random_number == 7:
            return [790,315]
        if  random_number == 8:
            return [890,332]
        if  random_number == 9:
            return [940,340]
        if  random_number == 10:
            return [1030,334]
        if  random_number == 11:
            return [1120,328]
        if  random_number == 12:
            return [1180,326]
        if  random_number == 13:
            return [1260,312]
        if  random_number == 14:
            return [35,500]
        if  random_number == 15:
            return [157,493]
        if  random_number == 16:
            return [280,475]
        if  random_number == 17:
            return [370,470]
        if  random_number == 18:
            return [450,450]
        if  random_number == 19:
            return [825,450]
        if  random_number == 20:
            return [935,440]
        if  random_number == 21:
            return [1010,475]
        if  random_number == 22:
            return [1185,530]