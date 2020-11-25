#lst=[1,2,3,4] #6 (2,4)  ,  #7 (3,4)
# lst=[1,2,3,4]
# pair = input("enter the element ")
# for item in lst:
#
#     for i in lst:
#             sum=0
#             if(item!=i):
#                 sum=item+i
#                 if(pair==sum):
#                     print(item,',',i)
#                     break


#------------------------------------------------------

lst=[1,2,3,4] #7 (3,4)

element=int(input("enter element"))
lst.sort()
low=0
upp=len(lst)-1
while(low<upp):
    total=lst[low]+lst[upp]
    if(total==element):
        print("pairs",lst[low],",",lst[upp])
        break
    elif(total>element):
        upp=upp-1
    elif(total<element):
        low+=1

