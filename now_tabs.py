# Jake Suman
# April 23,2020
# Debug Exercise 3 (Chapter 7)
# Design a program that asks the user to enter a store's sales for each day
# of the week.  The amounts should be stored in a list.  Use a loop to
# calculate the total sales for the week and display the result.
# Note: the result should be formatted with two decimal places
def main():
	daily_sales = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
	days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

	i = 0
	total = 0.0
	
	for i in range(7):
		print("Enter the amount of sales for", days_of_week[i])

		daily_sales[i] = float(input("Enter the sales here: "))
		
		total += daily_sales[i]

	print("The total sales for the week is :", format(total, '.2f'), sep = ' ')
main()
