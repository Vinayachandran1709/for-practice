array = [1,2,3,4,5]
x = 6
for i in range(0, len(array)):
    if array[i] == x:
        print(i)
        break
else:
    print(f"{x} is not found")