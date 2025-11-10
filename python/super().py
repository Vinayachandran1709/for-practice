class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"It's color is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self, color, is_filled, radius): #if we have tp change filled like is_filled we have to change in many places we can reduce that by using super()
        super().__init__(color, is_filled= False)# we have made the condition false here only if not made it will show it is filled on if cond
        self.radius = radius

    def  describe(self):
        print(f"")
class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

circle = Circle("Red", True, 100)
circle.describe()