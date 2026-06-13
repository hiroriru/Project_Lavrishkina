'''
Создание базового класса "Фигура" и его наследование для создания классов
"Квадрат", "Прямоугольник" и "Круг". Класс "Фигура" будет иметь общие методы,
такие как вычисление площади и периметра, а классы-наследники будут иметь
специфичные методы и свойства.
'''
class Figure:
    def __init__(self, name):
        self.name = name

    # Площадь и периметр будут переопределяться в классах-наследниках
    def get_area(self):
        return 0 
    def get_perimeter(self):
        return 0  

    def show_info(self):
        print(self.name)
        print("Площадь: " + str(self.get_area()))
        print("Периметр: " + str(self.get_perimeter()))


class Square(Figure):
    def __init__(self, side):
        super().__init__(self, "Квадрат")
        self.side = side

    def get_area(self):
        return self.side * self.side

    def get_perimeter(self):
        return 4 * self.side

    def scale(self, chislo):
        self.side = self.side * chislo


class Rectangle(Figure):
    def __init__(self, width, height):
        super().__init__(self, "Прямоугольник")
        self.width = width 
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height


class Circle(Figure):
    def __init__(self, radius):
        Figure.__init__(self, "Круг")
        self.radius = radius
        self.pi = 3.14159

    def get_area(self):
        return self.pi * (self.radius * self.radius)

    def get_perimeter(self):
        return 2 * self.pi * self.radius

    def inflate(self, velichina):
        self.radius = self.radius + velichina

sq = Square(5)
rect = Rectangle(16, 9)
circ = Circle(3)

print("До изменений\n")
for fig in [sq, rect, circ]:
    fig.show_info()
    print()

print("\nСпецифичные методы:")

sq.scale(2)
print("Сторона квадрата после увеличения в 2 раза:", sq.side)

print("Проверка, является ли прямоугольник квадратом:", rect.is_square())

circ.inflate(2)
print("Радиус круга после увеличения на 2:", circ.radius)

print("\nПосле изменений\n")
for fig in [sq, circ]:
    fig.show_info()
    print()