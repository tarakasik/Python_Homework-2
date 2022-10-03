# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.
# Значения N, a и b вводит пользователь с клавиатуры.


def multi(a, b, origin_list):
    return origin_list[a - 1] * origin_list[b - 1]

def sequence(n):
    numbers = []
    for i in range(-n, n + 1):
        numbers.append(i)
    return numbers

n = int(input("N: "))
a = int(input("a: "))
b = int(input("b: "))
num_list = sequence(n)
print(f"a * b = {num_list[a - 1]} * {num_list[b - 1]} = {multi(a, b, num_list)}")
