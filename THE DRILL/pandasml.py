import pandas as pd

data = {
    "name": ["A", "B", "C", "D"],
    "marks": [85, 90, 78, 45]
}

df = pd.DataFrame(data)

print(df)
print()
print(df["marks"])

print("Students with marks greater than 80: ")
result = df.loc[df["marks"] > 80, "name"]
print(result)

print("Average marks are: ", df["marks"].mean())