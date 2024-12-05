import numpy as np
import pandas as pd

# Row is accessed by index numbers
# Column is accessed by column names

a = {
    "Name": ["Jk", "Rm", "Har", "Nam", "Me", "You", "Potter", "Osb", "Teach"],
    "City": ["Delhi", "De", "Delh", "Delh", "De", "Delhi", "Del", "D", "Del"],
    "Marks": [32, 21, 54, 74, 12, 4, 45, 5, 12]
}

b = pd.DataFrame(a)

# If you want to display only first 4 rows
print(b.head(4))

# If you want to display only last 3 rows
print(b.tail(3))

# If you want to find various info regarding the marks/numerical values in your data like mean,75%,max,etc
print(b.describe())

# You can also use various arguments to specify certain values
# 'percentile' is used to specify the percentile values in a form of list. Make sure they are between 0 and 1
print(b.describe(percentiles=[.5, .7, .99]))