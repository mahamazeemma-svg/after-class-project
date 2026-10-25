class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

r = float(input("Enter the radius of the circle: "))
c = circle(r)
print("Area of the circle:", c.area())
print("Perimeter of the circle:", c.perimeter())