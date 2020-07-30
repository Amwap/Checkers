# coding: utf-8

class Figure():
    def __init__(self, name=None, ico="·", team="neutral", location=None, matrix=None, coordinate=None):
        self.name = name
        self.ico = ico
        self.algorithm = []
        self.team = team
        self.location = location #top bottom
        self.coordinate = coordinate
        self.status = "live" #or die


    def reverse(self, algorithm):
        new_alg = []
        for i in algorithm:
            if i[0] == "point":
                new_alg.append(i)
            else: new_alg.append((-i[0], -i[1])) 
        return new_alg

    def get_algorithm(self):
        return self.algorithm

    def get_name(self):
        return self.name

    def get_ico(self):
        return self.ico

    def get_team(self):
        return self.team

    def get_coordinate(self):
        return self.coordinate


