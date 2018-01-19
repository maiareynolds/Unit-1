#Maia Reynolds
#1/19/18
#isItaTriangle.py - determines if it could be a triangle

a=float(input("Enter Side A: "))
b=float(input("Enter Side B: "))
c=float(input("Enter Side C: "))

large=max(a,b,c)
smaller=((a+b+c)-large)
print(bool(smaller>large))