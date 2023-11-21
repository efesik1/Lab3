with open('subjects.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

subjects_dict = {}

for line in lines:
    parts = line.split(':')
    subject = parts[0].strip()
    details = parts[1].split()

    total_lectures = total_practicals = total_labs = 0

    for detail in details:
        if '(л)' in detail:
            total_lectures += int(detail.split('(л)')[0])
        elif '(пр)' in detail:
            total_practicals += int(detail.split('(пр)')[0])
        elif '(лаб)' in detail:
            total_labs += int(detail.split('(лаб)')[0])

    total_lessons = total_lectures + total_practicals + total_labs

    subjects_dict[subject] = total_lessons

print(subjects_dict)