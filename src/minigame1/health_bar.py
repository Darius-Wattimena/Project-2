import pygame as py

from src.helper.label import Label


class HealthBar:
    def __init__(self, screen, x, y, is_player):
        self.screen = screen
        self.x = x
        self.y = y
        self.mugshot_images = []
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
            self.mugshot_images.append(py.image.load("resources/graphics/minigame_1/player/mugshot1.png"))
            self.mugshot_images.append(py.image.load("resources/graphics/minigame_1/player/mugshot2.png"))
            self.mugshot_images.append(py.image.load("resources/graphics/minigame_1/player/mugshot3.png"))

            self.name = Label(self.screen, "Player", [255, 255, 255], 40,
                              font="resources/fonts/Carnevalee Freakshow.ttf")
            self.rect = self.images[0].get_rect(x=x + 70, y=y)
            self.mugshot_rect = self.rect
            self.mugshot_rect = self.mugshot_images[0].get_rect(x=x, y=y)
            self.name_x = self.x + 75
            self.name_y = self.y + 50
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

            self.mugshot_images.append(py.transform.flip(py.image.load("resources/graphics/minigame_1/ai/mugshot1.png"), True, False))
            self.mugshot_images.append(py.transform.flip(py.image.load("resources/graphics/minigame_1/ai/mugshot2.png"), True, False))
            self.mugshot_images.append(py.transform.flip(py.image.load("resources/graphics/minigame_1/ai/mugshot3.png"), True, False))

            self.name = Label(self.screen, "Enemy", [255, 255, 255], 40,
                              font="resources/fonts/Carnevalee Freakshow.ttf")
            self.rect = self.images[0].get_rect(x=x - 71, y=y)
            self.mugshot_rect = self.rect
            self.mugshot_rect = self.mugshot_images[0].get_rect(x=x + 341, y=y)
            self.name_x = self.x + 245
            self.name_y = self.y + 50

    def on_render(self, fighter):
        self.name.render(self.name_x, self.name_y)
        if fighter.health == 100:
            self.screen.blit(self.images[0], self.rect)
            self.screen.blit(self.mugshot_images[0], self.mugshot_rect)
        elif fighter.health >= 81:
            self.screen.blit(self.images[1], self.rect)
            self.screen.blit(self.mugshot_images[0], self.mugshot_rect)
        elif fighter.health >= 71:
            self.screen.blit(self.images[2], self.rect)
            self.screen.blit(self.mugshot_images[0], self.mugshot_rect)
        elif fighter.health >= 61:
            self.screen.blit(self.images[3], self.rect)
            self.screen.blit(self.mugshot_images[1], self.mugshot_rect)
        elif fighter.health >= 51:
            self.screen.blit(self.images[4], self.rect)
            self.screen.blit(self.mugshot_images[1], self.mugshot_rect)
        elif fighter.health >= 41:
            self.screen.blit(self.images[5], self.rect)
            self.screen.blit(self.mugshot_images[1], self.mugshot_rect)
        elif fighter.health >= 31:
            self.screen.blit(self.images[6], self.rect)
            self.screen.blit(self.mugshot_images[1], self.mugshot_rect)
        elif fighter.health >= 21:
            self.screen.blit(self.images[7], self.rect)
            self.screen.blit(self.mugshot_images[2], self.mugshot_rect)
        elif fighter.health >= 11:
            self.screen.blit(self.images[8], self.rect)
            self.screen.blit(self.mugshot_images[2], self.mugshot_rect)
        elif fighter.health >= 1:
            self.screen.blit(self.images[9], self.rect)
            self.screen.blit(self.mugshot_images[2], self.mugshot_rect)
        else:
            self.screen.blit(self.images[10], self.rect)
            self.screen.blit(self.mugshot_images[2], self.mugshot_rect)
