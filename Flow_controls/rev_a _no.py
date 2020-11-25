#(123 to 321 )
#pgm to reverse a number

num=int(input("enter a number"))
result=0
while(num!=0):
    temp=num%10
    result=(result*10)+temp
    num=num//10
print(result)

