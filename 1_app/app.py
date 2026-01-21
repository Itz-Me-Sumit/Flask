from flask import Flask , request

# Create Website.
app = Flask(__name__)
"""
    this "app" representing our Website.
    this is saying to flask that it is main file of website we are working on.
"""

# Creating "route" through help of decorator.
@app.route("/")
#this "@app.route" will tell flask that whenever someone will come to home page show code written after " @app.route("/") "
# route is used to connet specific web page to a specific function
# "app" is a flask object

def Home():
    return "Hello User This is my first Flask app"
"""
    this "def Home()" gonna return his return value whenever someone come to home page
"""


@app.route("/about")
def about_us():
    return "This is About_us Section"


@app.route("/contact")
def contact():
    return "This is Contact us page"


# Request
@app.route("/submit" , methods=["GET" , "POST"])
def submit():
    if request.method == "POST":
        return "You're Submitting or giving us Data"
    else:
        return "You're Viewing Data"

""" 
Flask accepts "GET" by Default , but to recive data we explictly have to write "POST".
"""






















# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello User This is my first Flask App"

# @app.route("/about")
# def about():
#     return "This is about us section"

# @app.route("/contact")
# def contact():
#     return "You Can Contact us here"

# @app.route("/submit" , methods=["GET","POST"])
# def submit():
#     if request.method == "POST":
#         return "You send data"
#     else:
#         return "You're Only viewing"