# coding: utf-8

from figures.figure import Figure

class FreeField(Figure):
    def __init__(self):
        Figure.__init__(self)

        self.name = "Empty"
        self.ico = "·"
        self.team = "Neutral"
