from collections import defaultdict
from collections import ChainMap

numbers = input("Input two hex numbers: ").split()
number1_length = len(numbers[0])
number2_length = len(numbers[1])
max_number_length = number1_length if number1_length > number2_length else number2_length
number1 = defaultdict(lambda x: "0")
number2 = defaultdict(lambda x: "0")
for i in range(0, max_number_length):
    number1[i] = "0"
    number2[i] = "0"
for i in range(max_number_length - len(numbers[0]), max_number_length):
    number1[i] = numbers[0][i - max_number_length + len(numbers[0])]
for i in range(max_number_length - len(numbers[1]), max_number_length):
    number2[i] = numbers[1][i - max_number_length + len(numbers[1])]
print(number1)
print(number2)
