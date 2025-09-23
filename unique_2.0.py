l=[1,2,3,4,5,4,3,2,1]
t=[]
for i in range(len(l)):

    if l[i] in t:
        j[0]+=1
        break
    else:
        t.append([1,l[i]])

for j in t:
    if j[0]==1:
        print(j)