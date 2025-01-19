import math


class Figure:
    def __init__(self, color, *sides):
        self._sides = list(sides)
        self._color = list(color)
        self.filled = True

    def sides_count(self):
        return 0

    def _is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 for x in (r, g, b)) and all(isinstance(x, int) for x in (r, g, b))

    def set_color(self, r, g, b):
        if self._is_valid_color(r, g, b):
            self._color = [r, g, b]

    def get_color(self):
        return self._color

    def _is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def set_sides(self, *new_sides):
        if self._is_valid_sides(*new_sides):
            self._sides = list(new_sides)

    def get_sides(self):
        return self._sides

    def __len__(self):
        return sum(self._sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, circumference):
        super().__init__(color, circumference)
        self._radius = circumference / (2 * math.pi)

    def get_square(self):
        return math.pi * (self._radius ** 2)

    def set_sides(self, circumference):
        if self._is_valid_sides(circumference):
            self._sides[0] = circumference
            self._radius = circumference / (2 * math.pi)


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, a, b, c):
        super().__init__(color, a, b, c)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, edge_length):
        super().__init__(color, *([edge_length] * self.sides_count))
        self._edge_length = edge_length

    def get_volume(self):
        return self._edge_length ** 3


# Код для проверки
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # [55, 66, 77]
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # 15

# Проверка объёма (куба):
print(cube1.get_volume())