students = [
    {"name" : "Sankeerthana", "marks" : 99},
    {"name" : "Harsha", "marks" : 89},
    {"name" : "Anitha", "marks" : 87},
    {"name" : "Ramesh", "marks" : 86},
    {"name" : "Pandu", "marks" : 70},
]

for data in students:
    if data["marks"] > 70:
        print(data["name"])

new_item = {"name" : "Chinnu", "marks" : 80}

students.append(new_item)

count = 0

for data in students:
    count = count + data["marks"]

print("Average: ",count/6)

topper = max(students, key = lambda x : x["marks"])
print(topper["name"])
