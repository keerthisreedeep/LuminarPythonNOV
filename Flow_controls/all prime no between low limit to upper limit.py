# print all prime nos between lower limit to upper limit
low = int(input("enter the lower limit"))
upp = int(input("enter the upper limit"))
for Number in range (low, (upp+1)):
    flag = 0

    for i in range(2, (Number // 2 + 1)):

        if (Number % i == 0):
            flag = flag + 1
            break
    if (flag == 0 and Number != 1):
        print( Number, end=' ')
