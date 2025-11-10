class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive = True

    def live(self):
        print(f"{self.name} is living in the earth")
    def eat(self):
        print(f"{self.name} is eating non-veg")
    def sleep(self):
        print(f"{self.name} is sleeping peacefully")

class Dog(Animal):
    def sound(self):
        print("WOOH")

class Cat(Animal):
    pass

class Lion(Animal):
    pass

dog = Dog("Aneesh")
cat = Cat("Kavitha")
lion = Lion("Vinay")

print(dog.name)
print(dog.is_alive)
dog.eat()
dog.live()
dog.sleep()
dog.sound()