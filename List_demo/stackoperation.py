# data structures
#------------------------------------------------------------------------------------------
#different types of data structures

#------------------------------------------------------------------------------------------
#Two different types of data structurs
#-----------------------------------------------------------------------------------------
#1. Linear  data structures
#-----------------------------------------------------------------------------------------

    # array={10,20,30,40} --> elements are stored in consicutive memmory location
    # array[0]
    # array[1]
    #.............................................................................
    #eg: stack
    #stack operation :push (insert an element to stack) & pop(remove an element from stack)
    #LIFO-->LAST IN FIRST OUT

#.................................................................................
# array,queue

#-----------------------------------------------------------------------------------------
#2. Non linear data structures--> elements are not stored in consicutive memmory location
#-----------------------------------------------------------------------------------------
    #eg: linked list
    # node[data 10,next address of b ]--> node[data 20,next address of c ]--> node[data 30,next]
    #       a                                                     b                   c
    #..........................................................................................
    #  eg: binary search tree
            #[20,18,17,19,25,23,24]
                #tree(root,left,right)

               # Traversal methods through this nodes
                        #in order-->left root right
                        #pre order -->
                        #post order-->
    #.........................................................................................
    #  eg: tree, graph
    #.........................................................................................
size=int(input("enter size"))
stk=[]
top=0
def push(element):
    global top
    if(top>(size-1)):
        print("stack full")
    else:

        stk.append(element)
        top+=1
def pop():
    print("inside pop")
def display():
    print("inside display")
n=1
while(n!=0):
    option=int(input("enter operation 1) push 2) pop 3) display"))
    if(option==1):
        element=int(input("enter element to push"))
        push(element)
    elif(option==2):
        pop()
    elif(option==3):
        display()
n=int(input("do u want to continue press 0 for exit 1"))
