def reverse(s):
    str=" "
    for i in s:
        str=i+str
    return str
s=str(input("Enter the string:"))
print("The original string is:",s)
print("The reversed string is:",reverse(s))