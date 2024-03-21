# CHALLENGE_04
## Class exercise 
1. Create a superclass called Shape(), which is the base of the classes Reactangle() and Square(), define the methods compute_area and compute_perimeter in Shape() and then using polymorphism redefine the methods properly in Rectangle and in Square.
```python
class Shape:
    def __init__(self):
        pass

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def compute_area(self):
        return self.width * self.height

    def compute_perimeter(self):
        return 2 * (self.width + self.height)


class Square(Shape):
    def __init__(self, lenght):
        self.lenght = lenght

    def compute_area(self):
        return self.lenght ** 2

    def compute_perimeter(self):
        return 4 * self.lenght
```
In this code i define two classes, Rectangle and Square, both of which are subclasses of a superclass Shape. 

The Rectangle class also has two methods: compute_area and compute_perimeter. The compute_area method returns the area of the rectangle (width * height), and the compute_perimeter method returns the perimeter of the rectangle (2 * (width + height))

The Square class is similar to the Rectangle class, but it only has one instance variable: length. This is because all sides of a square have the same length. The compute_area method returns the area of the square (length ** 2), and the compute_perimeter method returns the perimeter of the square (4 * length).

2. Using the classes Point() and Line() define a new super-class Shape() with the following structure:
```mermaid
classDiagram
    class Shape {
        + vertices: list(Point)
        + edges: list(Line)
        + inner_angles: list(float)
        + is_regular: bool
        + compute_area(self)
        + compute_perimeter(self)
        + compute_inner_angles(self)
    }

    class Point {
        + x: int
        + y: int
        + compute_distance(self, Point)
    }

    class Line {
        + start_point: Point
        + end_point: Point
        + length: float
    }

    class Triangle {
    }

    class Isosceles{
    }

    class Equilateral{
    }

    class Scalene{
    }

    class TriRectangle{
    }

    class Rectangle{
    }

    class Square{
    }

    Shape *-- Line 
    Shape *-- Point
    Triangle <|-- Shape
    Isosceles <|-- Triangle
    Equilateral <|-- Triangle
    Scalene <|-- Triangle
    TriRectangle <|-- Triangle
    Rectangle <|-- Shape
    Square <|-- Rectangle
```
### Definition of the classes Point() and Line()
```python
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
```
The Point class represents a point in a 2D space. It has two instance variables: _x and _y, which represent the x and y coordinates of the point.

This class also has a method compute_distance that calculates the distance between this point and another point. It does this using the formula sqrt((x2 - x1)^2 + (y2 - y1)^2), where (x1, y1) are the coordinates of this point and (x2, y2) are the coordinates of the other point.

The Point class also has getter and setter methods for the _x and _y instance variables. These methods allow the instance variables to be read and modified from outside the class.

In another hand, thw Line class represents a line in a 2D space. It has three instance variables: _start_point, _end_point, and _length. The _start_point and _end_point variables are objects of the Point class and represent the start and end points of the line. The _length variable is the length of the line, which is calculated as the distance between the start point and the end point.
The Line class also has getter and setter methods for the _start_point, _end_point, and _length instance variables. The setter methods for _start_point and _end_point also update the _length variable to reflect the new length of the line.
### class Shape:
```python
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
```
The Shape class is designed to represent a generic geometric shape. It doesn't directly inherit from Point or Line, but it uses instances of these classes to define its properties.
The constructor method __init__ gets called when a new instance of Shape is created. It takes a list of Point instances (vertices) as an argument. It then creates a list of Line instances (_edges) representing the edges of the shape, where each edge is a line between two consecutive vertices, ****(This is composition at its best, Shape is composed of instances of other classes (Point and Line).**** It also computes the inner angles of the shape and checks if the shape is regular (all edges have the same length).

compute_area: This method is intended to compute the area of the shape. It raises a NotImplementedError, meaning it should be implemented in a subclass.

compute_perimeter: This method computes the perimeter of the shape by summing the lengths of all edges.

compute_inner_angles: This method is intended to compute the inner angles of the shape. Like compute_area, it raises a NotImplementedError and should be implemented in a subclass.

check_regular: This method checks if the shape is regular (all edges have the same length).

get_vertices, set_vertices, get_edges, get_inner_angles, is_regular: These are getter and setter methods for the vertices, edges, inner angles, and regularity of the shape.(**encasulation**)
```python
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

# Create the points
p1 = Point(0, 0)
p2 = Point(2, 5)
p3 = Point(4, 0)

# Create the isosceles triangle
isosceles = Isosceles([p1, p2, p3])

# Print the Area, Perimeter and Inner angles of the Isosceles triangle
print("ISOSCELES TRIANGLE")
print("Area:", isosceles.compute_area())
print("Perimeter:", isosceles.compute_perimeter())
print("Inner angles:", isosceles.compute_inner_angles())
print("\n")

#EQUILATERAL TRIANGLE
r1 = Point(0, 0)
r2 = Point(1, 0)
r3 = Point(0.5, 0.8660254037844386)  # This creates an equilateral triangle with side length 1

equilateral = Equilateral([r1, r2, r3])

print("EQUILATERAL TRIANGLE")
print("Area:", equilateral.compute_area())
print("Perimeter:", equilateral.compute_perimeter())
print("Inner angles:", equilateral.compute_inner_angles())
print("\n")

#SCALENE TRIANGLE
m1 = Point(2, 0)
m2 = Point(3, 5)
m3 = Point(6, 0)

scalene = Scalene([m1, m2, m3])

print("SCALENE TRIANGLE")
print("Area:", scalene.compute_area())
print("Perimeter:", scalene.compute_perimeter())
print("Inner angles:", scalene.compute_inner_angles())
print("\n")

#RECTANGLE TRIANGLE
f1 = Point(0, 0)
f2 = Point(6, 4)
f3 = Point(6, 0)

tri_rectangle = TriRectangle([f1, f2, f3])

print("RECTANGLE TRIANGLE")
print("Area:", tri_rectangle.compute_area())
print("Perimeter:", tri_rectangle.compute_perimeter())
print("Inner angles:", tri_rectangle.compute_inner_angles())
print("\n")

#Rectangle
b1 = Point(0, 0)
b2 = Point(6, 2)
b3 = Point(6, 0)
b4 = Point(0, 2)

rectangle = Rectangle([b1, b2, b3, b4])

print("RECTANGLE")
print("Area:", rectangle.compute_area())
print("Perimeter:", rectangle.compute_perimeter())
print("Inner angles:", rectangle.compute_inner_angles())
print("\n")

# Square
g1 = Point(0, 0)
g2 = Point(0, 4)
g3 = Point(4, 4)
g4 = Point(4, 0)

square = Square([g1, g2, g3, g4])

print("SQUARE")
print("Area:", square.compute_area())
print("Perimeter:", square.compute_perimeter())
print("Inner angles:", square.compute_inner_angles())
```
In thus part of the code i defined several classes that represent different types of geometric shapes, specifically different types of triangles and quadrilaterals. These classes ****inherit**** from the Shape, Triangle, and Rectangle classes defined earlier.

Triangle: This class ****inherits**** from Shape and overrides the compute_area and compute_inner_angles methods to provide implementations specific to triangles. The area is computed using Heron's formula, and the inner angles are computed using the law of cosines.

Isosceles, Equilateral, Scalene, TriRectangle: These classes inherit from Triangle. They exist to represent specific types of triangles, and could be extended in the future to provide behavior specific to these types of triangles.

Rectangle: This class inherits from Shape and overrides the compute_area and compute_inner_angles methods to provide implementations specific to rectangles. The area is computed as the product of the lengths of two adjacent edges, and the inner angles are all 90 degrees.

Square: This class inherits from Rectangle but doesn't provide any new methods. It exists to represent squares.

Ater that I create instances of these classes to represent specific shapes. For each shape, it creates Point instances to represent the vertices of the shape, then creates an instance of the appropriate class (e.g., Isosceles, Equilateral, Scalene, TriRectangle, Rectangle, Square) using these vertices. It then prints the area, perimeter, and inner angles of each shape.

### The restaurant revisted
Add setters and getters to all subclasses for menu item
```python
class MenuItem:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def get_price(self):
        return self._price

    def set_price(self, value):
        self._price = value

    def calculate_total_price(self, quantity):
        return self.get_price() * quantity

class FoodItem(MenuItem):
    def __init__(self, name, price, category):
        super().__init__(name, price)
        self._category = category

    def get_category(self):
        return self._category

    def set_category(self, value):
        self._category = value

class Starters(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price, "Starters")

class Soupes(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price, "Soupes")

class MainCourse(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price, "Main Course")

class Drinks(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price, "Drinks")

class Dessert(FoodItem):
    def __init__(self, name, price):
        super().__init__(name, price, "Dessert")
```
In the MenuItem class, I added get_name, set_name, get_price, and set_price methods. These methods allow you to get and set the name and price attributes of a MenuItem object. The set_name and set_price methods can be used to change the name and price of a MenuItem after it has been created.

2. Here is the full code with the rest of the improvements
```python
class Payment:
    def __init__(self):
        pass

    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement pay()")

class Card(Payment):
    def __init__(self, number, cvv):
        super().__init__()
        self.number = number
        self.cvv = cvv

    def pay(self, amount):
        print(f"Paying {amount} with card {self.number[-4:]}")

class Cash(Payment):
    def __init__(self, amount_given):
        super().__init__()
        self.amount_given = amount_given

    def pay(self, amount):
        if self.amount_given >= amount:
            print(f"Payment made in cash. Change: {self.amount_given - amount}")
        else:
            print(f"Insufficient funds. Missing {amount - self.amount_given} to complete the payment.")

def user_payment(total_after_discount):
    while True:
        print("Please select a payment method:")
        print("1. Card")
        print("2. Cash")
        choice = input("Enter your choice (1 or 2): ")
        if choice == '1':
            card_number = input("Enter your card number: ")
            cvv = input("Enter your CVV: ")
            return Card(card_number, cvv)
        elif choice == '2':
            amount_given = float(input("Enter the amount you are giving: "))
            if amount_given < total_after_discount:
                print(f"Not enough money given. You still owe: ${total_after_discount - amount_given:.2f}")
            else:
                change = amount_given - total_after_discount
                print(f"Payment made in cash. Change: ${change:.2f}")
                return Cash(amount_given)
        else:
            print("Invalid choice. Please enter 1 or 2.")


# Define the Order class
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append((item, quantity))

    def calculate_total_price(self):
        total = 0
        for item, quantity in self.items:
            total += item.get_price() * quantity
        return total
    
    def ask_for_discount(self):
        categories = ["programmer", "mentally_ill", "student", "senior_citizen", "veteran", "unemployed", "homeless", "refugee", "disabled"]
        print("Please enter your population category. if you are not in any of these categories, please press enter")
        print("Available categories are:")
        for category in categories:
            print(category)
        user_category = input()
        if user_category in categories:
            return 10
        else:
            print("Sorry, you are not eligible for a discount.")
            return 0


    def apply_discount(self):
        discount = self.ask_for_discount()
        total_bill = self.calculate_total_price()
        return total_bill - (total_bill * discount / 100)

# Create instances of menu items
menu_items = [
    Starters("Diazepam, ONLY_FOR_SALE_WITH_PRESCRIPTION", 1.99,),
    Starters("Xanax, ONLY_FOR_SALE_WITH_PRESCRIPTION", 0.99),
    Starters("Propanonol, ONLY_FOR_SALE_WITH_PRESCRIPTION", 0.99), 
    Soupes("Programmer's tears with Mexican tortilla", 5.99),
    Soupes("Spinach with tomato", 3.99),
    Soupes("Lentil with bacon", 4.99),
    MainCourse("Korean boy beef burger", 201.99),
    MainCourse("Chicken fetus crepe", 122.99),
    MainCourse("Vegan salad with tuna", 7.99),
    MainCourse("Turkey pizza", 100),
    MainCourse("Venezuelan Pasta", 0.99),
    MainCourse("Fish and Chips with cornflakes", 12.99),
    Drinks("Fanta", 1.99),
    Drinks("Taylor Swift's sweat", 900.99),
    Drinks("Coca Cola", 1.99),
    Drinks("Pepsi", 1.99),
    Drinks("Water from arctic glaciers", 300.99),
    Dessert("Ice cream with an american sausage", 2.99),
    Dessert("Fruit salad without fruit or transgenic fruit", 2.99),
    Dessert("Fruit salad with organic fruit", 200.99),
    Dessert("Snow white apple, REQUIRES_SIGNED_CONSENT", 6.99),
]
# User interaction functions
def show_menu():
    print("Menu:")
    for index, item in enumerate(menu_items):
        print(f"{index + 1}. {item.get_name()} - ${item.get_price()} - Category: {item.get_category()}")
def user_order():
    show_menu()
    order = Order()
    while True:
        choice = input("Enter the menu item number (or 'done' to finish): ")
        if choice.lower() == 'done':
            break
        quantity = int(input("Enter the quantity: "))
        order.add_item(menu_items[int(choice) - 1], quantity)
    return order

# Main program
if __name__ == "__main__":
    print("WELCOME TO THE PYTHON PSYCHIATRIC RESTAURANT!")
    customer_order = user_order()
    print(f"Your total bill is: ${customer_order.calculate_total_price():.2f}")
    total_after_discount = customer_order.apply_discount()
    print(f"Your total bill after discount is: ${total_after_discount:.2f}")
    payment_method = user_payment(total_after_discount)
   
    print("Thank you for dining with us!")

    
```
