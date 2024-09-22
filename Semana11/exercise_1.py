class Circle:
    radius=float(input("Please enter the radius of your circle: "))


    def get_area(self):
        area=3.14159 * (self.radius)**2
        print(f"The area of your circle is: {area} cm2")


my_circle= Circle()

my_circle.radius

my_circle.get_area()

