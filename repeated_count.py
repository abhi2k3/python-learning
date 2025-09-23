s=input("enter the string : ")
i=0
if ( len(s)!=0):
    count={}
    for i in range(len(s)):
        char=s[i]
        if char in count:
            count[char]=count[char] + 1
        else:
            count[char]=1
    for i in range
#     for char in count:
#         print(f"{char} appears {count[char]} times ")
# else:
#     print(" string is empty")
