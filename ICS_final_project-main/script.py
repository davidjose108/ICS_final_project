# ReDI School 
# Introduction to Computer Sciences_Hybrid
# Final Project: Multichoice Test
# Name: David Garrido de Sousa

# The project contemplates the result of five questions related to CS. 
# If the user gets right 3 or more questions, it is a PASS.
# Otherwise, it is a FAIL. 


# Introduction

def introduction(user):
    print(f'\nWelcome {user}! \n\nYou will be presented with five questions related to Computer Sciences. \nIf you get more than three questions right, you passed!\n')
name = input('Welcome to Test Your Knowledge\n\nPlease enter your name: \n')
name=name.capitalize()
introduction(name)

input ('Are you ready? ')



# Question 1
# Put title of table 
def question_1():
    import random
    number = random.randint(0, 255)
    number_in_binary = "{:08b}".format(number)
    print(f'\nQuestion 1\nWrite in binary the following number:{number}  \n128     64      32      16      8       4       2       1\n')
    a1=input(f'Remember to write in 8 bits, e.g. 20 = 00010100\n{number} in binary = ')
    while len(a1)!=8:
        print('\nTry again.\n')
        a1=input(f'Remember to write in 8 bits, e.g. 20 = 00010100\n128     64      32      16      8       4       2       1\n{number} in binary = ')
    if a1 == number_in_binary:
        a1_result = 1
        print(f'\nCorrect, {name}!\n')
    else:
        a1_result = 0
        print(f'\nNot quite :( \nThe correct answer is {number_in_binary}\n')
    return a1_result
    input('Next question? \n')




# Question 2
def question_2():
    import string
    print('Question 2\nAn Operating System is divided into Kernel and User Interface\nIn the kernel, there are several managers, which of the following is NOT inside the kernel: \na) File manager\nb) Memory manager\nc) I/O Manager\nd) Process manager\ne) Protocol manager')
    a2=input()
    # The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.
    # Use the maketrans() method to create a mapping table.
    # If a character is not specified in the dictionary/table, the character will not be replaced.
    # If you use a dictionary, you must use ascii codes instead of characters.
    a2=a2.translate(a2.maketrans("","",string.punctuation))
    a2 = f'{a2.upper()}'
    while a2 == 'MANAGER':
        print('Please specify which manager do you mean.')
        a2=input()
    if a2 == '':
        a2_result = 0
        print('Ups! Not exaclty.\nThe correct answer is E.\nThere is no Protocol manager in the Kernel\n')
    elif a2=='E' or a2=="PROTOCOLMANAGER" or a2=='PROTOCOL':
        print("That's right!\n")
        a2_result=1
    else:
        a2_result = 0
        print('Ups! Not exaclty.\nThe correct answer is E.\nThere is no Protocol manager in the Kernel.\n')
    input('Hit ENTER for next \n')
    return(a2_result)


# Question 3
def question_3():
    print('Question 3\nThe following statement requires a Boolean answer.\n\nPython uses a compiler to translate high level language to machine leve language.')
    a3=input('Is it True or False? ')
    # a3=f'{a3.capitalize}'
    while a3!='False' and a3!='True':
        print('Try again.\nThis question only accepts Boolean values.')
        a3=input('Python uses a compiler to translate high level language to machine leve language.\nIs it True or False? ')
    if a3 == 'False':
        a3=False
    if a3==False:
        print(f'\nYou nailed it, {name}!\n')
        a3_result=1
    else:
        print("\nIt is False.\nA compiler language translates the source code to machine language, therefore it is harder to debug than an interpreted language.\n")
        a3_result=0
    input('Next question? \n')
    return(a3_result)


#  Question 4
def question_4():
    print('Question 4\n  What would be the correct result for the following operation?')
    a4=input('24 // 10 = ')
    if a4=='2':
        print('You are a genius!\n')
        a4_result=1
    else:
        print('The right answer is 2.\nThe operator // gives the quotient when 24 is divided by 10, rounded to the next smallest whole number.\n')
        a4_result=0
    input('You are almost there.\n')
    return(a4_result)


# Question 5
def question_5():
    import string
    print('Question 5\n\n#!/usr/bin/env python\nsum = 0\ncount = 0\n_____ count < 5:\n   n = input("Please specify a number: ")\n   sum = sum + n\n   count = count + 1\nprint("The sum is " + str(sum)\n')
    a5=(input('What is the missing command in the script? '))
    a5 = f'{a5.upper()}'
    a5=a5.translate(a5.maketrans("","",string.punctuation))
    if a5=='WHILE':
        print('\nYou are a truly PYTHONist!')
        a5_result=1
    else:
        print(f'\n{a5} is not the correct answer.\nThe missing command is WHILE\nA while loop will repeat the instruction(s) inside the loop-body, as long a condition is True')
        a5_result=0
    input('\nYou are done!\n\nHit ENTER to see your score\n')
    return(a5_result)

#Score
total_score=question_1()+question_2()+question_3()+question_4()+question_5()
print(f'Your total score is {total_score}!')
if total_score >= 3:
    print("You passed the TEST!")
else:
    print("Let's review the slides one more time and try again\n")
    