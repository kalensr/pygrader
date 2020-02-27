# Steven Howard
# February 19, 2020
# Use a loop to calculate the compound interest due to the user at the end of
# each year for 20 years at a rate of 4%.
# The program will start out at 2018 and will calcualte the interest for 20 years.

# The Constants are
RATE = .04
year = 2018

# Promt the user to enter a deposit amount
current_balance = float(input("Enter your deposit amount: "))

# Make sure you print the Table Headings
print()
print('Year\t   Amount')
print('----       ------')

total_interest = 0
interest_earned = 0

# Print the years 2018 through 2038 and their values of interest
for year in range(2018, 2038 + 1):
    total_interest += interest_earned
    interest_earned = current_balance * RATE
    print(f"{year}\t{current_balance:>10,.2f}")
    current_balance += interest_earned

#Print statement showing total interest earned
print(f"\nTotal interest earned: {total_interest:,.2f}")
