import math

class Figure:
    sides_count = 0
    __sides = []
    __color = [0,0,0]
    filled = False

    def __init__(self,color):
        self.set_color(color[0],color[1],color[2])

    # Color methods
    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_color(self, r, g, b):
        valid_color_r = False
        valid_color_g = False
        valid_color_b = False
        if isinstance(r, int) and r in range(0, 256):
            valid_color_r = True
        if isinstance(g, int) and g in range(0, 256):
            valid_color_g = True
        if isinstance(b, int) and b in range(0, 256):
            valid_color_b = True
        if valid_color_r and valid_color_g and valid_color_b:
            return True
        return False

    # Sides methods
    def __is_valid_sides(self, args):
        is_valid = True
        for i in args:
            if not isinstance(i, int) or i < 0:
                is_valid = False
                return is_valid
        return is_valid

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(new_sides):
            if len(new_sides) == self.sides_count:
                self.__sides = list(new_sides)


    def __len__(self):
        if isinstance(self, Circle):
            return self.get_sides()[0]
        if isinstance(self, Cube):
            return self.get_sides()[0]*12
        if isinstance(self, Triangle):
            res = 0
            for i in self.get_sides():
                res += i
            return res
#Circle
class Circle(Figure):
    __radius = 0

    def __init__(self, color,*args):
        self.sides_count = 1
        super().__init__(color)

        side = []
        if len(args) > 1:
            side.append(1)
        else:
            side.append(args[0])
        self.set_sides(*side)

        l = int(self.get_sides()[0])
        self.__radius = round(l / (2 * math.pi), 2)

    def get_square(self):
        return round(math.pi * math.pow(self.__radius,2),2)

#Cube
class Cube(Figure):

    def __init__(self, color,*args):
        self.sides_count = 12
        super().__init__(color)

        side = []
        len_args = len(args)
        if len_args == 1:
            for i in range(0,12):
                side.append(args[0])
        else:
            for i in range(0,12):
                side.append(1)
        self.set_sides(*side)

    def get_volume(self):
        return int(math.pow(self.get_sides()[0], 3))

#Triangle
class Triangle(Figure):

    def __init__(self, color, *args):
        self.sides_count = 3
        super().__init__(color)

        side = []
        len_args = len(args)
        if len_args == 1:
            for i in range(0, 3):
                side.append(args[0])
        if len_args == self.sides_count:
            for i in range(0, 3):
                side.append(args[i])
        if len_args == 2 or len_args > 3 :
            for i in range(0, 3):
                side.append(1)
        self.set_sides(*side)

    def get_square(self):
        sides = self.get_sides()
        p = 0
        for i in sides:
            p += i
        p = p/2
        return round(math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2])),2)


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
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
print()

#Своя проверка
triang = Triangle((100,44,55), 5,6)

print(triang.get_sides())
print(triang.get_square())


