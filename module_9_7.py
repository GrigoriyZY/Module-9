# Домашнее задание по теме "Декораторы"

def is_prime(func):

    def wrapper(*args):
        number = func(*args)
        if number <= 1:
            print('Число Составное.')
            return number
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                print('Число составное.')
                return number
        print('Число простое.')
        return number
    return wrapper

@is_prime
def sum_three(a: int, b: int, c: int):
    summa = a + b + c
    return summa


result = sum_three(2, 3, 6)
print(result)

result = sum_three(7, 5, 16)
print(result)
