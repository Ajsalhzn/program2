marks = [450, 380, 420, 390, 410, 370]
print(marks)

unique_marks = sorted(set(marks))
print(unique_marks)

if len(unique_marks) >= 3:
    third_lowest = unique_marks[2]
    print("third lowest total marks:", third_lowest)
else:
    print("Not enough data to find third lowest marks")