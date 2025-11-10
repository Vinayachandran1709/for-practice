class Employee:
  
  def __init__(self, name, position):
    self.name = name
    self.position = position

  def get_info(self):
    return(f"{self.name} = {self.position}")
    
  @staticmethod #to create a static method we need to create like this
  def is_valid_position(position): #this is static method it belongs to the class not to the object created inside the class
    valid_position = ["Manager", "Cashier","Engineer","Tester"]
    return position in valid_position

employee1 = Employee("Vinay", "Developer")
employee2 = Employee("Akash", "Cook")
employee3 = Employee("Kumar", "Waiter")
  
print(Employee.is_valid_position("Manager"))
print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())