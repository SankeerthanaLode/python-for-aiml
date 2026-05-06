import pandas as pd
import numpy as np

data = {
    "name": ["A", "B", "C", "D", "E", "F"],
    "marks": [85, None, 78, 90, None, 88],
    "age": [20, 21, None, 22, 20, None]
}

df = pd.DataFrame(data)

print("Missing values count: ", df.isnull().sum())
df["marks"] = df["marks"].fillna(df["marks"].mean())
df["age"] = df["age"].fillna(df["age"].mean())
print("Filtered data: ")
print(df)