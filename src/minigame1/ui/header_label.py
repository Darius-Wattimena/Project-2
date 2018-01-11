from src.helper.label import Label


class HeaderLabel(Label):
    def __init__(self, screen, text, color=None, font_size=40):
        if color is None:
            color = [249, 239, 196]

        super().__init__(screen, text, color, font_size, font="resources/fonts/Carnevalee Freakshow.ttf")
