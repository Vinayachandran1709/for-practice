#syntax - array('type_code',[])
#import array as a
from array import * #if you do this no need to insert a also 

#arr = array.array('type_code',[]) #type code means we define what type of data type we are going to 

arr = array('i',[1,2,3,4,5, -1, 0]) #if we use small i we can use both + and - values but in caps I we can use only + value
b = array('u',['a','b','c'])
print(arr)
print(b)
print(arr[5])
arr.insert(0,6) #0 is index position and 6 is value you want to insert
print(arr)
arr.pop(0) #delete operation just need to tell index position, if we don't say any index value in the bracket, the value in the last index position will be deleted
print(arr)

a = 5 #searching operation
for i in range(0, len(arr)):
    if arr[i] == a:
        print(i)
        break