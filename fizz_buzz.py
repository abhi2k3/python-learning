i = 1
pri=''
while(i <= 100):
    # if i % 3 == 0 and i % 5 == 0 :
    #     print("fizzbuzz")
    if i % 3 == 0:
        pri += " fizz"
        print(pri)
    if i % 5 == 0:
        pri += "buzz"
        print(pri)
    
    else:
        print(i)
    i = i + 1
