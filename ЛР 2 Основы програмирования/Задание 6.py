import math

x = int(input('Введите x ='))
y = int(input('Введите y ='))
z = int(input('Введите z ='))
a = float(x * (math.atan(z) + math.e ** (-(x + 3))))
b = float(1 + math.fabs(y - x) + (((y - x) ** 2) / 2) + (((math.fabs(y - x)) ** 3) / 3))
c = float((1 + math.cos(y - 2)) / ((x ** 4) / 2 + (math.sin(z)) ** 2))
d = float(1 + (math.tan(z / 2)) ** 2)
e = float(1 + (z ** 2 / (3 + (z ** 2) / 5)))
f = float((math.cos(math.atan(1 / 7))) ** 2)
g = float(x - (x ** 2 / math.factorial(3)) + (x ** 5 / math.factorial(5)))
print('a)', a)
print('b)', b)
print('c)', c)
print('d)', d)
print('e)', e)
print('f)', f)
print('g)', g)
