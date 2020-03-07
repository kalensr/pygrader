# Debug Exercise 3
# Write a program that asks the user to enter the amount that he or she
# budgeted for the month.  A loop should then prompt the user to enter
# each of his or her expenses for the month and keep a running total.
# When the loop finishes, the program should display the amount that
# the user is over or under budget.
    
budget = float(input('Enter amount budgeted for the month: '))
spent = float(input('Enter an amount spent(0 to quit): '))
# moved spent = statement above the while loop, for initial setting

total = 0
# need to define total outside of loop

while spent > 0:
    # change from = to >
    total = total + spent
    spent = float(input('Enter an amount spent(0 to quit): '))
    # need to accumulate total, change from = to =+
    
print ('Budgeted: $', format(budget, '.2f'))
print ('Spent: $', format(total, '.2f'))   
if budget > total:
    difference = budget - total
    print ('You are $', format(difference, '.2f'), \
           'under budget. WELL DONE!')
elif budget < total:
    difference = total - budget
    print ('You are $', format(difference, '.2f'), \
           'over budget. PLAN BETTER NEXT TIME!')
elif budget == total:
    print ('Spending matches budget. GOOD PLANNING!')
