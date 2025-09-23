a=[1,5,11,6,2,7]
d=[0]
target=13
if len(a) != 0:
    for i in range(0,len(a)-1,1):
        b=target-a[i]
        d[0]=b
        if(d[0] == a[i+1]):
            print(a[i],d[0])
#         for j in range(i+1,len(a),1):
#             sum = a[i]+a[j]
#             if(sum == target):
#                 print(f"{a[i]},{a[j]}")
# else :
#     print("Array is empty ")
