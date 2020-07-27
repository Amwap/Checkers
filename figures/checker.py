# coding: utf-8

from figure import Figure

class Checker(Figure):
    def __init__(self, board, position):
        Figure.__init__(self)
        self.board = board
        self.position = position
        

        self.name = "Checker"
        self.ico = "o"   
        self.algorithm = [(1,1), (-1,1), (-1,-1), (1,-1), ("point","smt?", "+1","from here"), (1,1), (-1,1)]

    def algorithm(self):
        
