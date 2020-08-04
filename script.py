# coding: utf-8


from board import Board
from figures.checker import Checker
from figures.queen import Queen
from figures.freefield import FreeField

class Script():
    def __init__(self):
        self.uname1 = "Player 1"
        self.uname2 = "Player 2"
        self.matrix = [[None]*9]
        self.figure_set = []

        self.i = 0
        self.j = 0


    def boardbuilder(self):
        self.j = 0

        def fillinger(even=None, ico="·", uname="neutral",location=None):
            self.j += 1; self.i = 0
            line = [None]
            for num in range(8):
                self.i += 1
                if (num%2 == 0) is even or even == None: line.append(FreeField(name="free", ico="·", team="free"))
                else: 
                    new = Checker(name="checker", ico=ico, team=uname, location=location, matrix=self.matrix, position=(self.j,self.i))
                    line.append(new)
                    self.figure_set.append(new)

            return line

        def longest_functions_name_in_this_code():
            line = [None]
            for i in range(8):
                new = FreeField(name="free", ico="·", team="free")
                line.append(new)
            return line


        self.matrix.append(fillinger(even=True, ico='☺',uname=self.uname1, location="bottom"))
        self.matrix.append(fillinger(even=False, ico='☺',uname=self.uname1, location="bottom"))
        self.matrix.append(fillinger(even=True, ico='☺',uname=self.uname1, location="bottom"))
        self.matrix.append(fillinger())
        self.matrix.append(fillinger())
        self.matrix.append(fillinger(even=False, ico='☻',uname=self.uname2, location="top"))
        self.matrix.append(fillinger(even=True, ico='☻',uname=self.uname2, location="top"))
        self.matrix.append(fillinger(even=False, ico='☻',uname=self.uname2, location="top"))



    def run(self):
        # print('Ferst team have figure like this "☻", for second team this "☺" ')
        # self.uname1 = input("First user enter you'r name: ")
        # print('If you wanna start game with bot, enter "bot"')
        # self.uname2 = input("Second user, enter you'r name: ")
        self.uname1 = "amwap"
        self.uname2 = "bot"

        self.boardbuilder()
        self.board = Board(self.matrix, self.figure_set)

        # print(self.figure_set)
        for figure in self.figure_set:
            figure.searcher(figure.get_position())
            print(figure.get_team())
            print(figure.get_position())
            print(figure.get_move_list())
            print('--------------------')
            # print(figure.move_list)



Script().run()


