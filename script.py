# ReDI School 
# Introduction to Computer Sciences_Hybrid
# Final Project: Multichoice Test
# Name: David Garrido de Sousa

# The project contemplates the result of five questions related to CS. 
# If the user gets right 3 or more questions, it is a PASS.
# Otherwise, it is a FAIL. 

# Introduction
name = input('Welcome to Test Your Knowledge\n Please enter your name: ')
print(f'Welcome {name}! \n You will be presented wit five questions related to the Computer Sciences. \n If you get more than three questions right, you passed!')
ready = input ('Are you ready? ')

# Question 1
print('Write in binary the following number: 194 \n 128     64      32      16      8       4       2       1')
a1=int(input('194 in binary: \nRemember to write in 8 bits, e.g. 20 = 00010100\n'))
if a1 == 11000010:
    a1_result = 1
    print(f'Correct, {name}!')
else:
    print('Not quite :( \nThe correct answer is 11000010')

# Question 2
