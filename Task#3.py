#Завдання 1
def square_or_power():
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    num3 = float(input("Введіть третє число: "))

    def process_number(num):
        if num >= 0:
            return num ** 2
        else:
            return num ** 4

    result1 = process_number(num1)
    result2 = process_number(num2)
    result3 = process_number(num3)

    print("Результати обробки:")
    print("Число 1:", result1)
    print("Число 2:", result2)
    print("Число 3:", result3)

# Завдання 2
def closer_point_to_origin():
    x1, y1 = map(float, input("Введіть координати точки A (x1, y1): ").split())
    x2, y2 = map(float, input("Введіть координати точки B (x2, y2): ").split())

    distance1 = (x1 ** 2 + y1 ** 2) ** 0.5
    distance2 = (x2 ** 2 + y2 ** 2) ** 0.5

    if distance1 < distance2:
        print("Точка A знаходиться ближче до початку координат.")
    elif distance1 > distance2:
        print("Точка B знаходиться ближче до початку координат.")
    else:
        print("Точки знаходяться на однаковій відстані до початку координат.")

# Завдання 3
def triangle_check():
    angle1 = float(input("Введіть перший кут трикутника (в градусах): "))
    angle2 = float(input("Введіть другий кут трикутника (в градусах): "))

    angle3 = 180 - angle1 - angle2

    if angle1 > 0 and angle2 > 0 and angle3 > 0:
        print("Такий трикутник існує.")
        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            print("Трикутник є прямокутним.")
        else:
            print("Трикутник не є прямокутним.")
    else:
        print("Такий трикутник не існує.")

# Завдання 4
def replace_numbers():
    x = float(input("Введіть перше число: "))
    y = float(input("Введіть друге число: "))

    if x != y:
        x, y = max(x, y), max(x, y)
    else:
        x, y = 0, 0

    print("Результат:")
    print("x =", x)
    print("y =", y)

# Завдання 5
def point_location():
    x, y = map(float, input("Введіть координати точки A (x, y): ").split())

    if x == 0 and y == 0:
        print("Точка розташована в початку координат.")
    elif x == 0:
        print("Точка розташована на вісі Y.")
    elif y == 0:
        print("Точка розташована на вісі X.")
    elif x > 0 and y > 0:
        print("Точка розташована в першому квадранті.")
    elif x < 0 and y > 0:
        print("Точка розташована в другому квадранті.")
    elif x < 0 and y < 0:
        print("Точка розташована в третьому квадранті.")
    else:
        print("Точка розташована в четвертому квадранті.")

# Завдання 6
def replace_or_zero():
    a = int(input("Введіть перше ціле число: "))
    b = int(input("Введіть друге ціле число: "))

    if a != b:
        a, b = max(a, b), max(a, b)
    else:
        a, b = 0, 0

    print("Результат:")
    print("a =", a)
    print("b =", b)

# Завдання 7
def count_negative():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))

    count = sum(n < 0 for n in [a, b, c])
    print("Кількість негативних чисел:", count)

# Завдання 8
def count_positive():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))

    count = sum(n > 0 for n in [a, b, c])
    print("Кількість додатніх чисел:", count)

# Завдання 9
def count_integers():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))

    count = sum(n.is_integer() for n in [a, b, c])
    print("Кількість цілих чисел:", count)

# Завдання 10
def divisor_of_numbers():
    a = float(input("Введіть число a: "))
    b = float(input("Введіть число b: "))
    c = float(input("Введіть число c: "))
    k = float(input("Введіть число k: "))

    divisors = [num for num in [a, b, c] if num % k == 0]
    print("Число k є дільником чисел:", divisors)


# Виклик функцій для виконання завдань
square_or_power()
closer_point_to_origin()
triangle_check()
replace_numbers()
point_location()
replace_or_zero()
count_negative()
count_positive()
count_integers()
divisor_of_numbers()