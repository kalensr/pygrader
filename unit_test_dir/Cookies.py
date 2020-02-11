# Purpose: calculate the amount of ingredients needed for
# a specified number of cookies.
# Name: Justin Moore
# Date: February 1, 2020

# Input: number of cookies
cookies = int(input("Enter the number of cookies: "))

# Create named contstants to calculate the amount of ingredeients needed
# for one cookie (we know the amount needed for 48 cookies, so we
# divide that by 48)
SUGAR = 1.5/48
BUTTER = 1/48
FLOUR = 2.75/48

# Multiply the number of cookies wanted by each ingredient (for one cookie)
sugarNeeded = SUGAR * cookies
butterNeeded = BUTTER * cookies
flourNeeded = FLOUR * cookies

# Output: number of cups of each ingredient
print("The amount of sugar needed is:", format(sugarNeeded, '.3f'), "cups")
print("The amount of butter needed is:", format(butterNeeded, '.3f'), "cups")
print("The amount of flour needed is:", format(flourNeeded, '.3f'), "cups")

# 24 cookies: 0.75, 0.5, 1.375
# 65 cookies: 2.03125, 1.35416666, 3.7239583333
