a=[1,2,3,4]
b=[0,0,0,0]
c=[0,0,0,0]
print(a,b,c)
print()
i=len(a)-1
j=len(b)-1
k=len(c)-1
if(c[k] == 0):
    c[k] = a[0]
    a[0] = 0
    print(a,b,c)
    print()
    if(b[j] == 0):
        b[j]=a[1]
        a[1] = 0
        print(a,b,c)
        print()
    if(b[j]> c[k]):
        b[j-1] = c[k]
        c[k]=a[i]
        a[i]=0
        print(a,b,c)
        print()
    if(a[i] == 0):
        a[i]=b[j-1]
        b[j-1]=0
        print(a,b,c)
        print()
        c[k-1]=b[j]
        b[j]=0
        print(a,b,c)
        print()
        c[0]=a[i]
        a[i]=0  
print(a,b,c)
print()
        