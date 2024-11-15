# Домашнее задание по теме "Генераторные сборки"

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [abs(len(x[0]) - len(x[1])) for x in zip(first, second) if len(x[0]) != len(x[1])]
second_result = [len(first[i]) == len(second[i]) for i in range(len(first))]

print(first_result)
print(second_result)