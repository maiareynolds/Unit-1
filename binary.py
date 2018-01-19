#Maia Reynolds
#1/18/19
#binarypy - converting binary to decimal

binary=int(input("Enter an 8-digit binary number: "))
a=int((binary//10000000)*128)
a2=binary%10000000
b=int((a2//1000000)*64)
b2=a2%1000000
c=int((b2//100000)*32)
c2=b2%100000
d=int((c2//10000)*16)
d2=c2%10000
e=int((d2//1000)*8)
e2=d2%1000
f=int((e2//100)*4)
f2=e2%100
g=int((f2//10)*2)
h=f2%10
print(a+b+c+d+e+f+g+h)