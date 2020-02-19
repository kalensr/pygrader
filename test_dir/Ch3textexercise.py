# Convert numerical grades to letter grades according to the following scale.
# 89.5 to 100=A
# 79.5 to 89.4=B
# 69.5 to 79.4=C
# 59.5 to 69.4=D
# 0 to 59.4=F
# Jake Suman
# February 16, 2020
score = float(input('Enter your numerical grade'))
x = score
L_SCORE = 0
I_SCORE = 100
A_SCORE = 89.5
B_SCORE = 79.5
C_SCORE = 69.5
D_SCORE = 59.5
F_SCORE = 0
if score >= A_SCORE and score <= I_SCORE:
    print('Your grade is A.')
elif score >= B_SCORE and score < A_SCORE:
    print('Your grade is B. ')
elif score >= C_SCORE and score < B_SCORE:
    print('Your grade is C. ')
elif score >= D_SCORE and score < C_SCORE:
    print('Your grade is D. ')
elif score >= F_SCORE and score < D_SCORE:
    print('Your grade is F. ')
elif score > I_SCORE:
    print('Invalid Grade')
elif score < L_SCORE:
    print('Invalid Grade')
