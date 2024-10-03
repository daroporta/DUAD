from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def calculate_perimeter(self):
        pass

    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius, diameter):
        self.radius= radius
        self.diameter= diameter

    def calculate_perimeter(self):
        perimeter=3.1416*self.diameter
        print(f"The perimeter of the circle is: {perimeter:.2f}")

    def calculate_area(self):
        area=3.1416 * (self.radius)**2
        print(f"The area of the circle is: {area:.2f}")


class Square(Shape):
    def __init__(self, side):
        self.side=side

    def calculate_perimeter(self):
        perimeter= self.side+self.side+self.side+self.side
        print(f"The perimeter of the square is: {perimeter:.2f}")

    def calculate_area(self):
        area=self.side*self.side
        print(f"The area of the square is: {area:.2f}")


class rectangle(Shape):
    def __init__(self, length, width):
        self.length= length
        self.width= width

    def calculate_perimeter(self):
        perimeter= (self.length*2) + (self.width*2)
        print(f"The perimeter of the rectangle is: {perimeter:.2f}")

    def calculate_area(self):
        area=self.length*self.width
        print(f"The area of the rectangle is: {area:.2f}")


circle=Circle(5.5, 10)

circle.calculate_area()
circle.calculate_perimeter()
print(10*"--")
square= Square(10.1)

square.calculate_area()
square.calculate_perimeter()
print(10*"--")
rectangle=rectangle(5.5, 4)

rectangle.calculate_perimeter()
rectangle.calculate_area()
