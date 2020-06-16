y=[x**2 for x in range(10)]
print(y)

z=[x for x in range(1,11) if x%2==0]
print(z)

z=[x+3 for x in range(1,11) if x>5]
print(z)

a=[x if x>5 else x+1 for x in range(1,11) ]
print(a)

n=[x*10 for x in range(1,5)]
print(n)

import functools
c=[1,3,5,7]
b=functools.reduce(lambda l,k:l+k,c)
print(b)