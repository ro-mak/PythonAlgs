# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843
number = input("Input number: ")
l = len(number)
result = ""
while l > 0:
    result += number[l - 1]
    l -= 1
print(result)
