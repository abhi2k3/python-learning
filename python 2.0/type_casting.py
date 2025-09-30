def typ_cast(s):
    result = 0
    index = 0
    if len(s) > 0 and s[0] == '-':
        for index in range(1,len(s),1):
            char = s[index]
            digit = ord(char) - ord('0')
            result = result * 10
            result = result + digit
        result = -result
    else:
        while index < len(s):
            char = s[index]
            digit = ord(char) - ord('0')
            result = result * 10
            result = result + digit
            index = index + 1
    print(result)
    print(type(result))
    return result
s = input("enter the integer : ")
print(type(s))
typ_cast(s)
