import numpy as np

# prob: Admission fee at small fair is 1.5 for children and 4.00 for adults. 
# On a certain day, 2200 people enter the fair and $5050 is collected. How many Children and how many adults attended

x + y = 2200
1.5*x + 4*y = 5050

A = np.array([[1,1],[1.5,4]])
b = np.array([2200, 5050])

np.linalg.solve(A, b)
