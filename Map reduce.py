# list=[1,6,2,4,5,8,6,4,7]
# even=0
# odd=0
# for i in list:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print(even)
# print(odd)


# for j in list:
#     j=j+2
#     print(j, end=" ")

# def is_even(n):
#     return n%2==0
#evens=list(filter(is_even,list1))
#equal to
# lambda n:n%2==0

from _functools import reduce
list1=[2,5,6,7,6,4,8,3,4]

evens=list(filter(lambda n:n%2==0,list1))

doubles=list(map(lambda n:n+2,evens))

sum=reduce(lambda a,b:a+b,doubles)

print(evens)
print(doubles)
print(sum)