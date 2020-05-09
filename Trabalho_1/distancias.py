# import csv

import numpy as np


data = np.genfromtxt('iris_log.dat',
                     names=True,
                     dtype=None,
                     delimiter=' ')

class1 = data[0:5]
class2 = data[5:10]
class3 = data[10:15]

class1_center = class1.mean(axis=0)[0:3]
class2_center = class2.mean(axis=0)[0:3]
class3_center = class3.mean(axis=0)[0:3]

print(data)

len_dta = data.shape[0]

for i in range(0, len_dta):
    
    distances = np.array([np.sqrt(((class1_center - data[i][0:3])**2).sum()),
                          np.sqrt(((class2_center - data[i][0:3])**2).sum()),
                          np.sqrt(((class3_center - data[i][0:3])**2).sum())])