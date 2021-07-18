# Определить, какое число в массиве встречается чаще всего.
from random import randint

random_numbers = [randint(0, 10) for i in range(0, 20)]
repeats = {0: 0}
for i in random_numbers:
    try:
        repeats[i] is None
    except KeyError:
        repeats[i] = 1
    else:
        repeats[i] += 1
max = None
result = None
for key, value in repeats.items():
    if max is None or max < value:
        max = value
        result = key
print(random_numbers)
print(repeats)
print(f"Number {result} repeats {max} times")
