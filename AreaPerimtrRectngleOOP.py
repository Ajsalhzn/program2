class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
r1 = Rectangle(10, 5)

print("Area of Rectangle: ", r1.area())
print("Perimeter of Rectangle:", r1.perimeter())