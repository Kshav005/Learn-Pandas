import numpy as np
import pandas as pd

ser = pd.Series(np.random.rand(34))     # Gives series of numbers from 0 to 34
print(ser)

# Creating a dataframe
# Gives a dataframe of 350 rows and 10 columns
df = pd.DataFrame(np.random.rand(350, 10), index=np.arange(350))

# Changing information in 2nd column and 3rd row
df[2][3] = "String"
print(df)

# Printing index (rows)
a = df.index

# Printing the number of columns
b = df.columns

# Changing the dataframe into a numpy array
print(df.to_numpy())

# Transposing the dataframe
c = df.T

# Sorting the dataframe through index, as it is already sorted in ascending order, we will be sorting to decreasing order
# Sorting Rows
d = df.sort_index(axis=0, ascending=False)

# Sorting Columns
e = df.sort_index(axis=1, ascending=False)

# Printing a column in form of series
print(df[1])

# Copying the whole data into another variable
newdf = df.copy()

# Hence there will be change in "newdf" and not in "df" as a copy has been made of that "df"
newdf[0][2] = "Nothing"
