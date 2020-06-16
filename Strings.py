# Create a string 's1' by concatenating two strings with values "Py" and 'thon'. Print 's1'.
# Consider the string 's2' with value 'Python is amazing'. Print 's2'.
# Consider the string 's3' with value 'Python\nis\namazing'. Print 's3'.
# Consider the string 's4' with value 'Python\tis\tamazing'. Print 's4'.

# s1="Py"+'thon'
# print(s1)
# s2='Python is amazing'
# print(s2)
# s3='Python\nis\namazing'
# print(s3)
# s4='Python\tis\tamazing'
# print(s4)

# Consider the string 's1' with value 'Python\nis\namazing'.
# Convert it to a raw string, named 'rs1', and print it.
# Consider the string 's2' with value 'Python\tis\tamazing'.
# Convert it to a raw string, named 'rs2', and print it.

# s1='Python\nis\namazing'
# rs1=r'Python\nis\namazing'
# print(rs1)
# s2='Python\tis\tamazing'
# rs2=r'Python\tis\tamazing'
# print(rs2)

# Check if 's' has alphabets only.
# Check if 's' has digits only.
# Determine the length of 's'.
# Convert all characters of 's' into upper case.
# Convert all characters of 's' into lower case.
# Find how many 'i' s are there in 's'.
# Find the index position of character 't' in '

# s="INfinity"
# print(s.isalpha())
# print(s.isdigit())
# print(len(s))
# print(s.upper())
# print(s.lower())
# print(s.count('i'))
# print(s.index('t'))

# x=input("enter string: ")
# reverse=""
#
# for i in x:
#     reverse=i+reverse
# print(reverse)

# x=input("enter string: ")
# l=len(x)
#
# for i in range(1,l+1):
#     for j in range (i):
#         print(x[j],end="")
#     print()

# for i in range(5,0,-1):
#     for j in range (i):
#         print(j,end="")
#     print()
#
#
# for i in range(5,0,-1):
#     for j in range (i):
#         print(i,end="")
#     print()

n=0
for i in range(1,5):
    for j in range (i):
        print(n,end="")
        n+=1
    print()
