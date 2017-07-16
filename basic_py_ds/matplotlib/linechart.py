import matplotlib.pyplot as plt

x = np.linspace(0, 10, 10)

y = np.sin(x)

plt.plot(x, y)

plt.show()

plt.plot(x, y)
plt.xlabel('time')
plt.ylabel('some function of time')
plt.title('my cool chart')

plt.show()

x = np.linspace(0, 10, 100)

y = np.sin(x)

plt.plot(x, y)

plt.show()


