# coding: utf-8

from figure import Figure

class Checker(Figure):
    def __init__(self):
        Figure.__init__(self)
        self.name = "Checker"
        self.ico = "o"
        self.move_algorithm = [(1,1),(-1,1),(-1,-1),(1,-1)]
        self.kill_algorithm = [(2,2),(-2,2),(-2,-2),(2,-2)]