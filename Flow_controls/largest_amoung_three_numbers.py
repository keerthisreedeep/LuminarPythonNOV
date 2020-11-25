#read 3 nos and print largest amoung 3

num1=int(input("enter the first number"))
num2=int(input("enter the second number"))
num3=int(input("enter the third number"))
if(num1>num2) & (num1 > num3):
    print("first number is the largest number")
elif (num1 < num2) & (num2 > num3):
    print("second number is the largest number")
elif (num2 < num3) & (num1 < num3):
    print("third number is the largest number")
elif (num1 == num2 == num3):
    print("all three numbers are equal")


    #------------------------------------------------------


# import functools
# lst=[10,50,25]
# max=functools.reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
# print(max)



