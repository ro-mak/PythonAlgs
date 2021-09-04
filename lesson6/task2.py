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
min_all = "None None"
max_all = "None None"
for index, i in enumerate(random_numbers):
    min = min_all.split()[0]
    if min == "None" or int(min) > i:
        min_all = f"{i} {index}"
    max = max_all.split()[0]
    if max == "None" or int(max) < i:
        max_all = f"{i} {index}"
random_numbers[int(min_all.split()[1])] = int(max_all.split()[0])
random_numbers[int(max_all.split()[1])] = int(min_all.split()[0])
print((int(min_all.split()[1])) * "_____" + "|")
print((int(max_all.split()[1])) * "_____" + "|")
print(random_numbers)
print(f"Min is {int(min_all.split()[0])}")
print(f"Max is {int(max_all.split()[0])}")

show_size(random_numbers)
show_size(min_all)
show_size(max_all)
print(
    f"Total size = {sys.getsizeof(random_numbers) + sys.getsizeof(min_all) + sys.getsizeof(max_all)}")

# Python: 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)]
# Platform: win32
# Total size = 291
#  type= <class 'list'>, size= 184, object= [580, 765, 543, 780, 382, 43, 773, 354, 364, 763]
# 	 type= <class 'int'>, size= 28, object= 580
# 	 type= <class 'int'>, size= 28, object= 765
# 	 type= <class 'int'>, size= 28, object= 543
# 	 type= <class 'int'>, size= 28, object= 780
# 	 type= <class 'int'>, size= 28, object= 382
# 	 type= <class 'int'>, size= 28, object= 43
# 	 type= <class 'int'>, size= 28, object= 773
# 	 type= <class 'int'>, size= 28, object= 354
# 	 type= <class 'int'>, size= 28, object= 364
# 	 type= <class 'int'>, size= 28, object= 763
#  type= <class 'str'>, size= 53, object= 43 3
#  type= <class 'str'>, size= 54, object= 780 5

