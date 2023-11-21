with open('students.txt', 'r',  encoding='utf-8') as file:
    lines = file.readlines()

names = []
grades = []

for line in lines:
    parts = line.split()
    if len(parts) == 2:
        names.append(parts[0])
        grades.append(float(parts[1]))

low_grades = [names[i] for i in range(len(names)) if 4 <= grades[i] < 6]
medium_grades = [names[i] for i in range(len(names)) if 6 <= grades[i] < 8]
high_grades = [names[i] for i in range(len(names)) if grades[i] >= 8]

print("Студенты с баллами от 4 до 6:", low_grades)
print("Студенты с баллами от 6 до 8:", medium_grades)
print("Студенты с баллами выше 8:", high_grades)

max_grade_index = grades.index(max(grades))
print("Студент с максимальным средним баллом:", names[max_grade_index])