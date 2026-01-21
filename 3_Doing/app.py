from flask import Flask , render_template , request

app=Flask(__name__)

@app.route("/")
def Home():
    return render_template("home.html")
    
@app.route("/form" , methods=["POST" , "GET"])
def ShowForm():
    return render_template("LoginForm.html")


@app.route("/submit" , methods=["POST" , "GET"])
def form():
    username=request.form.get("username")
    password=request.form.get("password")

    # if username=="sumit" and password=="pass":
    #     return render_template("welcome.html" , name=username)
    valid_users = {
        'admin':'123',
        'sumit43':'2020',
        'shivam':'234'
    }
    if username in valid_users and password == valid_users[username]:
        return render_template("welcome.html" , name=username)
    else:
        return "Invalid Credentials"


if __name__ == "__main__":
    app.run(debug=True, port=5001)