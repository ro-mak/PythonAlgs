import sys
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
from random import randint

print()
print()
print()
print(f"Python: {sys.version}")
print(f"Platform: {sys.platform}")
print()
print()
print()


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

# Python: 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]
# Platform: win32
# Total size = 292
# type= <class 'list'>, size= 184, object= [93, 541, 941, 560, 444, 688, 952, 725, 841, 376]
#  type= <class 'int'>, size= 28, object= 93
#  type= <class 'int'>, size= 28, object= 541
#  type= <class 'int'>, size= 28, object= 941
#  type= <class 'int'>, size= 28, object= 560
#  type= <class 'int'>, size= 28, object= 444
#  type= <class 'int'>, size= 28, object= 688
#  type= <class 'int'>, size= 28, object= 952
#  type= <class 'int'>, size= 28, object= 725
#  type= <class 'int'>, size= 28, object= 841
#  type= <class 'int'>, size= 28, object= 376
# type= <class 'int'>, size= 28, object= 93
# type= <class 'int'>, size= 28, object= 6
# type= <class 'int'>, size= 28, object= 952
# type= <class 'int'>, size= 24, object= 0
