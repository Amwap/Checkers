#-*- coding: UTF-8 -*-

from figures.freefield import FreeField
import re


class Board():
    def __init__(self, matrix):
        self.matrix = matrix
            
        
        '''self.matrix = [[None]*9,
            [None, free, f[0], free, f[1], free, f[2], free, f[3]],
            [None, f[4], free, f[5], free, f[6], free, f[7], free],
            [None, free, f[8], free, f[9], free, f[10], free, f[11]],
            [None, free, free, free, free, free, free, free, free],
            [None, free, free, free, free, free, free, free, free],
            [None, s[11], free, s[10], free, s[9], free, s[8], free],
            [None, free, s[7], free, s[6], free, s[5], free, s[4]],
            [None, s[3], free, s[2], free, s[1], free, s[0], free],
            ]
        '''

        def m(f1,f2):
            return self.matrix[f1][f2].get_ico()

        self.board = f"""
            8   {m(8,1)}  {m(8,2)}  {m(8,3)}  {m(8,4)}  {m(8,5)}  {m(8,6)}  {m(8,7)}  {m(8,8)}  
            7   {m(7,1)}  {m(7,2)}  {m(7,3)}  {m(7,4)}  {m(7,5)}  {m(7,6)}  {m(7,7)}  {m(7,8)}  
            6   {m(6,1)}  {m(6,2)}  {m(6,3)}  {m(6,4)}  {m(6,5)}  {m(6,6)}  {m(6,7)}  {m(6,8)}  
            5   {m(5,1)}  {m(5,2)}  {m(5,3)}  {m(5,4)}  {m(5,5)}  {m(5,6)}  {m(5,7)}  {m(5,8)}
            4   {m(4,1)}  {m(4,2)}  {m(4,3)}  {m(4,4)}  {m(4,5)}  {m(4,6)}  {m(4,7)}  {m(4,8)}  
            3   {m(3,1)}  {m(3,2)}  {m(3,3)}  {m(3,4)}  {m(3,5)}  {m(3,6)}  {m(3,7)}  {m(3,8)}
            2   {m(2,1)}  {m(2,2)}  {m(2,3)}  {m(2,4)}  {m(2,5)}  {m(2,6)}  {m(2,7)}  {m(2,8)}  
            1   {m(1,1)}  {m(1,2)}  {m(1,3)}  {m(1,4)}  {m(1,5)}  {m(1,6)}  {m(1,7)}  {m(1,8)}

                a  b  c  d  e  f  g  h
            """
        print(self.board)
    
    
    def transcription(self, string): # a2 b3 || a2b3 || 3b2a || 3b 2a
        t_list = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8,
                  "1":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8}
        t_string = [t_list[l] for l in re.compile('[^a-z0-9]').sub('',string.lower())]
        return  (tuple(t_string[0:2]), tuple(t_string[2:4]))#поля которые нужно поменять местами



    def search(self, figure):
        temp_list = []

    def get_board(self):
        return self.board

    def get_matrix(self):
        return self.matrix





    