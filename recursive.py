# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# num=int(input("Enter any number: " ))
# r=fact(num)
# print(r)

#factorial
# n=int(input("entre anu numne: "))
# i=1
# for j in range(4,0,-1):
#     i=i*j
# print(i)

#Fibonaccu
# i=1
# for j in range(5):
#     i=i+j
#     print(i)

#Prime
# x=int(input("Enter number: "))
# y=int(input("Enter number: "))
#
# for z in range(x,y+1):
#     if z>1:
#         for i in range(2,z):
#             if z%i==0:
#                 break
#                 print(" Not prime")
#         else:
#             print("not prime",z)
#
# n=int(input("Enter number: "))
# for i in range(2,n):
#     if n%i==0:
#         break
# else:
#     print("prime", n)
#perfect numbers

n=int(input("Enter number: "))
temp=0
for i in range(1,n):
    if n%i==0:
        temp=temp+i
if temp==n:
    print("erfect numbe")
else:
    print("not perfect")
