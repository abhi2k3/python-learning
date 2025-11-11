
for i in range(1,100,1):
    st = ""
    if i % 3 == 0:
        st += "fizz"
    if i % 5 == 0:
        st += "buzz"
    #print(st)
    if not st:
        st=i
    print(st)
    