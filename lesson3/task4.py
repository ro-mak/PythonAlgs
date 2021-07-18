# В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
from random import randint

random_numbers = [randint(-100, 10) for i in range(0, 20)]
max_sub_zero = None
max_sub_zero_index = None
for index, i in enumerate(random_numbers):
    if max_sub_zero is None and i < 0 or (0 > i > max_sub_zero):
        max_sub_zero = i
        max_sub_zero_index = index
print(random_numbers)
print(f"Max sub zero number: {max_sub_zero} is at index: {max_sub_zero_index}")
