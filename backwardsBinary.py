#Maia Reynolds
#1/24/18
#backwardsBinary.py - converts number to binary

number=int(input("Enter number <256: "))
a=(number//128)*10**7
b=((number%128)//64)*10**6
c=((number%128%64)//32)*10**5
d=(number%128%64%32//16)*10**4
e=(number%128%64%32%16//8)*10**3
f=(number%128%64%32%16%8//4)*10**2
g=(number%128%64%32%16%8%4//2)*10
h=(number%128%64%32%16%8%4%2//1)
print("Binary= ",a+b+c+d+e+f+g+h)
