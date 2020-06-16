list=[5,6,7,9,45,12,18]


n=45

# for i in list:
#     if i==n:
#         print("value found at: ",list.index(i))

# for i in range(len(list)):
#     if list[i]==n:
#         pos=i
#         print("element found at ", i)
i=0
while i<len(list):
    if list[i]==n:
        pos=i
        print("element found at ", i)
    i+=1



