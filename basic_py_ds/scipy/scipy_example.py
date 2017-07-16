import numpy as np
from scipy.stats import norm
from scipy.stats import multivariate_normal as mvn

norm.pdf(0)

norm.pdf(0, loc=5, scale=10) #sd=10, var=100

r = np.random.randn(10)

norm.pdf(r)


norm.logpdf(r)

norm.cdf(r) # integral form -inf to inf, but it is not actually solvable. must computer cumlative density numerically under the hood

r = np.random.randn(10000)

plt.hist(r, bins = 100); plt.show()

r = 10*np.random.randn(10000) + 5

plt.hist(r, bins = 100); plt.show()

# lets sample from a 2D gaussian (each dimension independent of other)

r = np.random.randn(10000, 2)

plt.scatter(r[:,0], r[:,1]);plt.show()

# ellipses
r[:,1] = 5*r[:,1] + 2

plt.scatter(r[:,0], r[:,1])
plt.axis('equal')
plt.show()

# sample from gaussian distributions not independent of each other
cov = np.array([[1,.8], [.8, 3]])

mu = np.array([0,2])

r = mvn.rvs(mean=mu, cov=cov, size=1000)

plt.scatter(r[:,0], r[:,1]); plt.axis('equal');plt.show()

# scipy.io.loadmat 
# interesting signal modules scipy.signals
# 

x = np.linspace(0, 100, 10000)

y = np.sin(x) + np.sin(3*x) + np.sin(5*x)

plt.plot(y); plt.show()

Y = np.fft.fft(y)

plt.plot(np.abs(Y));plt.show()
