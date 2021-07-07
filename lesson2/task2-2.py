# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов(n) вводится с клавиатуры.
n = int(input("Input number of elements to sum up: "))
progression_first = 1
progression_second = -0.5
q = progression_second / progression_first
i = 1
sum = progression_first
while i < n:
    next = progression_first * (q ** i)
    sum += next
    i += 1
print(f"Sum is {sum}")
