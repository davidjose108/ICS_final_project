import string
print('Question 5\n\n#!/usr/bin/env python\nsum = 0\ncount = 0\n_____ count < 5:\n   n = input("Please specify a number: ")\n   sum = sum + n\n   count = count + 1\nprint("The sum is " + str(sum)\n')
a5=(input('What is the missing command in the script? '))
a5 = f'{a5.upper()}'
print(a5)
if a5=='WHILE':
    print('\nYou are a truly PYTHONist!')
    a5_result=1
else:
    print(f'\n{a5} is not the correct answer.\nThe missing command is WHILE\nA while loop will repeat the instruction(s) inside the loop-body, as long a condition is True')
    a5_result=0
input('\nYou are done!\n\nHit ENTER to see your score\n')
