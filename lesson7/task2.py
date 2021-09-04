# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
from collections import deque
import random


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


def my_merge_sort(array_to_sort):
    if len(array_to_sort) < 2:
        return array_to_sort[:]
    else:
        middle = int(len(array_to_sort) / 2)
        left = my_merge_sort(array_to_sort[:middle])
        right = my_merge_sort(array_to_sort[middle:])
        return merge(left, right)


array = [i for i in range(10)]
size = len(array)
random.shuffle(array)
print(f"Init:{array}")

print(my_merge_sort(array))
