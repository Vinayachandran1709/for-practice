def day_week(day):
 if day == 1:
  return("It is Sunday")
 elif day == 2:
  return("It is Monday")
 elif day == 3:
  return("It is Tuesday")
 elif day == 4:
  return("It is Wednesday")
 elif day == 5:
  return("It is Thursday")
 elif day == 6:
  return("It is Friday")
 elif day == 5:
  return("It is Saturday")
 else:
  return("You are an idiot")
 
print(day_week(8))

#instead of so many you can match case like below

def day_week(day):
 match day:
  case 1:
   return("It is Sunday")
  case 2:
   return("It is Monday")
  case 3:
   return("It is Tuesday")
  case 4:
    return("It is Wednesday")
  case 5:
    return("It is Thursday")
  case 6:
    return("It is Friday")
  case 7:
    return("It is Saturday")
  case _:
    return("You are an idiot")
 
print(day_week(1))

#2nd example
def weekend(day):
 match day:
  case "Sunday":
   return True
  case "Monday":
   return("Not a weekend")
  case "Tuesday":
   return("Not a weekend")
  case "Wednesday":
    return("Not a weekend")
  case "Thursday":
    return("Not a weekend")
  case "Friday":
    return("Not a weekend")
  case "Saturday":
    return True
  case _:
    return("You are an idiot")
 
print(weekend("Sunday"))

#using operator 
def weekend(day):
 match day:
  case "Sunday" | "Saturday":
   return ("It is a weekend")
  case "Monday"|"Tuesday"|"Wednesday"|"Thursday"|"Friday":
   return("Not a weekend")
  case _:
    return("You are an idiot")
 
print(weekend("sunday"))