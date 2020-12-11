from matplotlib import pyplot as plt
import numpy as np
import sys


with open('data_4.txt', 'r') as f:
    data=[]
    for i in range(2000):
        data.append(float(f.readline()))
    # data_temp = f.readlines()
    # def f(x):
    #     return float(x.strip())
    # data = list(map(f, data_temp))
print(len(data))

from collections import deque

temp = deque(maxlen=10)
mean_data = []
for j in range(2000):
    temp.append(data[j])
    mean_data.append(sum(temp)/len(temp))

plt.plot(mean_data, label='10 DOF')
plt.xlabel('episodes')
plt.ylabel('mean rewards')
plt.legend(loc='lower right')
plt.savefig('10_dof_reward.svg')
plt.show()
