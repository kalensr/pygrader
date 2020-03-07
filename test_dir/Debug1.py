# Debug Exercise 1
# Write a program that calculates the total amount of a meal
# purchased at a restaurant.  The program should ask the user
# to enter the charge for the food, then calculate the amount
# of a 18 percent tip and 7 percent sales tax.  Display each of
# these amounts and the total formatted with two decimal places.

TAX_RATE = 0.07
TIP_RATE = 0.18
food = float(input("Enter the charge for food: "))
#corrected syntax error above

tip = food * TIP_RATE
tax = food * TAX_RATE
total = food + tip + tax
print ("Tip: $", format(tip, '2f'))
print ("Tax: $", format(tax, '2f'))
print ("Total: $", format(total, '2f'))
