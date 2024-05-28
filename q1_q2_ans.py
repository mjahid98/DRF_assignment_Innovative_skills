# oop using Inheritance and polymorphism

import math

# This is the base class that I created. 
# Because all of them are different shapes so I named the class as Shape
class Shape:
    def get_dimentions():
        pass
    def calculate_area():
        pass

# Here Circle(Shape) means Circle class inherits the Shape class. 
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

# As we know polymorphism means from a root class we redefine some and that override the root function.
# Basically, we change the function from the base class. 
# I am doing the same with the all of the other Shape classes. 
    def calculate_area(self):
        area = math.pi * self.radius ** 2
        return area
    
    def get_dimensions():
        radius = float(input("Enter the radius of the circle: "))
        return Circle(radius)
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        area = self.length * self.width
        return area
    
    def get_dimensions():
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        return Rectangle(length, width)

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        area = 0.5 * self.base * self.height
        return area
    
    def get_dimensions():
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        return Triangle(base, height)

    


# def calculate_circle_area(radius):
#     return math.pi * radius ** 2

# def calculate_rectangle_area(length, width): 
#     return length * width
# def calculate_triangle_area(base, height): 
#     return 0.5* base * height

def main():
    choice = input("Enter shape (circle, rectangle, triangle): ")
    
    if choice == "circle":
        shape = Circle
    elif choice == "rectangle":
        shape = Rectangle
    elif choice == "triangle":
        shape = Triangle
    else:
        print("Invalid shape choice!")

    shape_dimentions = shape.get_dimensions()
    area = shape_dimentions.calculate_area()
    print(f"Area of the {choice}:", area)
        
if __name__ == '__main__':
    main()