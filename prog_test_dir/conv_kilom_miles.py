# Convert kilometers to miles
# Student Name
# 3/6/20

# The main function will prompt user for input.
# then call the convert function to perform the calculation and display the
# results.

def main():

    # Prompt user to enter a number of kilometers
    km = float(input("Enter the number of kilometers: "))

    # Call the convert function and pass the number of kilometers
    result = convert(km)

    # Display the number of miles
    print(km, "kilometers equals", format(result, ",.2f"), "miles")
    
# The convert function will calculate the number of miles equivalent
# to the kilometers entered
def convert(kilometers):
    # To calculate miles, multiply kilometers by 0.6214
    CONVERSION_FACTOR = 0.6214
    
    miles = kilometers * CONVERSION_FACTOR
    return miles

main()

