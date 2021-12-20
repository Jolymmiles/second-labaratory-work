import math

num_of_task = 0
while num_of_task != -1:
    num_of_task = int(input())
    # Задание 1
    if num_of_task == 1:
        a = float(5 * math.cos(7.4 * math.pi))
        b = float(math.sin(2.8 * math.pi) * 15)
        c = int(math.sqrt(a + b) * 465)
        print('Это будет = ', c)
    # Задание 2
    elif num_of_task == 2:
        a = float(3 * math.cos(1.7 * math.pi))
        b = float(math.sin(2.9 * math.pi) * 5)
        c = int(math.sqrt(a + b) * 591)
        print('Это будет = ', c)

    # Задание 3
    elif num_of_task == 3:
        a = float(4 * math.cos(1.6 * math.pi))
        b = float(math.sin(1.9 * math.pi) * 9)
        c = int(math.sqrt(a - b) * 630)
        print('Это будет = ', c)

    # Задание 4
    elif num_of_task == 4:
        a = float(11 * math.cos(6.35 * math.pi))
        b = float(math.sin(2.2 * math.pi) * 8)
        c = int(math.sqrt(a - b) * 987)
        print('Это будет = ', c)

    # Задание 5
    elif num_of_task == 5:
        a = float(7 * math.sin(6.85 * math.pi))
        b = float(math.cos(3.3 * math.pi) * 3)
        c = int(math.sqrt(a - b) * 865)
        print('Это будет = ', c)

    # Задание 6
    elif num_of_task == 6:
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
