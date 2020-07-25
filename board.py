#-*- coding: UTF-8 -*-

class Board():
    def __init__(self,fgr):
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

        self.board = f"""
            8   {matrix[8][1]}  ·  {matrix[8][3]}  ·  {matrix[8][5]}  ·  {matrix[8][7]}  ·
            7   ·  {matrix[7][2]}  ·  {matrix[7][4]}  ·  {matrix[7][6]}  ·  {matrix[7][8]}  
            6   {matrix[6][1]}  ·  {matrix[6][3]}  ·  {matrix[6][5]}  ·  {matrix[6][7]}  ·
            5   ·  {matrix[5][2]}  ·  {matrix[5][4]}  ·  {matrix[5][6]}  ·  {matrix[5][8]}
            4   {matrix[4][1]}  ·  {matrix[4][3]}  ·  {matrix[4][5]}  ·  {matrix[4][7]}  ·
            3   ·  {matrix[3][2]}  ·  {matrix[3][4]}  ·  {matrix[3][6]}  ·  {matrix[3][8]}
            2   {matrix[2][1]}  ·  {matrix[2][3]}  ·  {matrix[2][5]}  ·  {matrix[2][7]}  ·  
            1   ·  {matrix[1][2]}  ·  {matrix[1][4]}  ·  {matrix[1][6]}  ·  {matrix[1][8]}

                a  b  c  d  e  f  g  h
            """

    def get_board(self):
        return self.board

    def get_matrix(self):
        return self.matrix

    