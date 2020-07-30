# coding: utf-8

from figures.figure import Figure

class Checker(Figure):
    def __init__(self, name=None, ico="·", team="neutral", location=None, matrix=None, coordinate=None):
        Figure.__init__(self)
        self.name = name
        self.ico = ico
        self.move_list = []
        self.team = team
        self.location = location #top bottom
        self.coordinate = coordinate
        self.algorithm = [(1,1), (-1,1), (-1,-1), (1,-1), ("point","smt?", "+1","empty?","from here"), (1,1), (-1,1)]
        
        if location == "top": 
            self.algorithm = self.reverse(self.algorithm)
        

    def searcher(self, position):
        pass