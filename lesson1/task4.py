f, s, t = map(int, input("Input three numbers: ").split())
if s < f < t or s > f > t:
    print("First")
elif f < s < t or f > s > t:
    print("Second")
elif f < t < s or s < t < f:
    print("Third")
