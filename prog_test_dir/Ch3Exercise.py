# The purpose of this program is to covert a numeerical score into a letter grade.
# student name removed
# 2/14/2020

# Promt the user to enter a numerical score
score =float(input("Enter numerical score: "))


# Display the corresponding letter grade
# If the score entered is less than 0, print invalid score
# If the score entered is more than 100, print invalid score
if score < 0:
    print("invalid score")
elif score > 100:
    print("invalid score")
elif score >= 89.5 <= 100:
    print("A")
elif score >= 79.5 <= 89.4:
    print("B")
elif score >= 69.5 <= 79.4:
    print("C")
elif score >= 59.5 <= 69.4:
    print("D")
elif score >= 0 <= 59.4:
    print("F")

