class Student:
    grad_year = 2024
    num_students = 0
    #this is class var created outside constructor
    def __init__(self, name, age):
        self.name = name #these are instance variables
        self.age = age
        Student.num_students += 1
        
student1 = Student("Vinay", 22)
student2 = Student("Akshay", 12)
student3 = Student("Bhaiya", 19)
student4 = Student("Mukesh", 35)

print(f"My graduating class had {Student.num_students} students")
print()
print(student1.name)
print(student2.age)
print(student1.grad_year)
print(Student.grad_year)
#it is good to access class var through the name of the class in this case Student is the class you will get answer even though you use student1
print()
print(student2.name)
print(student2.age)
print()
print(student3.name)
print(student3.age)