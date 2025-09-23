lst = [1,2,3,4,4,4,3,2,2,3,1]
for i in range(len(lst)):
    for j in range(0, len(lst) - i - 1):
        if lst[j] < lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
print(lst)