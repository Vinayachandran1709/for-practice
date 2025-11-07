#args
#def add(*args):
#total = 0
 # for arg in args:
  #total += arg
  #return total
#print(add(1,2,3))

#exit()

#kwargs
def print_address(**kwargs):
  for key, value in kwargs.items():
    print(f"{key}: {value}")

print_address(street="3/3, Govinda Singh Street", city="Chennai", state="Tamilnadu",country="India")