#print all even nos in between upper limit and lower limit
l=int(input("enter lower limit"))
u=int(input("enter upper limit"))
if(l>u):
    print("upper limit should be greater than lower limit")
while(l<=u):
    if(l%2==0):
        print(l)
    l+=1