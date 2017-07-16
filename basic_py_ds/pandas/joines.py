import pandas as pd

t1 = pd.read_csv('table1.csv')
t2 = pd.read_csv('table2.csv')

m = pd.merge(t1, t2, on = 'user_id') # will use row index if on is not specified, can join on more

t1.merge(t2, on = 'user_id')
