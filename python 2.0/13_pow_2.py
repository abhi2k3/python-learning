def pow_2(n):
    if n <= 0:
        return(print("enter positine number "))

    s = n & (n - 1)

    if s == 0:
        print("power of 2 ")
    else:
       print("Not a power of 2 ")


n = int(input("enter the number "))
pow_2(n)