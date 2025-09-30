rows=int(input("enter number of rows : "))
num=1
if(rows>0):
    for i in range(1,rows+1,1):

        for j in range(1,2*i,1):
            print(num, end=" ")
            num=num+1
        print("")
elif(rows == 0):
    print(" no pyramid will be printed as value is 0 ")
else:
    print("enter a positive value")
