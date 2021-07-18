# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint

random_numbers = [randint(0, 1000) for i in range(0, 10)]
print(random_numbers)
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
random_numbers[min_index] = max
random_numbers[max_index] = min
print((min_index) * "_____" + "|")
print((max_index) * "_____" + "|")
print(random_numbers)
print(f"Min is {min}")
print(f"Max is {max}")
