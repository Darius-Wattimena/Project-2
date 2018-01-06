from src.helper.label import Label


class HeaderLabel(Label):
    def __init__(self, screen, text):
        super().__init__(screen, text, [249, 239, 196], 40, font="resources/fonts/Carnevalee Freakshow.ttf")
