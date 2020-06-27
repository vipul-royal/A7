t=0
gcd=0
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
x=a
y=b
while b!=0:
    t=b
    b=a%b
    a=t
gcd=a
print("The GCD of",x,"and",y,"is:",gcd)