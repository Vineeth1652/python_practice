from array import *
from numpy import *

arr2=array[2,5,3]
print(type(arr2))

# arr=array('i',[3,5,7,9,10])
# print(type(arr))
# arr1=array(arr.typecode,(a*a for a in arr))
# print(arr1)
# for i in arr:
#     print("index of each element is: ", i ,arr.index(i))

arr=array('i',[])
x=int(input("eneter length of array: "))
for i in range(x):
    y=int(input("eneter number: "))
    arr.append(y)
print(arr)
z=int(input("eneter search: "))
for j in arr:
    if z==j:
        print("match")
        print(arr.index(z))
        break
else:
    print("match not found")