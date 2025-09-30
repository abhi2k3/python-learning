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

# for num in numbers:
#     if is_power_of_two(num):
#         print(num, "is a power of 2")
#     else:
#         print(num, "is NOT a power of 2")