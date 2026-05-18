import pandas as pd

data = {
    "name": ["A", "B", "C", "D"],
    "city": ["Hyd", "Delhi", "Mumbai", "Hyd"]
}

df = pd.DataFrame(data)

df["label_encoding"] = df["city"].astype("category").cat.codes

print(df)

one_hot_encoded = pd.get_dummies(df["city"])

print(one_hot_encoded)