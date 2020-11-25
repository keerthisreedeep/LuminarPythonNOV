num=int(input("enter a number"))
result=0
while(num!=0):
    temp=num%10
    result=(result)+(temp**3)
    num=num//10
print(result)
