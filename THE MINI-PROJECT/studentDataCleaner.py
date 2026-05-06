import pandas as pd
import numpy as np

data = {
    "name": ["A", "B", "C", "D", "E", "F"],
    "marks": [85, None, 78, 90, None, 88],
    "age": [20, 21, None, 22, 20, None]
}

df = pd.DataFrame(data)

print("The count of the missing values: ",df.isnull().sum())

df["marks"] = df["marks"].fillna(df["marks"].mean())
df["age"] = df["age"].fillna(df["age"].mean())

print("Average marks: ",df["marks"].mean())

topper = df.loc[df["marks"].idxmax(), "name"]
print("The topper is: ", topper)

df["status"] = df["marks"].apply(lambda x : "Pass" if x > 50 else "Fail")

print(df)