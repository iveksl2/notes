import numpy as np
import pandas as pd
from datetime import datetime

X = []

for line in open('data_2d.csv'):
    row = line.split(',')
    sample = map(float, row)
    X.append(sample)

X = np.array(X)

x = pd.read_csv('data_2d.csv', header=None) # need to specify headerless

M = x.as_matrix() # actualy a numpy array

x.iloc[0]

x.ix[0] # deprecated

type( x.iloc[0])

x[[0,2]]

x[x[0] < 5]

df = pd.read_csv('international-airline-passengers.csv', engine = 'python', skipfooter = 3) # no header necessary, skip last rows (requires engine since not compatible with C)

df.columns = ['month', 'passangers']

df.passangers # would not have worked

df['ones'] = 1

datetime.datetime(1949, 5, 1, 0, 0)

df['dt'] = df.apply(lambda row: datetime.strptime(row['month'], '%Y-%m'), axis = 1)


