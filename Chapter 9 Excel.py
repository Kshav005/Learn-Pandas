import pandas as pd
import numpy as np

# Opening an excel file
# We can open the excel file by installing a module called "xlrd"/"openpyxl".
a = pd.read_excel("Test2.xlsx")

# If you want to access other sheet then enter the sheet name
b = pd.read_excel("Test2.xlsx", sheet_name="Sheet2")

print(a)
print(b)
