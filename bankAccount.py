#Maia Reynolds
#1/25/18
#bankAccount.py - finds number of years for money to reach certain amount

from math import log10
start=int(input("Enter starting value: "))
interest=float(input("Enter interest rate as a decimal: "))
compound=int(input("Enter how many times per year interest is compounded: "))
final=float(input("Enter the final amount of money you want: "))
print("It will take",(log10(final/start)/log10(1+(interest/compound)))/compound,"years")