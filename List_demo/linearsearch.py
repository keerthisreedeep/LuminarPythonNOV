
#search for an element in list
lst=[]
lst = input("enter the elements in the list")
search=int(input("search item"))
flag=0
for item in lst:
    if(item==search):
        flag=1
        break
    else:
        flag=0
if (flag>0):
    print("item found in the list")
else:
    print("item not in the list")