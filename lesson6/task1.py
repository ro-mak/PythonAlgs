import sys
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint


def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


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

show_size(random_numbers)
show_size(min)
show_size(min_index)
show_size(max)
show_size(max_index)
print(
    f"Total size = {sys.getsizeof(random_numbers) + sys.getsizeof(min) + sys.getsizeof(min_index) + sys.getsizeof(max) + sys.getsizeof(max_index)}")
