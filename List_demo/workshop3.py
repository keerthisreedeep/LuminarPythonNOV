
 #lst=[2,3,5]
 #o/p [8,7,5]

lst=[2,3,5,8]
total=sum(lst)
op=[]
for i in lst:
    num=total-i
    op.append(num)
print(op)
