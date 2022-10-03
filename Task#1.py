# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# 6782 -> 23
# 0,56 -> 11

num = str(input('Number: '))
i = 0
for elem in num:
    if elem.isdigit():
        i += int(elem)
print("The sum of digits in this number =", i)