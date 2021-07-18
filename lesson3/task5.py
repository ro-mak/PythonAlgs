# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
from random import randint

random_numbers = [randint(-100, 100) for i in range(0, 20)]

min = None
min_index = None
max = None
max_index = None
for index, i in enumerate(random_numbers):
    if min is None or min > i:
        min = i
        min_index = index
    if max is None or max < i:
        max = i
        max_index = index
sum = 0
for index, j in enumerate(random_numbers):
    if index != min_index and index != max_index:
        sum += j
print(random_numbers)
print(f"Sum of all elements between {min} and {max} is {sum}")
