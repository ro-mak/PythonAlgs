first_array = [i * 3 for i in range(1, 13)]
second_array = [index for index, j in enumerate(first_array) if j % 2 == 0]
print(first_array)
print(second_array)
