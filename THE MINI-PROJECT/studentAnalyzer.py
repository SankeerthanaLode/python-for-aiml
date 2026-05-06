import pandas as pd

data = {
    "name" : ["ram", "ani", "chinnu", "pandu", "rosa"],
    "marks" : [89, 97, 87, 76, 45],
    "age" : [21, 20, 20, 20, 21]
}

df = pd.DataFrame(data)

print("Students who got more than 75 are: ")
high = df.loc[df["marks"] > 75, "name"]
print(high)

print("Average marks area: ",df["marks"].mean())

topper = df.loc[df["marks"].idxmax(), "name"]
print("The topper is: ",topper)

df["status"] = df["marks"] > 50