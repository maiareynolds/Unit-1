#Maia Reynolds
#1/19/18
#change.py - amount of money to change

cents=int(input("number of cents: "))
print("Quarters: ",int(cents//25))
print("Dimes: ",int(cents%25)//10)
print("Nickels: ",int((cents%25)%10)//5)
print("Pennies: ",int(((cents%25)%10)%5))