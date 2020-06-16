list=[10,30,40,45,50,55,60,75]
l=0
u=len(list)-1


n=55
while l<=u:
    m=(l+u)//2
    if list[m]==n:
        print("found at: ", m)
        break
    else:
        if list[m]<n:
            l=m

        break