def topten():
    n=1
    while n<=10:
        sq=n*n
        yield sq
        n+=1
    yield 5
    yield 6
    yield 7
    yield 8

values=topten()

print(values)
print(values.__next__())
print(values.__next__())

for i in values:
    print(i)
