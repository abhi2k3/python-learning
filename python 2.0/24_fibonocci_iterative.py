n=int(input("enter number : "))
a=0
b=1
c=0
count=0
if n < 0:
    print("enter positive number ")
elif n == 1:
    print(a)
elif n == 0:
    print("no numbers is printed ")
else:
    for i in range(0,n,1):
        
        a=b
        b=c
        c=a+b
        print(f"{i} : {b}")

