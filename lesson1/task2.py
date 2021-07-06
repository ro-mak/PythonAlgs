x, y = map(int, input("Input first coordinates: ").split())
x1, y1 = map(int, input("Input second coordinates: ").split())
k = (y - y1) / (x - x1)
b = y - k * x
print(f"y = {k}x + {b}")
