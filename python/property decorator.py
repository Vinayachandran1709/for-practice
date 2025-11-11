class Rectangle:
  def __init__(self, width, height):
    self._width = width #the _ before means width and height tells the dev that they need to be protected, are internal and can't be accessed directly
    self._height = height

  @property
  def width(self):
    return f"{self._width:.1f}cm"

  @property
  def height(self):
    return f"{self._height:.1f}cm"
  
  @width.setter #setter method
  def width(self,new_width):
    if new_width > 0:
      self._width = new_width
    else:
      print("Width greater than zero")

  @height.setter #setter method
  def height(self,new_height):
    if new_height > 0:
      self._height = new_height
    else:
      print("height greater than zero")


rectangle = Rectangle(3,4)
rectangle.width = 5
rectangle.height = 8


print(rectangle.width)
print(rectangle.height) #this is getter method to get the obj we are also setting business logic like internal use 


     