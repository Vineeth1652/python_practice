n=int(input("Enter number: "))
result=0
#
# while n>0:
#     rem=n%10
#     result=result+rem
#     n=n//10
# print(result)

for i in range(len(str(n))):
    rem=n%10
    result=result+rem
    n=n//10
print(result)