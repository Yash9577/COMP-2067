
L1=[5,-34,0,98,-1,244,193,28,-10,-20,45,67]#defining list l1
print("L1 =",L1)#printing list L1
n=len(L1)#this calculates length of list and stores into variable n
x=int(input("Enter an integer x in the range 0 to "+str(n-1)+": "))#ask user to enter the value of x
#check that user entered value is in range
if x>=0 and x<=n-1:
    #if x is in range then run the following lines
    print("The x_th element of L1 is:",L1[x])#print x_th element if exists
    if x in L1:
        print(x,"occurs in L1 at position:",L1.index(x))
    else:
        print(x,"does not occur in L1")
    if x%2==0 and x>0:
        print("The first",x,"elements of L1",L1[:x])#print first x elements
    if x%2!=0 and x>0:
        print("The last",x,"elements of L1",L1[len(L1)-x:])#print last x elements
    if x==0:
        print("L1: []")
#otherwise x is not in range then display the message
else:
    print("You did not enter a valid input!")
