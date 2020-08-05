# coding: utf-8
from vector import Point
class Figure():
    def __init__(self, name=None, ico="·", team="neutral", location=None, matrix=None, position=None):
        self.name = name
        self.ico = ico
        self.algorithm = []
        self.team = team
        self.move_list = []
        self.location = location #top bottom
        self.position = position
        self.status = "live" #or die


    def reverse(self, algorithm):
        new_alg = []
        for i in algorithm:
            if i == 'next':
                new_alg.append(i)
            else: new_alg.append(Point(-i.x, -i.y)) 
        return new_alg

    def get_algorithm(self):
        return self.algorithm

    def get_name(self):
        return self.name

    def get_ico(self):
        return self.ico

    def get_team(self):
        return self.team

    def get_position(self):
        return self.position

    def get_move_list(self):
        return self.move_list


