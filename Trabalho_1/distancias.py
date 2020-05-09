# import csv

import numpy as np


data = np.genfromtxt('iris_log.dat',
                     encoding='ASCII',
                     names=True,
                     dtype=None,
                     delimiter=' ')

# print(data)
