def fizzbuzz(i):
    st = ""
    if i % 3 == 0:
        st += "fizz"
    if i % 5 == 0:
        st += "buzz"
    if st:
        print(st)
    else:
        print(i)
for i in range(1,101,1):
    fizzbuzz(i)
