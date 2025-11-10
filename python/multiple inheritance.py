class Animal:
    def eat(self):
        print("The animal can eat")

    def sleep(self):
        print("The animal can sleep")

class Prey(Animal):
    def flee(self):
      print("This animal is escaping")

class Predator(Animal):
    def hunt(self):
        print("This animal is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator): #this is multiple inheritance
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()
prey = Prey()

fish.hunt()
fish.flee()
fish.eat()
hawk.sleep()