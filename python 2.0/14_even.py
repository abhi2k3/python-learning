l=[1,2,3,4,5,6,7,-8,9,10]
for i in range(0,len(l),1):
    n = l[i] ^ 1 
    if n == l[i] + 1:
        print(l[i])