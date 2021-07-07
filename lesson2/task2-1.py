# Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов(n) вводится с клавиатуры.
n = int(input("Input number of elements to sum up: "))
progression = [1, -0.5, 0.25, -0.125]
q = progression[1] / progression[0]
last = progression[0] * (q ** (n - 1))
result = (progression[0] * (q ** n - 1)) / (q - 1)
print(f"Sum is {result}")
