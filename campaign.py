import pygame
import random as rd

from settings import *

from char import *


class Campaign:
    def __init__(self):
        self.levels = 5
        self.level_list = []

    def build_campaign(self, inimigos, chefes):
        for level in range(1, self.levels + 1):
            inimigo = rd.choice(inimigos)
            if level == 5 or level == 10 or level == 15:
                    inimigo = chefes[0]
            if self.level_list.count(inimigo) > 0: 
                while self.level_list.count(inimigo) > 0: 
                    inimigo = rd.choice(inimigos)         
            self.level_list.append(inimigo)
    
    def delete_battle(self, battle):
        del battle
         



