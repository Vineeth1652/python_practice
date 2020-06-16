# Consider the string 's' contains the value 'tata consultancy services limited'.
# Determine the no. of vowels present in it, using the "while" loop.
# Store the number in the variable 'count', and print it.

s='tata consultancy services limited'
l=len(s)
print(l)
#vowel
count=0
counter=0

while(counter<l):
    if s[counter]=="a" or s[counter]=="e" or s[counter]=="i" or s[counter]=="o" or s[counter]=="u":
        count=count+1
    counter=counter+1
print(count)
# s='tata consultancy services limited'
# l=len(s)
# print(l)
# count=0
# counter=0
#
# while(counter<l):
#     if s[counter]!="a" or s[counter]!="e" or s[counter]!="i" or s[counter]!="o" or s[counter]!="u":
#         count=count+1
#     counter=counter+1
# print(count)

