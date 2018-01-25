#Maia Reynolds
#1/25/18
#distance2points.py - finds distance between two points

from math import sqrt
x1=int(input("Enter x1: "))
y1=int(input("Enter y1: "))
x2=int(input("Enter x2: "))
y2=int(input("Enter y2: "))
print("The Distance is ",sqrt(abs((x1-x2)**2)+abs((y1-y2)**2)))