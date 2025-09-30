size=int(input("enter the size : "))
list=[]
for i in range(size):
    data=int(input(f"enter the data {i+1} : "))
    list.append(data)
print(list)
if(len(list)!=0):
    count={}
    for data in list:
        if data in count:
            count[data]=count[data]+1
        else:
            count[data]=1
    for data in count:
        if count[data] == 1:
            print(f"unique value : {data}")
    else:
        print("No unique values ")
else:
    print("List is empty ")