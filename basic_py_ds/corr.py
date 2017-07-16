import pandas as pd
path = 'http://archive.ics.uci.edu/ml/machine-learning-databases/auto-mpg/auto-mpg.data'

mpg_data = pd.read_csv(path, delim_whitespace=True, header=None,
                    names = ['mpg', 'cylinders', 'displacement','horsepower',
                                    'weight', 'acceleration', 'model_year', 'origin', 'name'],
                                na_values='?')
