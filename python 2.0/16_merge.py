l1=['apple',"banana",3.12,4,5]
l2=[3,4,5,6,7]
for i in range(0,len(l1)-1,1):
    for j in range(0,len(l2)-1,1):
        if l1[i] == l2[j]:
            l2.remove(l1[i])
    l2.append(l1[i])
print(l2)
