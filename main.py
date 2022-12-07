
from flask import Flask
from flask import request, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
total_score = 0


app = Flask(__name__)

user = ""
the_name = ""
@app.route("/")
def index():
    global user
    user = request.args.get("user","")
    if user:
        user = introduction(user)
    else:
        user = ""
    return (
        """<body>
        <h1>Welcome to Test your Knowledge!</h1>
        </body>
            <form action="" method="get">
                Please enter your name: <input type="text" name="user">
                <input type="submit" value="Submit">
            </form>"""
        + ""
        + user
    )

def introduction(user):
    # user = request.args.get("user","")
    global the_name
    the_name = user
    return (
        f'Welcome {user.capitalize()}! You will be presented with five questions related to Computer Sciences. If you get more than three questions right, you passed!'
        """<h1></h1>
        <form action="/question_1" method="get">
                <input type="submit" value="Click to start">
        </form>"""
        ) 

import random
number = random.randint(0, 255)
number_in_binary = "{:08b}".format(number)
a = random.randint(0,1000)
b = 10
c=a//b


@app.route("/question_1")
def question_1():
    global total_score
    total_score = 0
    a1 = request.args.get("a1", "") 
    if a1:
        a1 = answer_1()
    else:
        a1 = ""
    return (
        """
        <h1>Question 1</h1>
        <h3>Write the following number in binary: </h3>"""
        f'{number}'
        """<h1></h1>
        <a href="https://sites.google.com/site/syhsguzmancsp/creative-projects/binary-numbers">Click on the link below for refresh</a>
        <h4>Example</h4>
        <table>
            <tr>
                <th>128</th>
                <th>64</th>
                <th>32</th>
                <th>16</th>
                <th>8</th>
                <th>4</th>
                <th>2</th>
                <th>1</th>
                <th></th>
            </tr>
            <tr>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td>1</td>
                <td>0</td>
                <td>1</td>
                <td>0</td>
                <td>0</td>
                <th>= This binary number 00010100 represents this decimal number 20</th>
            </tr>
        </table>
        <h3>       </h3>
        <form action="" method="get">
            <input type="int" name="a1">
            <input type="submit" value="Submit answer">
        </form>"""
        +""
        + a1     
    )

def answer_1():
    global total_score
    global user
    global the_name
    a1 = request.args.get("a1", "")
    if a1 == number_in_binary:
        total_score = total_score + 1
        return(
            """<h1></h1>"""
            f'Correct, {the_name}!'
                """<h1></h1>
                <form action="/question_2" method="get">
                        <input type="submit" value="Next question">
                </form>"""
            
            )
    else:
        return(
            """<h3>Not quite :( The correct answer is </h3>""" 
            f'{ number_in_binary }'
            """<h3></h3>""" 
            """<form action="/question_2" method="get">
                    <input type="submit" value="Next question">
            </form>"""
            )

@app.route("/question_2")
def question_2():
    a2 = request.args.get("a2","")
    import string
    if a2:
        a2= answer_2()
    else:
        a2 = ""
    return (
        """<body>
        <h1>Question 2</h1>
        <h3>An Operating System is divided into Kernel and User Interface.</h3> 
        <h3>In the kernel, there are several managers, which of the following is NOT inside the kernel:</h3>
        <h3>a) File Manager</h3>
        <h3>b) Memory Manager</h3>
        <h3>c) I/O Manager</h3>
        <h3>d) Process Manager</h3>
        <h3>e) Protocol Manager</h3>
        <h3></h3>
        <form action="" method="get">
            <input type="text" name="a2">
            <input type="submit" value="Submit answer">
        </form></body>"""
        +""
        + a2)
    # The translate() method returns a string where some specified characters are replaced with the character described in a dictionary, or in a mapping table.
    # Use the maketrans() method to create a mapping table.
    # If a character is not specified in the dictionary/table, the character will not be replaced.
    # If you use a dictionary, you must use ascii codes instead of characters.
    
def answer_2():
    global total_score
    import string
    a2 = request.args.get("a2", "")
    a2=a2.translate(a2.maketrans("","",string.punctuation))
    a2 = f'{a2.upper()}'
    # while a2 == 'MANAGER':
    #     return('Please specify which manager do you mean.')
    #     a2=input()
    if a2=='E' or a2=="PROTOCOLMANAGER" or a2=='PROTOCOL':
        total_score = total_score + 1
        return("""That's right!
        <h3></h3> 
            <form action="/question_3" method="get">
                    <input type="submit" value="Next question">
            </form>""")
    else:
        return("""Ups! Not exactly.The correct answer is E.There is no Protocol Manager in the Kernel.
        <h3></h3> 
            <form action="/question_3" method="get">
                    <input type="submit" value="Next question">
            </form>""")

@app.route("/question_3")
def question_3():
    a3 = request.args.get("a3","")
    if a3:
        a3= answer_3()
    else:
        a3 = ""
    return (
        """<body>
        <h1>Question 3</h1>
        <h3>Is the following statement True or False?</h3>
        <h3></h3>
        <h3>"Python uses a compiler to translate high level language to machine level language."</h3> 
        <form action="" method="get">
                Remember to submit a Boolean answer <input type="text" name="a3">
                <input type="submit" value="Submit">
            </form>"""
        + ""
        + a3)

def answer_3():
    global total_score
    a3 = request.args.get("a3", "")
    while a3!='False' and a3!='True':
        return ('Try again.\nThis question only accepts Boolean values.')
        a3= ""
    if a3 == 'False':
        a3=False
    if a3==False:
        total_score = total_score + 1
        return (f'You nailed it, {user}!'
        """<h3></h3> 
            <form action="/question_4" method="get">
                    <input type="submit" value="Next question">
            </form>""")
    else:
        return(
            """<h3>It is False.</h3> 
            <h3>Python is an interpreted language, which means the source code of a Python program is converted into bytecode that is then executed by the Python virtual machine.</h3>
            <form action="/question_4" method="get">
                    <input type="submit" value="Next question">
            </form>""")
        

@app.route("/question_4")
def question_4():
    a4 = request.args.get("a4", "")
    if a4:
        a4=answer_4()
    else:
        a4=""
    return("""<body>
        <h1>Question 4</h1>
        <h3>What would be the correct result for the following operation?</h3>
        <h3></h3>"""
        
        """<h3></h3>
            <form action="" method="get">"""
                f'{a} // {b} =  '"""<input type="int" name="a4" size="4">
                <input type="submit" value="Submit">
            </form>"""
        + ""
        + a4)

def answer_4():
    global total_score
    a4 = request.args.get("a4", "")
    a4 = int(a4)
    if a4 == c:
        total_score = total_score + 1
        return(
            f'{a4}'
            """You are a genius!"""
            """<h3></h3> 
            <form action="/question_5" method="get">
                    <input type="submit" value="Click for the last question!">
            </form>""")
        
    else:
        return(
            f'{a4}'
            """ is not the correct answer. The right answer is """ f'{c}'
            """. The operator // gives the quotient when """ f'{a}' """ is divided by 10, rounded to the next smallest whole number."""
            """<h3></h3> 
            <form action="/question_5" method="get">
                    <input type="submit" value="Click for the last question!">
            </form>""")
        

@app.route("/question_5")
def question_5():
    a5 = request.args.get("a5", "")
    if a5:
        a5=answer_5()
    else:
        a5=""
    return("""<head>
    <style type="text/css">
    <!--
    .tab { margin-left: 40px; }
    -->
    </style>
    </head>
    <body>
        <h1>Question 5</h1>
        <h3>What is the missing command in this script? </h3>
        <h3></h3>
        <p>#!/usr/bin/env python</p>
        <p>sum = 0</p>
        <p>count = 0</p>
        <p>_____ count < 5:</p>
        <p class="tab">    n = input("Please specify a number: ")
        <p class="tab">   sum = sum + n
        <p class="tab">   count = count + 1
        <p class="tab">    print("The sum is " + str(sum))</p3>
        """
        
        """<h3></h3>
            <form action="" method="get">"""
                """<input type="text" name="a5" size="4">
                <input type="submit" value="Submit">
            </form>"""
        + ""
        + a5)

def answer_5():
    global total_score
    import string
    a5 = request.args.get("a5", "")
    a5 = f'{a5.upper()}'
    a5=a5.translate(a5.maketrans("","",string.punctuation))
    if a5=='WHILE':
        total_score = total_score + 1
        return(
            f'{a5}'
            """You are a truly PYTHONist!"""
            """<h3></h3> 
            <form action="/final_score" method="get">
                    <input type="submit" value="Click to see your results!">
            </form>""")
        
        
    else:
        return(
            f'{a5}'""" is not the correct answer."""
            """The missing command is WHILE. A while loop will repeat the instruction(s) inside the loop-body, as long a condition is True"""
            """<h3></h3> 
            <form action="/final_score" method="get">
                    <input type="submit" value="Click to see your results!">
            </form>""")
        


@app.route("/final_score")
def final_score():
    return (f'{total_score}')
    # print(a1_result)
    # final_score = a1_result + a2_result + a3_result + a4_result + a5_result
    # if final_score >= 3:
    #     return("""<h1>You passed the TEST!</h1>""")
    # else:
    #     return("""<h1>Let's review the slides one more time and try again</h1>
    #     <form action="/" method="get">
    #                 <input type="submit" value="Try again">
    #         </form>""")




if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)