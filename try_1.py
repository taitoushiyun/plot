import numpy as np


with open('data_0.txt', 'r') as f:
    def tf(x):
        return float(x.strip())
    data = list(map(tf, f.readlines()))
temp = 0
iter_list = []
for i in range(500):
    temp += data[i]
    iter_step = temp // 256
    iter_list.append(iter_step)
from matplotlib import pyplot as plt

plt.plot(iter_list)
print(iter_step)
plt.show()