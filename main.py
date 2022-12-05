
from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    user = request.args.get("user", "")
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
    return (
        f'Welcome {user.capitalize()}! You will be presented with five questions related to Computer Sciences. If you get more than three questions right, you passed!'
        """<h1></h1>
        <form action="/question_1" method="get">
                <input type="submit" value="Click to start">
        </form>"""
        )   

number_in_binary = ""
@app.route("/question_1", methods=['GET'])
def question_1():
    import random
    number = random.randint(0, 255)
    number_in_binary = "{:08b}".format(number)
    a1 = ""
    return render_template("question_1.html", number = number, number_in_binary=number_in_binary, a1 = a1)   

@app.route("/question_1", methods=['POST'])
def answer_1():
    a1 = request.args.get ("a1","")
    user = request.args.get("user","")
    print(a1, number_in_binary, type(a1), type(number_in_binary))
    if a1 == number_in_binary:
        a1_result = 1
        return(
            f'Correct, {user}!'
            """<h1></h1>
            <form action="/question_2" method="get">
                    <input type="submit" value="Next question">
            </form>""")
    else:
        a1_result = 0
        return(
            """<h3>Not quite :(. The correct answer is {{ number_in_binary }}</h3>
            <form action="/question_2" method="get">
                    <input type="submit" value="Next question">
            </form>""")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)