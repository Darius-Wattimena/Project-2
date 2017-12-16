from random import randint


class Target:
    def __init__(self):
        return

    def get_location(self):
        random_number = randint(1, 22)

        location_map = [
            [30, 250],
            [130, 250],
            [180, 250],
            [305, 310],
            [430, 270],
            [620, 280],
            [790, 250],
            [910, 280],
            [965, 290],
            [1025, 280],
            [1100, 270],
            [1160, 270],
            [1230, 242],
            [5, 450],
            [137, 433],
            [250, 410],
            [340, 410],
            [420, 385],
            [795, 385],
            [910, 380],
            [990, 415],
            [1165, 490]
        ]

        random_index = random_number - 1
        return location_map[random_index]
