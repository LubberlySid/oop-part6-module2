class Shape:
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

    def display_color(self):
        return f"Color: {self.color}"


class Rectangle(Shape):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)

    def display_color(self):
        super().display_color()
        return f"Color: {self.color}", f"Width: {self.width}", f"Height: {self.height}"


class Square(Rectangle):
    def __init__(self, color, side_length):
        super().__init__(color, side_length, side_length)
        self.side_length = side_length

    def display_color(self):
        super().display_color()
        return f"Color: {self.color}"


square = Square("Green", 8)
print(square.display_color())
print(square.width)
print(square.height)
print(square.side_length)
