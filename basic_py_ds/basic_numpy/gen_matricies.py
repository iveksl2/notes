import numpy as np

np.array([1,2,3]) # manual

Z = np.zeros(10)

Z = np.zeros((10, 10)) # tuple as argument

R = np.random.random((10, 10)) # uniformily distributed btwn 0 and 1

G = np.random.randn(10, 10) # this is the only true for randn, others are passes as tuple

G.mean()

G.var()



