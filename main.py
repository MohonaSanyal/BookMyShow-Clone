from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import sqlalchemy
from dummydata import getDummyData

dummy = getDummyData()

app = Flask(__name__)
app.secret_key = "BHSN1378nsdf6avnb8"
app.permanent_session_lifetime = timedelta(minutes = 5)

@app.route("/")
@app.route("/home")
def home(): 
    return render_template("home.html")

@app.route("/shows")
def shows():
    return render_template("shows.html", data = dummy)

@app.route("/login", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user", methods = ["POST", "GET"])
def user():
    email = None
    if "user" in session:
        flash("Successfully logged in!", "info")
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email = email)
    else:
        if "user" in session:
            flash("You are already logged in!", "info")
            return redirect(url_for("user"))
        
        return redirect(url_for("login"))
    
@app.route("/logout")
def logout():
    flash("You have been logged out!", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("login"))

if __name__ == '__main__':
    app.run(debug = True)