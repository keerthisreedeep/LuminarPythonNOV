#read two numbers and print largest amoung these two

#num1=int(input("enter the first number"))
#num2=int(input("enter the second number"))
#if(num1>num2):
    #print("num1 is the largest number")
#else:
    #print("num2 is the largest number")

    #-------------------------------------------------

#read two numbers and print largest amoung these two using elif

num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
if(num1>num2):
    print("num1 is the largest number")
elif(num2>num1):
    print("num2 is the largest number")
elif (num2 == num1):
    print("both numbers are equal")
