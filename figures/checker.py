# coding: utf-8

from figures.figure import Figure
from vector import Point

class Checker(Figure):
    def __init__(self, name=None, ico="·", team="neutral", location=None, matrix=None, position=None):
        Figure.__init__(self)
        self.name = name
        self.ico = ico
        self.move_list = []
        self.team = team
        self.location = location #top bottom
        self.position = position
        self.matrix = matrix
        self.priority = False
        self.algorithm = [Point(1,1), Point(-1,1), Point(-1,-1), Point(1,-1),"next", Point(1,1), Point(1,-1)]
        
        if location == "top": 
            self.algorithm = self.reverse(self.algorithm)
        

    def searcher(self, position): # - Блят! да почему она не работает как надо?!
                                  # - Потому, что ты перепутал Х с У долбоёб!
        temp_list = []
        point = False
        for stage in self.algorithm:
            
            
            if stage == "next":
                point = True
                if len(temp_list) != 0:
                    self.priority = True
                    self.move_list = temp_list
                    return 'complite' 
                continue            

            if not (1 <= (self.position.col+stage.col) <= 8):  continue 
            if not (1 <= (self.position.row+stage.row) <= 8):  continue 
            

            if point == True:
                field = self.matrix[self.position.col+stage.col][self.position.row+stage.row]
                team = field.get_team()
                if field.get_team() == "free":
                    temp_list.append(Point(self.position.col+stage.col,self.position.row+stage.row))


        self.move_list = temp_list


                

                    
                
                