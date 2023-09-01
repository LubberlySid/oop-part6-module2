class Shape:
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

    def display_color(self):
        return f"Color: {self.color}"


class Rectangle(Shape):
    def __init__(self, width, height, color):
        super().__init__(color, width, height)

    def display_color(self):
        super().display_color()
        return f"Color: {self.color}", f"Width: {self.width}", f"Height: {self.height}"


rectangle = Rectangle(4, 6, "Green")
print(rectangle.display_color())
