from abc import ABC, abstractmethod

class Shape:
  @abstractmethod
  
  #Shape is an abstract base class (ABC) — it cannot be instantiated directly.
  #@abstractmethod means that any class inheriting from Shape must define the method area().
  #So, this ensures that every subclass of Shape (like Circle, Square, Triangle) has an area() method.
  def area(self):
   pass

class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius

  def area(self):
    return 3.14 * self.radius ** 2

class Square(Shape):
  def __init__(self, side):
    self.side = side

  def area(self):
    return self.side ** 2

class Triangle(Shape):
  def __init__(self, base, height):
    self.base = base
    self.height = height

  def area(self):
    return self.base * self.height * 0.5

#circle = Circle() our circle is also Circle and a Shape but not square or triangle same applies for others
shapes = [Circle(4), Square(5), Triangle(6,7)]

for shape in shapes:
  print(shape.area())