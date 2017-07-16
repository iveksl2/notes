import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

A = pd.read_csv('data_1d.csv', header=None).as_matrix()

x = A[:,0]
y = A[:,1]

plt.scatter(x, y)

plt.show()

x_line = np.linspace(0, 100, 100)

y_line = 2*x_line + 1

plt.scatter(x, y)
plt.plot(x_line, y_line)
plt.show()

plt.hist(x)
plt.show()

R = np.random.random(10000)

plt.hist(R)

plt.show()

plt.hist(R, bins = 20); plt.show()

y_actual = x*x + 1



