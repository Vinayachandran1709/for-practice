#word = "APPLE"
#letter = input("Give a letter: ").upper()
#if letter in word:
#  print(f"There is a letter named {letter} in the secret word")
#else:
#  print(f"There is not letter named {letter} in the secret word")

# students = {"Vinay", "Arun", "Kumar", "Praveen"}
# name = input("Enter your name: ").title()

# if name in students:
 #  print(f"Welcome {name}, you are a student")
# else:
  # print(f"Sorry {name}, you are not a student")


#grades = {"Sandy": "A","Squidward": "B","Spongebob" : "C","Patrick": "D"}
#key = input("Enter the name of a student: ").title()
#for key, value in grades.items():
 #print(f"{key}'s grade is {value}")

email ="imvinayachandran@gmail.com"
symbol = input("Enter the symbol: ")

if "@" in email and ".com" in email:
  print("Valid email")
else:
  print("Invalid email")