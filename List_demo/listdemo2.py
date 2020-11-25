 lst=[10,11,12,13,14,15,16,17]
 print(lst)
#
# #itreration
#
# for item in lst:
#     print(item)
#
# #-------------------------------------
#
# #print sum of this list without using any pre defined function
#
 total=0
 for item in lst:
     total=total+item
 print(total)

# #------------------------------------------------
#
# #print all even numbers from list
#
 for item in lst:
     if (item%2==0):
        print(item)
# #or
#
 data=[i for i in lst if i%2 ]
 print(data)
#
# #----------------------------------------------
# #find sum of evn numbers and odd numbers from list
#
sumeven=0
sumodd=0
for item in list:
    if(item%2==0):
        sumeven=item+sumeven
    else:
        sumodd=item+sumodd

print("sum of even numbers is",sumeven)
print("sum of odd numbers is",sumodd)
#
# #--------------------------------------------
#






