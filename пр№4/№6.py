import math
x = float(input("Введите число: "))
r = math.radians(x)
result = math.sin(r) + math.cos(r) + math.tan(r) ** 2
print(result)
