def fizzbuzz(i):
    st = ""
    if i % 3 == 0:
        st += "fizz"
    if i % 5 == 0:
        st += "buzz"
    print(st)
    if not st:
        print(i)
for i in range(1,101,1):
    fizzbuzz(i)
