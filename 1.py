with open('F1.txt', 'w') as f1:
    while True:
        line = input("Введите строку (пустая строка для завершения ввода): ")
        if not line:
            break
        f1.write(line + '\n')

with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
    for line in f1:
        if line.strip().endswith('А'):
            f2.write(line)

print("Программа завершена.")