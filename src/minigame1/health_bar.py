import pygame as py


class HealthBar:
    def __init__(self, screen, x, y, is_player):
        self.screen = screen
        self.images = []
        if is_player:
            self.images.append(py.image.load("resources/graphics/minigame_1/ui/HealthBar10.png"))
            self.images.append(py.image.load("resources/graphics/minigame_1/ui/HealthBar9.png"))
            self.images.append(py.image.load("resources/graphics/minigame_1/ui/HealthBar8.png"))
            self.images.append(py.image.load("resources/graphics/minigame_1/ui/HealthBar7.png"))
            self.images.append(py.image.load("resources/graphics/minigame_1/ui/HealthBar6.png"))
            self.images.append(py.image.load("resources/graphics/minigame_1/ui/HealthBar5.png"))
            self.images.append(py.image.load("resources/graphics/minigame_1/ui/HealthBar4.png"))
            self.images.append(py.image.load("resources/graphics/minigame_1/ui/HealthBar3.png"))
            self.images.append(py.image.load("resources/graphics/minigame_1/ui/HealthBar2.png"))
            self.images.append(py.image.load("resources/graphics/minigame_1/ui/HealthBar1.png"))
            self.images.append(py.image.load("resources/graphics/minigame_1/ui/HealthBar0.png"))
        else:
            self.images.append(py.transform.flip(py.image.load("resources/graphics/minigame_1/ui/HealthBar10.png"), True, False))
            self.images.append(py.transform.flip(py.image.load("resources/graphics/minigame_1/ui/HealthBar9.png"), True, False))
            self.images.append(py.transform.flip(py.image.load("resources/graphics/minigame_1/ui/HealthBar8.png"), True, False))
            self.images.append(py.transform.flip(py.image.load("resources/graphics/minigame_1/ui/HealthBar7.png"), True, False))
            self.images.append(py.transform.flip(py.image.load("resources/graphics/minigame_1/ui/HealthBar6.png"), True, False))
            self.images.append(py.transform.flip(py.image.load("resources/graphics/minigame_1/ui/HealthBar5.png"), True, False))
            self.images.append(py.transform.flip(py.image.load("resources/graphics/minigame_1/ui/HealthBar4.png"), True, False))
            self.images.append(py.transform.flip(py.image.load("resources/graphics/minigame_1/ui/HealthBar3.png"), True, False))
            self.images.append(py.transform.flip(py.image.load("resources/graphics/minigame_1/ui/HealthBar2.png"), True, False))
            self.images.append(py.transform.flip(py.image.load("resources/graphics/minigame_1/ui/HealthBar1.png"), True, False))
            self.images.append(py.transform.flip(py.image.load("resources/graphics/minigame_1/ui/HealthBar0.png"), True, False))
        self.rect = self.images[0].get_rect(x=x, y=y)

    def on_render(self, fighter):
        if fighter.health == 100:
            self.screen.blit(self.images[0], self.rect)
        elif fighter.health >= 81:
            self.screen.blit(self.images[1], self.rect)
        elif fighter.health >= 71:
            self.screen.blit(self.images[2], self.rect)
        elif fighter.health >= 61:
            self.screen.blit(self.images[3], self.rect)
        elif fighter.health >= 51:
            self.screen.blit(self.images[4], self.rect)
        elif fighter.health >= 41:
            self.screen.blit(self.images[5], self.rect)
        elif fighter.health >= 31:
            self.screen.blit(self.images[6], self.rect)
        elif fighter.health >= 21:
            self.screen.blit(self.images[7], self.rect)
        elif fighter.health >= 11:
            self.screen.blit(self.images[8], self.rect)
        elif fighter.health >= 1:
            self.screen.blit(self.images[9], self.rect)
        else:
            self.screen.blit(self.images[10], self.rect)
