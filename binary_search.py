value=int(input("enter a value "))
a=[1,5,7,9,11,13,16,18,19,25,27]
left=0
right=len(a)-1
while left<=right:
    mid=(left+right)//2
    if a[mid]==value:
        print(mid)
        break
    elif value< a[mid]:
        right=mid-1
    elif value>a[mid]:
        left=mid+1
    else:
        print("value not found ")

