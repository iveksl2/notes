import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('train.csv')

M = df.as_matrix()

im = M[0, 1:]

im = im.reshape(28, 28)

plt.imshow(im)

plt.show()

iplt.imshow(im, cmap='gray')

plt.imshow(255-im, cmap='gray')


