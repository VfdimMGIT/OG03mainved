import math

print("Выберите метод вычисления площади параллелограмма:")
print("1. Через основание и высоту")
print("2. Через две стороны и угол между ними")

choice = input("Введите номер метода (1 или 2): ")

if choice == '1':
    base = float(input("Введите длину основания: "))
    height = float(input("Введите высоту: "))
    area = base * height
    print(f"Площадь параллелограмма: {area:.2f}")
elif choice == '2':
    side1 = float(input("Введите длину первой стороны: "))
    side2 = float(input("Введите длину второй стороны: "))
    angle = float(input("Введите угол между сторонами (в градусах): "))
    radians_angle = math.radians(angle)
    area = side1 * side2 * math.sin(radians_angle)
    print(f"Площадь параллелограмма: {area:.2f}")
else:
    print("Ошибка: выбран неверный метод")

# Добавляем изменение
    def area_square_area(a):
        S_s = a ** 2
        return S_s