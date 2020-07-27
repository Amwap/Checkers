# coding: utf-8

class Figure():
    def __init__(self):
        self.name = ""
        self.ico = ""
        self.algorithm = []
        self.team = None

    def reverse(self, algorithm):
        return [ (-a[0], -a[1]) for a in algorithm]

    def get_algorithm(self):
        return self.algorithm

    def get_name(self):
        return self.name

    def get_ico(self):
        return self.ico

    def get_team(self):
        return self.team


