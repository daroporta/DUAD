class Circle:
    while True:
        try:
            radius=float(input("Please enter the radius of your circle: "))
            break
        except ValueError:
            print("Please type a number.")


    def get_area(self):
        area=3.14159 * (self.radius)**2
        print(f"The area of your circle is: {area} cm2")


my_circle= Circle()

my_circle.radius

my_circle.get_area()

