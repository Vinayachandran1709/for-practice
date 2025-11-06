#def wishes(greetings, first, last):
 #   print(f"{greetings} {first} {last}")
#wishes("happy birthday", "vinaya", "chandran" )

#for x in range(1, 11):
 # print(x, end = "-")

def get_code(country, code, first, last):
  return f"{country} : {code} - {first} {last}"

print(get_code(country="India",code="91", first="Vinaya", last="Chandran"))