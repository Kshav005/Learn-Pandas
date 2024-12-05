import numpy as np
import pandas as pd

a = {"A": [1, 2],
     "B": [4, 5],
     "C": [7, 8]}

a = pd.DataFrame(a)

# Getting the mean value
mean = a.mean()

# Getting correlation matrix
cor = a.corr()

# Counting the total items
coun = a.count()

# Getting the maximum value
mx = a.max()

# Getting the minimum value
mn = a.min()

# Getting the median value
med = a.median()

# Getting the standard deviation
stdev = a.std()

print(f"The mean => \n{mean}\nThe median => \n{med}\nThe max => \n{mx}\nThe min => \n{mn}\nThe correlation => \n{cor}\nThe standard deviation => \n{stdev}\nThe total count => \n{coun}")
