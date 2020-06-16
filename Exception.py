# a=10
# b=0
#
# try:
#     print(a/b)
# except Exception as e:
#     print("this block executes if try block results to error: ",e)
# finally:
#     print("if we got error or not")
#
# print("bye")

list=[1,2,3,4,5]


try:
    print(list[5])
except Exception as e:
    print("this block executes if try block results to error: ",e)
finally:
     print("if we got error or not")


