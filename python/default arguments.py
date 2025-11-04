#def net_price(list_price, discount=0, tax=0.05):
    #return list_price * (1 - discount) * (1 + tax)
#print(net_price(500, 0.1))

import time
def count(start = 0, end= 11):
    for x in range(start, end+1):
        #end + 1 other wise end value will be excluded 
        print(x)
        time.sleep(1)
        #time.sleep() is a function from Python’s built-in time module that tells the computer to pause (do nothing) for a certain number of seconds before continuing.
    print("Done")

count()