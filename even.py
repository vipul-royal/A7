n=(11,445,124,27,97,5,3,61,46)
codd=0
ceven=0
for i in n:
        if not i%2:
            ceven=ceven+1
        else:
            codd=codd+1
print("Number of even numbers :",ceven)
print("Number of odd numbers :",codd)