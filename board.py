#-*- coding: UTF-8 -*-

import re

class Board():
    def __init__(self,checker):
        fgr = checker

        self.move_list = []

        self.matrix = [[None]*10,
            [None, "·", "o", "·", "o", "·", "o", "·", "o", None],
            [None, "o", "·", "o", "·", "o", "·", "o", "·", None],
            [None, "·", "o", "·", "o", "·", "o", "·", "o", None],
            [None, "·", "·", "·", "·", "·", "·", "·", "·", None],
            [None, "·", "·", "·", "·", "·", "·", "·", "·", None],
            [None, fgr, "·", fgr, "·", fgr, "·", fgr, "·", None],
            [None, "·", fgr, "·", fgr, "·", fgr, "·", fgr, None],
            [None, fgr, "·", fgr, "·", fgr, "·", fgr, "·", None],
            [None]*10,]
                '''
        self.matrix = [[None]*10,
            [None, "·", "o", "·", "o", "·", "o", "·", "o", None],
            [None, "o", "·", "o", "·", "o", "·", "o", "·", None],
            [None, "·", "o", "·", ".", "·", ".", "·", "o", None],
            [None, "·", "·", fgr, "·", fgr, "·", "·", "·", None],
            [None, "·", "·", "·", "·", "·", "·", "·", "·", None],
            [None, fgr, "·", fgr, "·", fgr, "·", fgr, "·", None],
            [None, "·", fgr, "·", fgr, "·", fgr, "·", fgr, None],
            [None, fgr, "·", fgr, "·", fgr, "·", fgr, "·", None],
            [None]*10,]
        '''
        self.board = f"""
            8   {self.matrix[8][1]}  ·  {self.matrix[8][3]}  ·  {self.matrix[8][5]}  ·  {self.matrix[8][7]}  ·
            7   ·  {self.matrix[7][2]}  ·  {self.matrix[7][4]}  ·  {self.matrix[7][6]}  ·  {self.matrix[7][8]}  
            6   {self.matrix[6][1]}  ·  {self.matrix[6][3]}  ·  {self.matrix[6][5]}  ·  {self.matrix[6][7]}  ·
            5   ·  {self.matrix[5][2]}  ·  {self.matrix[5][4]}  ·  {self.matrix[5][6]}  ·  {self.matrix[5][8]}
            4   {self.matrix[4][1]}  ·  {self.matrix[4][3]}  ·  {self.matrix[4][5]}  ·  {self.matrix[4][7]}  ·
            3   ·  {self.matrix[3][2]}  ·  {self.matrix[3][4]}  ·  {self.matrix[3][6]}  ·  {self.matrix[3][8]}
            2   {self.matrix[2][1]}  ·  {self.matrix[2][3]}  ·  {self.matrix[2][5]}  ·  {self.matrix[2][7]}  ·  
            1   ·  {self.matrix[1][2]}  ·  {self.matrix[1][4]}  ·  {self.matrix[1][6]}  ·  {self.matrix[1][8]}

                a  b  c  d  e  f  g  h
            """
    
    
    def transcription(self, string): # a2 b3 || a2b3 || 3b2a || 3b 2a
        t_list = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8,
                  "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8}
        t_string = [t_list[l] for l in re.compile('[^a-z0-9]').sub('',string.lower())]
        return  (tuple(t_string[0:2]), tuple(t_string[2:4]))#поля которые нужно поменять местами



    def search(self, figure):
        temp_list = []

        
12

    def get_board(self):
        return self.board

    def get_matrix(self):
        return self.matrix





    