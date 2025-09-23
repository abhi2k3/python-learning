name = input("enter your name : ")
if('A' <= name[0]<='Z'):
    print(f"Hi {name}! ")
else :
    name=chr(ord(name[0]) - 32) + name[1:]
    print(f"Hi {name}! ")   
age = int(input("enter your age : "))
print(f"your age is {age} ")
height = float(input("Enter height : "))
print(f"height = {height} cm ")
weight = float(input("Enter weight : "))
print(f"weight = {weight} kg ")
bmi= weight / ((height / 100) * (height / 100))
print(f"your bmi is: {bmi} kg/m^2 ")