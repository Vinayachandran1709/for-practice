class Animal:
  alive = True

class Dog(Animal):
  def speak(self):
    print("WOOH")

class Cat(Animal):
  def speak(self):
    print("MEOW")

class Car:
  def speak(self): #Car class has speak function but not alive attribute
    print("Racing sound")

animals = [Dog(), Cat(), Car()]

for animal in animals:
  animal.speak()
  print(animal.alive)