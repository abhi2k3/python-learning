name = input("enter your name : ")
if('A' <= name[0]<='Z'):
    print(f"Hi {name}! ")
else :
    name=chr(ord(name[0]) - 32) + name[1:]
    print(f"Hi {name}! ")   