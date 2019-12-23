import pandas as pd
import matplotlib.pyplot as plt

'''df = pd.DataFrame({'x': [10.4, 8, 10, 7, 7, 10, 9, 9],
                   'y': [6, 4, 5, 5, 7, 10, 9, 9]})
mass = [i for i in range(64) ]
print(mass)

df.plot()
plt.show()'''

import re
date = ['31.12.1943','31.12.1946','31.12.1966','31.12.1976','31.12.1987']
df = pd.DataFrame()
df['Date'] = date
print(next(iter(df[df['Date']=='31.12.1946'].index)))
print(df.loc[[i for i in range(1,4)]])
