import pygame as py


class Label:
    def __init__(self, screen, text, color, size, font=None, sys_font=None):
        self.screen = screen
        self.text = text
        self.color = color
        self.size = size
        if sys_font is not None:
            self.font = py.font.SysFont(sys_font, self.size)
        else:
            self.font = py.font.Font(font, self.size)

    def render(self, x, y):
        text = self.font.render(self.text, True, self.color)
        text_rect = text.get_rect(x=x, y=y)
        self.screen.blit(text, text_rect)

    def get_width(self):
        text = self.font.render(self.text, True, self.color)
        text_rect = text.get_rect()
        return text_rect.width
