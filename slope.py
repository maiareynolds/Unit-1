#Maia Reynolds
#1/17/18
#slope.py - calculates slope of line given two points

x1=int(input("X1= "))
y1=int(input("Y1= "))
x2=int(input("X2= "))
y2=int(input("Y2= "))
slope=(y1-y2)/(x1-x2)
print("The slope of the line is",slope)
c=-((slope*x1)-y1)
print("The equation of the line is Y= ",slope,"X+",c)