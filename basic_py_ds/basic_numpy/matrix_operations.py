import numpy as np

# dot product is matrix multiplication!
# in numpy asteriks element by element. dot -> matrix multiplication
# isn't a well defined symbol for element wise multiplication

A = np.array([[1,2], [3,4]])

Ainv = np.linalg.inv(A)

A.dot(Ainv) # result: identity matrix 

np.linalg.det(A) 

np.diag(A)

np.diag([1,2])

a = np.array([1,2])
b = np.array([3,4])

np.outer(a, b)

np.inner(a, b) # same as a.dot(b)

np.diag(A).sum()

np.trace(A) # sum of the diaganols. ^ same as above

x = np.random.randn(100, 3)

cov = np.cov(x)

cov = np.cov(x.T)

np.linalg.eigh(cov)

np.linalg.eig(cov) # eigenvecors and eigenvalues



