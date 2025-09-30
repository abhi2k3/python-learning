st=input("Enter the string : ")
if(len(st)!=0):
    count={}
    for data in st:
        if data in count:
            count[data]=count[data]+1
        else:
            count[data]=1
    for data in count:
        if count[data] == 1:
            print(f"unique value : {data}")
            break
    else:
        print("No unique values ")
else:
    print("string is empty ")