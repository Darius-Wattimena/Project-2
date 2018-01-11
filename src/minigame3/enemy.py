from random import randint


class Enemy:
    def __init__(self):
        return

    def get_location(self):
        random_number = randint(1, 8)

        if random_number == 1:
            return [0, 250]
        elif random_number == 2:
            return [160, 250]
        elif random_number == 3:
            return [320, 250]
        elif random_number == 4:
            return [480, 250]
        elif random_number == 5:
            return [640, 250]
        elif random_number == 6:
            return [800, 250]
        elif random_number == 7:
            return [960, 250]
        elif random_number == 8:
            return [1120, 250]
