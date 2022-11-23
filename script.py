# ReDI School 
# Introduction to Computer Sciences_Hybrid
# Final Project: Multichoice Test
# Name: David Garrido de Sousa

# The project contemplates the result of five questions related to CS. 
# If the user gets right 3 or more questions, it is a PASS.
# Otherwise, it is a FAIL. 

# Introduction
name = input('Welcome to Test Your Knowledge\n Please enter your name: ')
print(f'Welcome {name}! \n You will be presented with five questions related to Computer Sciences. \n If you get more than three questions right, you passed!')
print('')
input ('Are you ready? ')
print('')

# Question 1
print('Question 1\nWrite in binary the following number: 194 \n 128     64      32      16      8       4       2       1')
a1=int(input('194 in binary: \nRemember to write in 8 bits, e.g. 20 = 00010100\n'))
if a1 == 11000010:
    a1_result = 1
    print(f'Correct, {name}!\n')
else:
    a1_result = 0
    print('Not quite :( \nThe correct answer is 11000010\n')

input('Next question? ')
print('')

# Question 2
print('Question 2\nAn Operating System is divided into Kernel and User Interface\nIn the kernel, there are several managers, which of the following is NOT inside the kernel: ')
a = 'a) File manager'
b = 'b) Memory manager'
c = 'c) I/O Manager'
d = 'd) Process manager'
e = 'e) Protocol manager'
print(f'{a}\n{b}\n{c}\n{d}\n{e}')
a2=input()
if a2 == 'e':
    print("That's right!\n")
    a2_result=1
else:
    a2_result = 0
    print('Ups! Not exaclty.\nThere is no Protocol manager in the Kernel\n')
