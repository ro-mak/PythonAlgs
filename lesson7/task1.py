# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

import random
import sys

array = [i for i in range(-100, 100)]
size = len(array)
random.shuffle(array)
print(f"Init:{array}")

n = 1
count = 0
isSorted = False
while n < len(array):
    if isSorted:
        break
    isSorted = True
    for i in range(len(array) - n):
        count += 1
      #  print(f"n = {n} i = {i} first={array[i]} second={array[i+1]} {array}")
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            isSorted = False

    n += 1

print(array)
print(f"Elements: {size} Iter: {count} Memory: {sys.getsizeof(n) + sys.getsizeof(isSorted)}")
