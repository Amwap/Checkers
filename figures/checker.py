# coding: utf-8

from figures.figure import Figure

class Checker(Figure):
    def __init__(self, name=None, ico="·", team="neutral", location=None):
        Figure.__init__(self)
        self.name = name
        self.ico = ico
        self.algorithm = []
        self.team = team
        self.location = location #top bottom

        self.algorithm = [(1,1), (-1,1), (-1,-1), (1,-1), ("point","smt?", "+1","empty?","from here"), (1,1), (-1,1)]

    def algorithm(self):
        for point in self.algorithm:
            pass
