doubles = []
for x in range(1, 11):
  doubles.append(x * 2)
print(doubles)

#we can simplify this code by using list comprehension format

#[expression for value in iterable]
doubles = [x * 2 for x in range(1,11)]
print(doubles)
#we can do like this insetad of the above said loop format

#now with strings
fruits = ["apple","orange","banana","mango"]
upper_fruits = [fruit.upper() for fruit in fruits]
print(upper_fruits)

fruits = ["apple","orange","banana","mango"]
fruit_char = [fruit[0] for fruit in fruits]
print(fruit_char)
#character finding 

#now with if condition
numbers = [1, -2, -3, 4, -5, -6, 7]
positive_nums = [num for num in numbers if num >=0]
negative_nums = [num for num in numbers if num<0]
even_nums = [num for num in numbers if num % 2 == 0 and num > 0]
print(positive_nums)
print(negative_nums)
print(even_nums)
