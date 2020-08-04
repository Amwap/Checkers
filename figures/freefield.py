# coding: utf-8

from figures.figure import Figure

class FreeField(Figure):
    def __init__(self, name, ico, team):
        Figure.__init__(self)

        self.name = "Empty"
        self.ico = "·"
        self.team = "free"
