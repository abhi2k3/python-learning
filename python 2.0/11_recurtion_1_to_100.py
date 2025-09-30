def num(n):
    if n == 0:
        return(0)
    else :
        value  = num(n-1) + 1
        print(value)
        return value

n = 100
num(n)