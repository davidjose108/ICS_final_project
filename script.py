# ReDI School 
# Introduction to Computer Sciences_Hybrid
# Final Project: Multichoice Test
# Name: David Garrido de Sousa

# The project contemplates the result of five questions related to CS. 
# If the user gets right 3 or more questions, it is a PASS.
# Otherwise, it is a FAIL. 

# Introduction
name = input('Welcome to Test Your Knowledge\n Please enter your name: ')
print(f'Welcome {name}! \n\nYou will be presented with five questions related to Computer Sciences. \nIf you get more than three questions right, you passed!')
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

input('Next question? \n')

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

input('Hit ENTER for next \n')

# Question 3
print('Question 3\nThe following statement requires a Boolean answer.\n\nA compiler programming language can be run on different platforms, regardless for what system it was built into.')
a3=bool(input('Is it true or false?'))
if a3==0 or a3==False:
    print(f'You nailed it, {name}!')
    a3_result=1
else:
    print("A compiler language writes for an specific OS.\nThe instructions in binary code in WindowsOS are different from MacOS.\n")
    a3_result=0

input('Next question? \n')

# Question 4
print('Question 4\n  What would be the correct result for the following operation?')
a4=int(input('24 // 10 = '))
if a4==2:
    print('You are a genius!\n')
    a4_result=1
else:
    print('The operator // gives the quotient when 24 is divided by 10, rounded to the next smallest whole number.\n')
    a4_result=0

input('You are almost there.\n')

#Question 5
print('#!/usr/bin/env python\nsum = 0\ncount = 0\n_____ count < 5:\n   n = input("Please specify a number: ")\n   sum = sum + n\n   count = count + 1\nprint("The sum is " + str(sum)\n\n')
a5=(input('What is the missing command in the script?: \n'))
if a5=='WHILE' or 'while' or 'While':
    print('You are a truly PYTHONist!')
    a5_result=1
else:
    print('The missing command is WHILE\nA while loop will repeat the instruction(s) inside the loop-body, as long a condition is True')

input('You are done!\nHit ENTER to see your score\n')

#Score
total_score=a1_result+a2_result+a3_result+a4_result+a5_result
print(f'Your total score is {total_score}!')
if total_score >= 3:
    print("You passed the TEST!")
else:
    print("Let's review the slides one more time and try again")
    