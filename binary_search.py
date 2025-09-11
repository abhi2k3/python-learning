value=int(input("enter a value "))
a = [1]
print(type(a))
left = 0
right = len(a) - 1
flag = False
while left <= right:
    mid = (left + right) // 2
    if a[mid] == value:
        print(mid)
        flag=True
        break
    elif value < a[mid]:
        right = mid - 1
    elif value > a[mid]:
        left = mid + 1
if(flag != True ):
    print("element not found ")

