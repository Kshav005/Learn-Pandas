import pandas as pd


# Suppose you have a readymade csv file stored in your computer
# Then you can open and read it here, then perform different operations on it
# For example, we created a file named "test.csv"
cd = pd.read_csv("test.csv")


# To read the row using the given row name, use 'var_name["column_name"]'
print(cd["City"])

# To read a particular column at an index, then use 'var_name["column_name"][index]
print(cd["Name"][4])

# To change the value of something in the data
cd["Name"][4] = "Alpha"


# Another method to change the value of something in the data
cd.loc[0, "City"] = 56
print(cd)

# Deleting a row/column in the data
cd.drop(1, axis=1)


# To save the changes
cd.to_csv("test.csv")
