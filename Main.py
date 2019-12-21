import pandas as pd
import matplotlib.pyplot as plt

'''df = pd.DataFrame({'x': [10.4, 8, 10, 7, 7, 10, 9, 9],
                   'y': [6, 4, 5, 5, 7, 10, 9, 9]})
mass = [i for i in range(64) ]
print(mass)

df.plot()
plt.show()'''

import re
string = 'декабря'
date = '31 декабря 1995'
#result = re.sub(r'\D'+string+'\D','.12.',date)
result = re.findall(r'\D[а-я]',date)
print(result)