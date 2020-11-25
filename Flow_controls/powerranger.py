#2
#2+22=24
#3+33+333=369
#4+44+444+4444

#---------------------------------

number=input("enter number")
i=1
total=0
while(i<=int(number)):
    print(number*i)
    data=number*i
    total=total+int(data)
    i+=1
print(total)