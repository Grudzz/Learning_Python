# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 18:11:11 2020

@author: LT00U
"""


import numpy as np
import matplotlib.pyplot as plt
 



height = [35, 45, 95, 70]
bars = ('Lonzo Ball', 'Loren Gray', 'Ben Grudzien', 'George Lopez')
y_pos = np.arange(len(bars))
plt.bar(y_pos, height, color=(0.5, 0.5, 0.5, 0.5))
plt.xticks(y_pos, bars)
plt.show()
plt.bar(y_pos, height, color=['blue', 'red', 'green', 'yellow',])
plt.xticks(y_pos, bars)
plt.show()


