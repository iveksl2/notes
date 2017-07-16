import numpy as np

a = np.array([1,2])
b = np.array([2,1])

dot = 0

for e,f in zip(a, b):
    dot += e*f

dot

a*b

np.sum(a*b)

(a*b).sum()

np.dot(a, b) # instance method of numpy class. can call it on the instance itself 

a.dot(b)

b.dot(a)

amg = np.sqrt(a*a.sum())

amg

amag= np.linalg.norm(a)

amag

cosangle = a.dot(b) / (np.linalg.norm(a) * np.linalg.norm(b))
