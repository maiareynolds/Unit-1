#Maia Reynolds
#1/18/19
#binarypy - converting binary to decimal

binary=int(input("Enter an 8-digit binary number: "))
a=int((binary//10**7)*2**7)
b=int(((binary%10**7)//10**6)*2**6)
c=int(((binary%10**7)%10**6//10**5)*2**5)
d=int(((binary%10**7)%10**6%10**5//10**4)*2**4)
e=int(((binary%10**7)%10**6%10**5%10**4//10**3)*2**3)
f=int(((binary%10**7)%10**6%10**5%10**4%10**3//10**2)*2**2)
g=int(((binary%10**7)%10**6%10**5%10**4%10**3%10**2//10)*2)
h=int((binary%10**7)%10**6%10**5%10**4%10**3%10**2%10)
print(a+b+c+d+e+f+g+h)