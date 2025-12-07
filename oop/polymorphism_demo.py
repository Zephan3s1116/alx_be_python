
import math

class Shape:
    """Base class for all shapes, defining the area() interface."""
    def area(self):
        """
        Calculates the area of the shape. Must be overridden by subclasses.
        """
        raise NotImplementedError("Subclasses must override the area() method.")

class Rectangle(Shape):
    """Derived class for a rectangle, inheriting from Shape."""
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Overrides the base method to calculate the rectangle's area."""
        return self.length * self.width

class Circle(Shape):
    """Derived class for a circle, inheriting from Shape."""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Overrides the base method to calculate the circle's area (π * r²)."""
        
        return math.pi * (self.radius ** 2)

