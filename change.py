#Maia Reynolds
#1/19/18
#change.py - amount of money to change

cents=int(input("number of cents: "))
print("Quarters: ",int(cents//25))
First=int(cents%25)
print("Dimes: ",First//10)
Second=int(First%10)
print("Nickels: ",Second//5)
Third=int(Second%5)
print("Pennies: ",Third)