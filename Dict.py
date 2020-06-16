# Create an empty Dictionary, 'd1' using the 'dict' function.
# Print 'd1'.
# Create a Dictionary 'd2' with key values p-play , t-talk.
# Print 'd2'.
# Add two new key values: v-vibe, d-docs.
# Print 'd2'.
# Remove the key value pair, 'v' - vibe, from 'd2'
# print 'd2'
d1=dict()
print(d1)
d2={"p":"play","t":"talk"}
print(d2)
d2['v']='vibe'
d2['d']='docs'
print(d2)
del d2["v"]
print(d2)

list=[1,2,3,4,5]

dict1=dict.fromkeys(list) #Used to create list from ieterators

print(dict1)

dict1.setdefault(6) # finds for the value in dict, if not it will insert into it
print(dict1)

d2.update(dict1) #adds two dictionries
d2.update(x=5,y=10)
print(d2)




