# #input list or array
#
# ar=[6,4,5,2,1,3]
#
# #input of binary search is always a sorted array
#
# ar.sort() # sort() is used for sorting an iterable
# print(ar) #[1,2,3,4,5,6]
#
# low=0
# upper=len(ar)
# print(upper)
# #calculate mid position
#
# mid=(low+upper)//2#0+6//2=3
#
# #element to search=5
#
# #case1 element>ar[mid]
# #5>ar[3]
# if(element>ar[mid]):
#     low=mid+1
#     #low=4
# mid=(4+upper)//2 #4+6//2=5
#
# #element>ar[mid]5<5
# # case2 :5==5 element found
# # case3 :5<5

#----------------------------------------------------
#-------------------------------------------------------
#pgm for binary search
#input list or array
ar=[6,4,5,2,1,3]
#step sort
ar.sort()
low=0
upp=len(ar)
element=int(input("enter element for search"))
while(low<=upp): #0<6 4<6
    mid=(low+upp)//2 #mid=3 4+6//2=5
    #[1,2,3,4,5,6]
    #case1
    if(element>ar[mid]): #5>ar[3] 5>4 5>5
        low=mid+1 #low=3+1=4
    elif(element<ar[mid]):#5<5
        upp=mid-1
    elif(element==ar[mid]): #5==5
        print("element found")
    break