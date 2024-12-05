import numpy as np
import pandas as pd

# Panda has two types of data structures - Series and Dataframe
# Series is a one directional array (read numpy repository) having indexes, only stores a single column or single row
# Dataframe is a tabular spreadsheet (just like Microsoft Excel), representing various rows and columns. It is two dimensional.

a = {
    "name": ["Rah", "Jgder", "Av", "Ja"],
    "marks": [34, 38, 40, 39],
    "city": ["Kolkata", "Haryana", "Delhi", "America"]
}

# Data Frame is like an excel sheet, used to analyze big data
b = pd.DataFrame(a)      # It creates an index number given to each column
print(b)

# saves this data into a csv file, and 'index=False' will remove the index number
b.to_csv("marksheet.csv", index=False)
