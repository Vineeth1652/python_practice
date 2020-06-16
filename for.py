# Consider the string 's' contains the value 'tata consultancy services limited'.
# Determine the no. of vowels present in it, using the "while" loop.
# Store the number in the variable 'count', and print it.
s='tata consultancy services limited'
list=['a','e','i','o','u']
count=0

for char in s:
    if char in list:
        count=count+1
print(count)
# s = 'tata consultancy services limited'
# count = 0
# for i in s:
#   if(i == 'a' or i == 'e' or i == 'i' or i == 'u' or i == 'o' ):
#     count+=1
# print(count)
