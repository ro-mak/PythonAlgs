# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, второй массив надо заполнить значениями 0, 3, 4, 5
# (помните, что индексация начинается с нуля), т. к. именно в этих позициях первого массива стоят четные числа.
first_array = [i * 3 for i in range(1, 13)]
second_array = [index for index, j in enumerate(first_array) if j % 2 == 0]
print(first_array)
print(second_array)
