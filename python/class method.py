class Student:

  count = 0

  def __init__(self, name, gpa):
    self.name = name
    self.gpa = gpa
    Student.count += 1

  def get_info(self):
    return f"{self.name} = {self.gpa}"
  
  @classmethod
  def get_count(cls): #cls means class
    return f"Total no of students: {cls.count}"

student = [Student("A", 10),
Student("B", 9),
Student("C", 8),
Student("D", 7),
Student("E", 6),
Student("F", 5),
Student("G", 4),
Student("H", 3),
Student("I", 2),
Student("J", 1)]

print(Student.get_count())
for s in student:
    print(s.get_info())
