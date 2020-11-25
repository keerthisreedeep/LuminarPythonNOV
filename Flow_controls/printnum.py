#print numbers between low limit to upper limit
l=int(input("enter lower limit"))
u=int(input("enter upper limit"))
if(l>u):
    print("upper limit should be greater than lower limit")
while(l<=u):
    print(l)
    l+=1