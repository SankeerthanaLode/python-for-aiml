import numpy as np

students = [
    {"name": "A", "marks": [85, 90, 78]},
    {"name": "B", "marks": [70, 60, 75]},
    {"name": "C", "marks": [67, 57, 95]},
    {"name": "D", "marks": [45, 87, 85]},
    {"name": "E", "marks": [96, 97, 80]},
]

for student in students:
    student["marks"] = np.array(student["marks"])
    student["average"] = student["marks"].mean()

for student in students:
    print("Student: ",student["name"]," Average marks: ", student["average"])

averages_list = [student["average"] for student in students]
student_averages = np.array(averages_list)
class_avg = student_averages.mean()

print("Average of the class is : ", class_avg)

topper_index = np.argmax(student_averages)
topper = students[topper_index]["name"]

print("Topper:", topper)

count = np.sum(student_averages > class_avg)
print("Number of students who got more than average: ", count)
