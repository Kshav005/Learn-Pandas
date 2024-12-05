import numpy as np
import pandas as pd


newdf = pd.DataFrame(np.random.rand(350, 10), index=np.arange(
    350))       # Gives a dataframe of 350 rows and 10 columns


# To get specific set of row and column
a3 = newdf.loc[[1, 2], [4, 5]]

# To get only columns use a colon (:)
a2 = newdf.loc[:, [2, 8]]

# To get only rows
a1 = newdf.loc[[1, 3], :]

# To get rows in which the value is greater than some integer
a0 = newdf.loc[(newdf[1] < 0.4) & (newdf[3] < 0.1)]
print(a0)

# To get a value from a row and column
a00 = newdf.iloc[5, 3]
print(f"The value at 5th Column and 3rd Row = {a00}")

# Dropping a row
b = newdf.drop([0])
print(b)

# Dropping a column
# Adding "implace" will edit all this in the original "newdf"
newdf.drop(3, axis=1, inplace=True)

print(newdf)
