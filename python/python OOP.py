from car import Car
#this is how we import a python file into new one the file name is car.py the class is Car
car1 = Car("Nexon", 2023, "brown", False)
car2 = Car("Innova", 2015, "white", True)
#False word must be capitalised
print(car1.model)
#the dot between car1 and model is called Attribute access operator 
print(car1.year)
print(car1.color)
print(car1.for_sale)
car1.drive()
car1.stop()

print()
print(car2.model)
print(car2.year)
print(car2.color)
print(car2.for_sale)
car2.drive()
car2.stop()