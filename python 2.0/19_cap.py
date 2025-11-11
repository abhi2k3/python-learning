# name = input("enter your name : ")
# if('A' <= name[0]<='Z'):
#     print(f"Hi {name}! ")
# else :
#     name=chr(ord(name[0]) - 32) + name[1:]
#     print(f"Hi {name}! ")   
#st = input("write some sentence : ")
def capitalize(st):
    if('a' <= st[0]<='z'):
        st=chr(ord(st[0]) - 32) + st[1:]
    elif not ('a' <= st[0]<='z'):
        if st[1] == " ":
            st= st[:1]+" "+ chr(ord(st[1]) - 32) + st[2:]
        else:
            st= st[:1]+ chr(ord(st[1]) - 32) + st[2:]
    for i in range(0,len(st)-1,1):
        if st[i] == " ":
            j = i+1
            if('a' <= st[j]<='z'):
                st=st[:j-1]+" "+chr(ord(st[j]) - 32) + st[j+1:]
    return st
l=["this is a test", "This is a test", "2 percent of people pass this test", "_test is a string",
     "$400 is the charge", "  my name is abHiram", "& my name is Rajesh", "  This is       a test","( this is abhi )"]
for st in l:
    print(st,"=>",capitalize(st),"==>",st.title())