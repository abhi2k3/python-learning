def typ_cast(s):
    result = 0
    index = 0
    while index < len(s):
        char = s[index]
        digit = ord(char) - ord('0')
        result = result * 10
        result = result + digit
        index = index + 1
    return result
    
s = input("enter the integer : ")
print(type(s))
if len(s) > 0 and s[0] == '-':
    s = s[1:]
    result = typ_cast(s)
    result = -result
else:
    result = typ_cast(s)

print(result)
print(type(result))