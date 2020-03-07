# Debug Exercise 2
# Create a change-counting game that gets the user to enter the number of
# coins required to make exactly one dollar.  The program should prompt
# the user to enter the number of pennies, nickels, dimes, and quarters.
# If the total value of the coins entered is equal to one dollar, the
# program should congratulate the user for winning the game.  Otherwise,
# the program should display a message indicating whether the amount
# entered was more than or less than one dollar.

numPennies = int(input('Enter the number of pennies: '))
numNickels = int(input('Enter the number of nickels: '))
numDimes = int(input('Enter the number of dimes: '))
numQuarters = int(input('Enter the number of quarters: '))
# need to convert the above to floats

totalCentValue = numPennies + (numNickels * 5) + (numDimes * 10) + (numQuarters * 25)
# convert count of coins to cents - above

totalDollars = totalCentValue / 100
if totalDollars > 1:
    # correct spelling with variable above, lower case 'd', changed to uppercase 'D'
    print('Sorry, the amount you entered was more than one dollar.')
elif totalDollars < 1:
    # corrected syntax above with else/if statement
    print('Sorry, the amount you entered was less than one dollar.')
else:
    print('Congratulations!')
    print('The amount you entered was exactly one dollar!')
    print('You win the game!')

