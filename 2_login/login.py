from flask import Flask , request , Response , redirect , url_for , session 

app = Flask(__name__)
app.secret_key = "kisi_ko_pata_nahi_chalna_chahiye"

@app.route("/" , methods = ["GET" , "POST"])

# Creating Home Page (Login Page)
def Login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username == "admin" and password == "123":
            session["user"] = username
            return redirect(url_for("welcome_page"))
        else:
            return Response("Invalid , Try Again" , mimetype="text/plain")
        
    return """
        <h1>Login Here</h1>
        <form method="POST">
            <label for="username">UserName</label>
            <input type="text" id="username" name="username">
            <br><br>
            <label for="pass">Password</label>
            <input type="password" id="pass" name="password">
            <br><br>
            <button type="Submit" value="login">Login</button>
        </form>
"""

# welcome page
@app.route("/welcome" )
def welcome_page():
    if "user" in session:
        return f"""
            <h1>Welcome {session["user"]}! To This App</h1>
            <a href={url_for('logout')}>Logout</a>
            """
    return redirect(url_for("Login"))


# logout page
@app.route("/logout")
def logout():
    session.pop("user" , None)
    return redirect(url_for("Login"))
    


if __name__ == "__main__":
    app.run(debug=True, port=5001)