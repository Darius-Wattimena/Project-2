import pygame as py


class Label:
    def __init__(self, screen, text, color, size, font=None):
        self.screen = screen
        self.text = text
        self.color = color
        self.size = size
        self.font = font

    def render(self, x, y):
        font = py.font.Font(self.font, self.size)
        text = font.render(self.text, True, self.color)
        text_rect = text.get_rect(x=x, y=y)
        self.screen.blit(text, text_rect)

    def get_width(self):
        font = py.font.Font(self.font, self.size)
        text = font.render(self.text, True, self.color)
        text_rect = text.get_rect()
        return text_rect.width
