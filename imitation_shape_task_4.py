class Shape:
    def __init__(self, color):
        self.color = color

    def display_color(self):
        return self.color


class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color)
        self.width = width
        self.height = height

    def width(self):
        return self.width

    def height(self):
        return self.height


shape = Shape("Blue")
print(shape.display_color())
rectangle = Rectangle(4, 6, "Green")
print(rectangle.width)
print(rectangle.height)
print(rectangle.display_color())
