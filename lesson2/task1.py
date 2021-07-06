# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
number = input("Input natural number: ")
countEven = 0
countOdd = 0
for element in number:
    if int(element) % 2 == 0:
        countEven += 1
    else:
        countOdd += 1
print(f"There are {countEven} even numbers and {countOdd} odd numbers in number {number}")
