from Coords import Coords as Coordinates
from Total_Energy import Total_Energy as Energy
from math import exp
from numpy import random

class MonteCarlo:
    def __init__(self,coords: Coordinates, total_en:Energy, T:float):
        self.__T = T
        self.__coords = coords
        self.__max_step = 0.3
        self.__en = total_en



    def sample(self,n_steps):
        for i in range(n_steps):
            for j in range(self.__coords.n_atoms):
                dx = random.uniform(-self.__max_step,self.__max_step)
                dy = random.uniform(-self.__max_step, self.__max_step)
                old_x, old_y = self.__coords[j].x, self.__coords[j].y
                # x, y sa u mnie byly zdefiniowane jako prywatne...
                # old_x, old_y = self.__coords[j].get_position[0], self.__coords[j].get_position[1]


                old_en = self.__en.energy()
                if self.__coords[j].x is not None:
                    self.__coords[j].x = float(self.__coords[j].x) + dx
                    self.__coords[j].y = float(self.__coords[j].y) + dy
                new_en = self.__en.energy()
                delta_e = new_en - old_en
                if delta_e >0 and random.random() > exp(-delta_e/self.__T):
                    self.__coords[j].x = old_x
                    self.__coords[j].y = old_y
            print(self.__en.energy())
