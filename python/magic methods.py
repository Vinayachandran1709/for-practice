class Book:
  
  def __init__(self, title, author, num_pages):
    self.title = title
    self.author = author
    self.num_pages = num_pages

  def __str__(self):
    return f"{self.title} by {self.author} contains {self.num_pages} pages"
  
  def __eq__(self, other): #other is to save the other book for comparison
    return self.title == other.title and self.author == other.author

  def __lt__(self, other):
    return self.num_pages < other.num_pages

  def __add__(self, other):
    return self.num_pages + other.num_pages

  def __contains__(self, keyword):
    return keyword in self.title or keyword in self.author

book1 = Book("Kampus","Vinay", 1080)
book2 = Book("Kampus","Vinay", 420)
book3 = Book("Melbourne","Karlsen", 980)

print(book1)
print(book2)
print(book3)
print(book1 == book2)
print(book2 > book3)
print(book2 + book3)
print("Kampus" in book2)