import math

class Figure:
    sides_count = 0

    def __init__(self, color: list, *sides):
       self.__color = [color[0],color[1],color[2]] if self.__is_valid_color(*color) else [0,0,0]
       self.__sides = sides if len(sides) == self.sides_count else [1] * self.sides_count
       self.filled = False

    def __len__(self):
        if isinstance(self, Circle):
            return self.get_sides()[0]
        if isinstance(self, Cube):
            return self.get_sides()[0] * 12
        if isinstance(self, Triangle):
            res = 0
            for i in self.get_sides():
                res += i
            return res

#Color methods
    def get_color(self):
        return self.__color

    def set_color(self, r,g,b):
        if self.__is_valid_color(r,g,b):
            self.__color = [r,g,b]

    def __is_valid_color(self, r,g,b):
        return all(isinstance(i,int) and 0<=i<=255 for i in (r,g,b))

#Sides_method
    def get_sides(self):
        return list(self.__sides)

    def set_sides(self,*new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides

    def __is_valid_sides(self, *sides):
        return all(isinstance(i,int) and i>0 for i in sides) and len(sides) == self.sides_count



class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color,*sides)
        self.__radius = round(self.get_sides()[0] / (2 * math.pi), 2)

    def get_square(self):
        return round(math.pi * math.pow(self.__radius,2),2)

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color,*sides)
        self.set_sides(*list(sides)*12)

    def get_volume(self):
        return int(math.pow(self.get_sides()[0], 3))

class Triangle(Figure):
    sides_count = 3
    
    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        sides = self.get_sides()
        p = 0
        for i in sides:
            p += i
        p = p/2
        return round(math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])),2)

circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

#Своя проверка
triang = Triangle((100,44,55), 5,6)

print(triang.get_sides())
print(triang.get_square())
