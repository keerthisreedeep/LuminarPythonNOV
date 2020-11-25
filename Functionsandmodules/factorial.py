#pgm to create a function for finding factorial of a number
# n=int(input("enter a number"))
# def factorial(n):
#     if (n==0):
#         return 1
#     else:
#         return n*factorial(n-1)
print(factorial(n))

#-----------------------------------------------
def fact(num)
    fact=1
    for i in range((1,num+1)):
        fact=fact*i
    print(fact)
number=int(input("enter number to find factorial"))
fact(number)
# function with argument and no return value
#-----------------------------------------------------
def factorial(num):
    fact=1
    for i in range(1,(num+1)):
    fact=fact*i
    return fact
print(factorial(5))