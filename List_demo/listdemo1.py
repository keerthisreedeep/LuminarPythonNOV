#-------------------------------------------
#-------------------------------------------

# public class Helloworld{
#     public static void main(string []args){
#       System.out.println("helloworld"):
#
#       String[] name=new string[3]
# name[0]="csk";
# name[1]="kee";
# name[2]="csr";
# name[3]="gbb";
# }
# }

#-------------------------------------------
#-------------------------------------------

#list

#---------------------------------
#we can define list by using [] or we can define empty list by using list()
lst=[] # or ()
print (type(lst))

#----------------------------------
# we can store same and different types of data inside list object
lst=["lum",2017,true]
print(lst)

#-----------------------------------
#  we can store duplicate values
lst=["lum",2017,true, "lum"]
print(lst)

#-----------------------------------------
# list object is mutable(updation is possible)
lst=["ajay",29,25000]
print(lst)
print(lst[0])
lst[0]="vijay"
print(lst)
