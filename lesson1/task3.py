print("Стороны:")
a, b, c = map(float, input("a b c: ").split())
if a + b > c and a + c > b and b + c > a:
    triangle_type = ""
    if a == b and b == c and c == a:
        triangle_type = "Равносторонний "
    elif a == b and b != c or a == c and c != b or b == c and c != a:
        triangle_type = "Равнобедренный "
    else:
        triangle_type = "Разносторонний "
    print(f"{triangle_type}Треугольник существует")
else:
    print("Треугольник не существует")
