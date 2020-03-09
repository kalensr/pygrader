# Debug Exercise 2
# Create a change-counting game that gets the user to enter the number of
# coins required to make exactly one dollar.  The program should prompt
# the user to enter the number of pennies, nickels, dimes, and quarters.
# If the total value of the coins entered is equal to one dollar, the
# program should congratulate the user for winning the game.  Otherwise,
# the program should display a message indicating whether the amount
# entered was more than or less than one dollar.

# Input: Prompt the user for pennies, nickles, dimes, and quarters. 

Penny_value = 1
Nickel_value = 5
Dime_value = 10
Quarter_value = 25

pennies = int(input('Enter the number of pennies: '))
nickels = int(input('Enter the number of nickels: '))
dimes = int(input('Enter the number of dimes: '))
quarters = int(input('Enter the number of quarters: '))

# Total the value of pennies, nickles, dimes, and quarters.
# Represented as the number of pennies
penny_total = pennies * Penny_value
nickel_total = nickels * Nickel_value
dime_total = dimes * Dime_value
quarter_total = quarters * Quarter_value
totalCentValue = penny_total + nickel_total + dime_total + quarter_total
print(totalCentValue)
# Determine the dollar amount
totalDollars = totalCentValue / 100

# Output: determine which message to print depending on the dollar amount
if totalDollars > 1:
    print('Sorry, the amount you entered was more than one dollar.')
elif totalDollars < 1:
    print('Sorry, the amount you entered was less than one dollar.')
else:
    print('Congratulations!')
    print('The amount you entered was exactly one dollar!')
    print('You win the game!')

