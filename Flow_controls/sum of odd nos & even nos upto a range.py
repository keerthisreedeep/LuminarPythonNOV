#calculate sum of odd nos & even nos upto a range
low=int(input("enter the lower limit"))
upp=int(input("enter the upper limit"))
sumeven=0
sumodd=0
for i in range(low,upp):
    if(i%2==0):
        sumeven=1+sumeven
    else:
        sumodd=1+sumodd
        i=i+1
print("sum of even numbers is",sumeven)
print("sum of odd numbers is",sumodd)