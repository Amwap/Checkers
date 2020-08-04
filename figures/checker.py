# coding: utf-8

from figures.figure import Figure

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
        self.algorithm = [(1,1), (-1,1), (-1,-1), (1,-1), ("point",), (1,1), (-1,1)]
        
        if location == "top": 
            self.algorithm = self.reverse(self.algorithm)
        

    def searcher(self, position): #Блят! да почему она не работает как надо?!
        temp_list = []
        point = False
        for stage in self.algorithm:
            
            
            if stage[0] == "point":
                point = True
                if len(temp_list) != 0:
                    self.priority = True
                    self.move_list = temp_list
                    return 'complite' 
                continue            

            if not (1 <= (self.position[0]+stage[0]) <= 8):  continue 
            if not (1 <= (self.position[1]+stage[1]) <= 8):  continue 
            
            


            # if point == False:
            #     field = self.matrix[self.position[0]+stage[0]][self.position[1]+stage[1]]
            #     team = field.get_team()
            #     if team != self.team and team != "free":
            #         temp_list.append((self.position[0]+stage[0],self.position[1]+stage[1]))
            


            if point == True:
                # if self.location == 'top' and stage == (1, -1):
                #     print(True)

                field = self.matrix[self.position[0]+stage[0]][self.position[1]+stage[1]]
                team = field.get_team()
                if field.get_team() == "free":
                    temp_list.append((self.position[0]+stage[0],self.position[1]+stage[1]))


        self.move_list = temp_list


                

                    
                
                