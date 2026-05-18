import pandas as pd

data = {
    "name": ["A", "B", "C", "D", "E"],
    "marks": [85, 90, 78, 92, 88],
    "city": ["Hyd", "Hyd", "Delhi", "Delhi", "Hyd"]
}

df = pd.DataFrame(data)

print(df.groupby("city")["marks"].agg(["mean", "max", "min"]))
print()
print(df.groupby("city")["name"].count())
print()

city_avg = df.groupby("city")["marks"].mean()

top_city = city_avg.idxmax()

print("City with highest average marks:", top_city)