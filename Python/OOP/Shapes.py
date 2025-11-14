class Shape:
    def __init__(self, color, brdColor):
        self.color = color
        self.brdColor = brdColor

    def printDetail(self):
        print(
            f"This Shape has Color as {self.color} & Border color as {self.brdColor}")


class Rectangle(Shape):
    def __init__(self, Length, Breath, color, brdColor):
        self.Length = Length
        self.Breath = Breath
        Shape.__init__(self, color, brdColor)

    def area(self):
        print(f"Area of this rectangle is", self.Length*self.Breath)


class Circle(Shape):
    def __init__(self, Radius, color, brdColor):
        self.Radius = Radius
        Shape.__init__(self, color, brdColor)

# rhombus = Shape("White", "Black")

# rhombus.printDetail()


rec1 = Rectangle(5, 8, "Red", "White")

rec1.printDetail()
rec1.area()

sh1 = Shape("B", "G")

cir1 = Circle(5, "Dark Blue", "Red")
cir1.printDetail()
