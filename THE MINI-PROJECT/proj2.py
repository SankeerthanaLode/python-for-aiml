import numpy as np

marks = np.array([56, 78, 89, 58, 79])

avg = np.mean(marks)
print("Average marks: ", avg)

count = np.sum(marks > avg)
print("Number of students who got more than average: ", count)

print("Highest marks: ", np.max(marks))
print("Lowest marks: ", np.min(marks))