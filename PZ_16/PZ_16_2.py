'''
Создание базового класса "Фигура" и его наследование для создания классов
"Квадрат", "Прямоугольник" и "Круг". Класс "Фигура" будет иметь общие методы,
такие как вычисление площади и периметра, а классы-наследники будут иметь
специфичные методы и свойства.
'''
import math

class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

class Square(Shape):
    def __init__(self, side_length):
        if side_length <= 0:
            print("Предупреждение: длина стороны должна быть положительной. Установлена в 0.")
            side_length = 0.0
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length
    
    def diagonal(self):
        return self.side_length * math.sqrt(2)


class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0:
            print("Предупреждение: ширина должна быть положительной. Установлена в 0.")
            width = 0.0
        if height <= 0:
            print("Предупреждение: высота должна быть положительной. Установлена в 0.")
            height = 0.0
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def is_square(self):
        return self.width == self.height


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            print("Предупреждение: радиус должен быть положительным. Установлен в 0.")
            radius = 0.0
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def diameter(self):
        return 2 * self.radius

square = Square(5)
print(f"Квадрат: сторона = {square.side_length}")
print(f"Площадь: {square.area()}")
print(f"Периметр: {square.perimeter()}")
print(f"Диагональ: {square.diagonal():.2f}\n")

rectangle = Rectangle(4, 6)
print(f"Прямоугольник: ширина = {rectangle.width}, высота = {rectangle.height}")
print(f"Площадь: {rectangle.area()}")
print(f"Периметр: {rectangle.perimeter()}")
print(f"Является квадратом? {rectangle.is_square()}\n")

circle = Circle(3)
print(f"Круг: радиус = {circle.radius}")
print(f"Площадь: {circle.area():.2f}")
print(f"Периметр (длина окружности): {circle.perimeter():.2f}")
print(f"Диаметр: {circle.diameter()}")

print("\nПример с отрицательным значением")
invalid_rectangle = Rectangle(-5, 10)
print(f"Прямоугольник: ширина = {invalid_rectangle.width}, высота = {invalid_rectangle.height}")
print(f"Площадь: {invalid_rectangle.area()}") 