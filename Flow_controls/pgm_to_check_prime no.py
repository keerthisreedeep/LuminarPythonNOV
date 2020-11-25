number=int(input("enter a number"))
flag=0
for i in range(2,number):
    if(number%i==0):
        flag=1
        break
    else:
        flag=0
if(flag>0):
        print("number is not a prime number")
else:
        print("number is prime number")


