import numpy as nm
import pandas as pd

a = {
    "Place": ["Antartica", "AP", "Karnatka", "Europe", "Plaza"],
    "PINCODE": [122002, 200422, 234546, 342422, 112113]
}

b = pd.DataFrame(a)

# Changes the index style
b.index = ["one", "two", "three", "four", "five"]
print(b)
