grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = list(students)
students.sort()
average_value = {}
for a in range(len(students)):
    sum = 0
    for b in range(len(grades[a])):
        sum = sum + grades[a][b]
    average_value[students[a]] = sum / len(grades[a])
print(average_value)