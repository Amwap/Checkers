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


    def boardbuilder(self):
        def fillinger(even, ico, uname):
            line = [None]
            for i in range(8):
                if (i%2 == 0) is even: line.append(FreeField())
                else: line.append(Checker(name="checker", ico=ico, team=uname, location="top"))
            return line

        def longest_functions_name_in_this_code():
            line = [None]
            for i in range(8):
                line.append(FreeField())
            return line


        self.matrix.append(fillinger(even=True, ico='☺',uname=self.uname1))
        self.matrix.append(fillinger(even=False, ico='☺',uname=self.uname1))
        self.matrix.append(fillinger(even=True, ico='☺',uname=self.uname1))
        self.matrix.append(longest_functions_name_in_this_code())
        self.matrix.append(longest_functions_name_in_this_code())
        self.matrix.append(fillinger(even=False, ico='☻',uname=self.uname2))
        self.matrix.append(fillinger(even=True, ico='☻',uname=self.uname2))
        self.matrix.append(fillinger(even=False, ico='☻',uname=self.uname2))



    def run(self):
        # print('Ferst team have figure like this "☻", for second team this "☺" ')
        # self.uname1 = input("First user enter you'r name: ")
        # print('If you wanna start game with bot, enter "bot"')
        # self.uname2 = input("Second user, enter you'r name: ")
        self.uname1 = "1"
        self.uname2 = "2"

        self.boardbuilder()
        self.board = Board(self.matrix)



Script().run()


