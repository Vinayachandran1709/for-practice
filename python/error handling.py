try:
    number = int(input("Enter the number: "))
    print(1 / number)
except ZeroDivisionError:
    print("You are dividing it with zero")
except ValueError:
    print("Enter valid numbers please")
except Exception:
    print("Something went wrong")
finally:
    print("Do something good for the society")