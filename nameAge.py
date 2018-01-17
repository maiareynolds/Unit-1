#Maia Reynolds
#1/17/18
#nameAge.py - characters in names and age next year

fullName=input("Enter your first and last name: ")
age=int(input("Enter your age: "))
first,last=fullName.split( )
print("Your first name has",len(first),"letters")
print("Your last name has",len(last),"letters")
print("Next year you will be",age+1,"years old")