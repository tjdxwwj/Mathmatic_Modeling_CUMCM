# -*- coding: utf-8 -*-
"""
---------------------------------------------
    File Name:          缓速下降
    Desciption:         
    Author:             fanzhiwei
    date:               2019/9/5 20:36
---------------------------------------------
    Change Activity:    2019/9/5 20:36
---------------------------------------------
"""


import math
import matplotlib.pyplot as plt

yuexin = [0.0, 0.0, 0.0]
t = 0.0001

class Zhujiansu():

    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.z = 1734403.000099938130006
        self.v = 0.03550947606212837
        self.m = 1229.5722989064545
        self.t = 0.0
        self.f = 0.0
        self.ve = 2940.0
        self.G = 6.67*10**(-11)
        self.M = 7.3477*10**22
        self.t_set = []
        self.v_set = []
        self.f_set = []
        self.height_set = []


        self.t_set.append(self.t)
        self.v_set.append(self.v)
        self.f_set.append(self.f)
        self.height_set.append(30.0)

    def get_a(self):
        r2 = self.z ** 2
        mg = self.G * self.M * self.m / r2
        a_z = (self.f - mg) / self.m
        return a_z

    def update(self):
        self.t = self.t + t
        self.f = self.f + 0.04115169
        self.m = self.m - (self.f / self.ve) * t
        a_z = self.get_a()
        z = self.z - self.v * t + 0.5 * a_z * t ** 2
        self.v = self.v - a_z * t
        self.z = z

        self.t_set.append(self.t)
        self.f_set.append(self.f)
        self.height_set.append(self.z-1734373.0)
        self.v_set.append(self.v)

    def draw(self):
        plt.figure()
        plt.plot(self.t_set, self.height_set)
        plt.show()

if __name__ == "__main__":
    print('start')
    zhujiansu = Zhujiansu()
    while zhujiansu.z - 1734377.0 > 10**(-4):
        zhujiansu.update()
    print("time:", zhujiansu.t)
    print("v:", zhujiansu.v)
    print("m:", zhujiansu.m)
    print("height:", zhujiansu.z-1734373.0)
    zhujiansu.draw()