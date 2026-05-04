marks = [45, 67, 56, 89, 64]

marks.append(99)

print(marks[0], marks[-1])

for mark in marks:
    if mark > 50:
        print(mark)