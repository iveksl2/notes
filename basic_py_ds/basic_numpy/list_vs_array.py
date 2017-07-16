import numpy as np

L = [1,2,3]

A = np.array([1,2,3])

for e in L:
    print(e)

for e in A:
    print(e)

L.append(4)

A.append(4) # error

L = L + [5]

A = A + [4, 5] # cant add numpy arrays

L2 = []

for e in L:
    L2.append(e + e)

A + A # lists do concotentatoin, this does vector addition

2*A # scalar, otherwise need to do a for loop with list
2*L # doubles the length of list

# numpy -> operations typically act elementwise (vector) like in R   
    # for loops tend to be slower, so avoid when possible





