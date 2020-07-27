# -*- coding: UTF-8 -*-

class User():
    def __init__(self):
        self.user_name = str()

        self.move_history = []
        self.last_move = str()
        self.score = None
        self.eated_figures = []

    def move_to(self, string):
        self.move_history.append(string)

    

    
