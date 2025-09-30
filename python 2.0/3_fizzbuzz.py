
for i in range(1,100,1):
    st = ""
    if i % 3 == 0:
        st += "fizz"
    if i % 5 == 0:
        st += "buzz"
    if st:
        print(st)
    else:
        print(i)
    