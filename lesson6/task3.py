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
min_arr = [None, None]
max_arr = [None, None]
for index, i in enumerate(random_numbers):
    if min_arr[0] is None or min_arr[0] > i:
        min_arr[0] = i
        min_arr[1] = index
    if max_arr[0] is None or max_arr[0] < i:
        max_arr[0] = i
        max_arr[1] = index
random_numbers[min_arr[1]] = max_arr[0]
random_numbers[max_arr[1]] = min_arr[0]
print((min_arr[1]) * "_____" + "|")
print((max_arr[1]) * "_____" + "|")
print(random_numbers)
print(f"Min is {min_arr[0]}")
print(f"Max is {max_arr[0]}")

show_size(random_numbers)
show_size(min_arr)
show_size(max_arr)
print(
    f"Total size = {sys.getsizeof(random_numbers) + sys.getsizeof(min_arr) + sys.getsizeof(max_arr)}")

# Python: 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]
# Platform: win32
# Total size = 328
#  type= <class 'list'>, size= 184, object= [956, 558, 994, 977, 210, 687, 226, 785, 545, 994]
# 	 type= <class 'int'>, size= 28, object= 956
# 	 type= <class 'int'>, size= 28, object= 558
# 	 type= <class 'int'>, size= 28, object= 994
# 	 type= <class 'int'>, size= 28, object= 977
# 	 type= <class 'int'>, size= 28, object= 210
# 	 type= <class 'int'>, size= 28, object= 687
# 	 type= <class 'int'>, size= 28, object= 226
# 	 type= <class 'int'>, size= 28, object= 785
# 	 type= <class 'int'>, size= 28, object= 545
# 	 type= <class 'int'>, size= 28, object= 994
#  type= <class 'list'>, size= 72, object= [210, 2]
# 	 type= <class 'int'>, size= 28, object= 210
# 	 type= <class 'int'>, size= 28, object= 2
#  type= <class 'list'>, size= 72, object= [994, 4]
# 	 type= <class 'int'>, size= 28, object= 994
# 	 type= <class 'int'>, size= 28, object= 4

# Вывод: первый вариант с обычными переменными занимает меньше места,
# чем строки или массивы поскольку сами типы данных весят меньше.
# Строки хранят информацию о счетчике ссылок и типе
# А массивы хранят информацию обо всех элементах и их индексах
# https://habr.com/ru/company/mailru/blog/336156/
