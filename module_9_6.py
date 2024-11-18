# Домашнее задание по теме "Генераторы"

def all_variants(string: str):
    x = 1
    while x <= len(string):
        i = 0
        while i < len(string)-x+1:
            yield string[i: i + x]
            i += 1
        x += 1


a = all_variants("abcde")
for i in a:
    print(i)
