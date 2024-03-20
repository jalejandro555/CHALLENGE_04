import math

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def compute_distance(self, other):
        return math.sqrt((self._x - other._x)**2 + (self._y - other._y)**2)

    def get_x(self):
        return self._x

    def set_x(self, value):
        self._x = value

    def get_y(self):
        return self._y

    def set_y(self, value):
        self._y = value


class Line:
    def __init__(self, start_point: Point, end_point:Point):
        self._start_point = start_point
        self._end_point = end_point
        self._length = start_point.compute_distance(end_point)

    def get_length(self):
        return self._length

    def get_start_point(self):
        return self._start_point

    def set_start_point(self, value):
        self._start_point = value
        self._length = self._start_point.compute_distance(self._end_point)

    def get_end_point(self):
        return self._end_point

    def set_end_point(self, value):
        self._end_point = value
        self._length = self._start_point.compute_distance(self._end_point)


class Shape:
    def __init__(self, vertices):
        self._vertices = vertices
        self._edges = [Line(vertices[i], vertices[(i+1)%len(vertices)]) for i in range(len(vertices))]
        self._inner_angles = self.compute_inner_angles()
        self._is_regular = self.check_regular()

    def compute_area(self):
        raise NotImplementedError

    def compute_perimeter(self):
        return sum(edge.get_length() for edge in self._edges)

    def compute_inner_angles(self):
        raise NotImplementedError

    def check_regular(self):
        return all(edge.get_length() == self._edges[0].get_length() for edge in self._edges)

    def get_vertices(self):
        return self._vertices

    def set_vertices(self, value):
        self._vertices = value
        self._edges = [Line(self._vertices[i], self._vertices[(i+1)%len(self._vertices)]) for i in range(len(self._vertices))]
        self._inner_angles = self.compute_inner_angles()
        self._is_regular = self.check_regular()

    def get_edges(self):
        return self._edges

    def get_inner_angles(self):
        return self._inner_angles

    def is_regular(self):
        return self._is_regular


class Triangle(Shape):
    def __init__(self, vertices):
        super().__init__(vertices)

    def compute_area(self):
        # Using Heron's formula
        a, b, c = self._edges[0].get_length(), self._edges[1].get_length(), self._edges[2].get_length()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    def compute_inner_angles(self):
        # Using the law of cosines
        a, b, c = self._edges[0].get_length(), self._edges[1].get_length(), self._edges[2].get_length()
        return [math.degrees(math.acos((b**2 + c**2 - a**2) / (2 * b * c))),
                math.degrees(math.acos((a**2 + c**2 - b**2) / (2 * a * c))),
                math.degrees(math.acos((a**2 + b**2 - c**2) / (2 * a * b)))]


class Isosceles(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)


class Equilateral(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)


class Scalene(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)


class TriRectangle(Triangle):
    def __init__(self, vertices):
        super().__init__(vertices)


class Rectangle(Shape):
    def __init__(self, vertices):
        super().__init__(vertices)

    def compute_area(self):
        return self._edges[0].get_length() * self._edges[1].get_length()

    def compute_inner_angles(self):
        return [90] * 4


class Square(Rectangle):
    def __init__(self, vertices):
        super().__init__(vertices)

# Crear los puntos
p1 = Point(0, 0)
p2 = Point(2, 5)
p3 = Point(4, 0)

# Crear el triángulo isósceles
isosceles = Isosceles([p1, p2, p3])

# Imprimir el área, el perímetro y los ángulos internos
print("ISOSCELES TRIANGLE")
print("Area:", isosceles.compute_area())
print("Perimeter:", isosceles.compute_perimeter())
print("Inner angles:", isosceles.compute_inner_angles())
print("\n")

# Crear los puntos
r1 = Point(0, 0)
r2 = Point(1, 0)
r3 = Point(0.5, 0.8660254037844386)  # This creates an equilateral triangle with side length 1

# Crear el triángulo equilátero
equilateral = Equilateral([r1, r2, r3])

# Imprimir el área, el perímetro y los ángulos internos
print("EQUILATERAL TRIANGLE")
print("Area:", equilateral.compute_area())
print("Perimeter:", equilateral.compute_perimeter())
print("Inner angles:", equilateral.compute_inner_angles())
print("\n")

# Crear los puntos
m1 = Point(2, 0)
m2 = Point(3, 5)
m3 = Point(6, 0)

# Crear el triángulo escaleno
scalene = Scalene([m1, m2, m3])

# Imprimir el área, el perímetro y los ángulos internos
print("SCALENE TRIANGLE")
print("Area:", scalene.compute_area())
print("Perimeter:", scalene.compute_perimeter())
print("Inner angles:", scalene.compute_inner_angles())
print("\n")

# Crear los puntos
f1 = Point(0, 0)
f2 = Point(6, 4)
f3 = Point(6, 0)

# Crear el triángulo rectángulo
tri_rectangle = TriRectangle([f1, f2, f3])

# Imprimir el área, el perímetro y los ángulos internos
print("RECTANGLE TRIANGLE")
print("Area:", tri_rectangle.compute_area())
print("Perimeter:", tri_rectangle.compute_perimeter())
print("Inner angles:", tri_rectangle.compute_inner_angles())
print("\n")

# Crear los puntos
b1 = Point(0, 0)
b2 = Point(6, 2)
b3 = Point(6, 0)
b4 = Point(0, 2)

# Crear el rectángulo
rectangle = Rectangle([b1, b2, b3, b4])

# Imprimir el área, el perímetro y los ángulos internos
print("RECTANGLE")
print("Area:", rectangle.compute_area())
print("Perimeter:", rectangle.compute_perimeter())
print("Inner angles:", rectangle.compute_inner_angles())
print("\n")

# Crear los puntos
g1 = Point(0, 0)
g2 = Point(0, 4)
g3 = Point(4, 4)
g4 = Point(4, 0)

# Crear el cuadrado
square = Square([g1, g2, g3, g4])

# Imprimir el área, el perímetro y los ángulos internos
print("SQUARE")
print("Area:", square.compute_area())
print("Perimeter:", square.compute_perimeter())
print("Inner angles:", square.compute_inner_angles())