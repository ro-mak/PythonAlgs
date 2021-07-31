from collections import OrderedDict
from collections import deque

hex_numbers = OrderedDict(
    {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 8: "8", 9: "9", 10: "A", 11: "B", 12: "C", 13: "D",
     14: "E", 15: "F"})
hex_numbers_reversed = {value: key for (key, value) in hex_numbers.items()}
numbers = input("Input two hex numbers: ").split()
number1_length = len(numbers[0])
number2_length = len(numbers[1])
max_number_length = number1_length if number1_length > number2_length else number2_length
number1 = dict()
number2 = dict()
for i in range(0, max_number_length):
    number1[i] = "0"
    number2[i] = "0"
for i in range(max_number_length - len(numbers[0]), max_number_length):
    number1[i] = numbers[0][i - max_number_length + len(numbers[0])]
for i in range(max_number_length - len(numbers[1]), max_number_length):
    number2[i] = numbers[1][i - max_number_length + len(numbers[1])]
hex_sum = deque()
dec_1 = 0
dec_2 = 0
for i in range(max_number_length-1, -1, -1):
    power_1 = (16 ** (max_number_length - 1 - i))
    converted_1 = hex_numbers_reversed[number1[i]]
    power_2 = (16 ** (max_number_length - 1 - i))
    converted_2 = hex_numbers_reversed[number2[i]]
    dec_1 += converted_1 * power_1
    dec_2 += converted_2 * power_2
dec_sum = dec_1 + dec_2
print(f"Decimal sum= {dec_sum}")
r = dec_sum

while r > 0:
    hex_sum.appendleft(hex_numbers[r % 16])
    r //= 16
print(hex_sum)
