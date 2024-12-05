import numpy as np
import pandas as pd

# Make sure you use "loc" function most of the time as it doesn't make changes in the original file, instead it creates another file (copies) and prints the changes you have made in the file

newdf = pd.DataFrame(np.random.rand(350, 10), index=np.arange(
    350))       # Gives a dataframe of 350 rows and 10 columns


# Resetting index
d = newdf.reset_index(drop=True)      # Drops the old index and adds a new one
print(d)

# If you want to add the same value in a particular row
newdf[4] = "Hello"
print(newdf)

# Describe the shape of the dataframe
print(newdf.shape)

# You can get info regarding your data too
print(newdf.info())

# To get where there is not null (Gives False if the value is null)
print(newdf.notnull())

# To get where there is null (Opposite of "notnull", which means that it gives True if the value is null)
print(newdf.isnull())
