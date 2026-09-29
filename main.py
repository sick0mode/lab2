from calculator import add, subtract, multiply, divide, is_even, sqrt, power

print("Мини-калькулятор")

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

print("Сумма:", add(a, b))
print("Разность:", subtract(a, b))
print("Произведение:", multiply(a, b))
print("Возведение в степень:", power(a, b))


result = divide(a, b)

if result is None:
    print("Ошибка: деление на ноль")
else:
    print("Результат деления:", result)

number = int(input("Введите число для проверки четности: "))

if is_even(number):
    print("Число четное")
else:
    print("Число нечетное")

number2 = int(input("Введите число для возведения в корень: "))

if number2 > 0:
    print(sqrt(number2))
else:
    print("Число меньше 0")