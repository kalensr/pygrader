# This program will add a series of positive numbers and display the sum.
# An unknown amount of numbers will be entered, so a sentinel value is used
# to indicate the end of the series of numbers.
# <student name>
# February 21, 2020

# Input: Prompt the user to enter positive numbers
# and enter a negative number when they want to stop entering numbers to be added.
print("Enter a series of positive numbers to be added together.")
print("Enter a negative number to signal when you want to stop entering numbers.")
number = float(input("Enter a positive number, or a negative number to stop: "))

# Initialize the value of the sum variable to zero.
sum = 0

# Create a loop to enter the series of numbers.
# The loop will stop when a negative number is entered.
# Then the total will be displayed.
while number >= 0:
    sum = sum + number
    number = float(input("Enter a positive number, or a negative number to stop: "))

# Output: sum the series of positive numbers entered
print ("The sum of the numbers entered is", format(sum, ",.2f"))
