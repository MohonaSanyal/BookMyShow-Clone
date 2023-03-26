from flask import Flask, redirect, url_for, render_template, request, session, flash
from forms import RegistrationForm, LoginForm
from datetime import timedelta
import sqlalchemy
from dummydata import getDummyData
import json

dummy = getDummyData()

app = Flask(__name__)
app.secret_key = '4d22b856660b7fb47b460e1df938554d9c0c97c1a7f7c89a'
app.permanent_session_lifetime = timedelta(minutes = 5)

@app.route("/")
@app.route("/home")
def home(): 
    return render_template("home.html")

@app.route("/shows")
def shows():
    return render_template("shows.html", data = dummy, dump = json.dumps)


@app.route("/register", methods = ["POST", "GET"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("user_register.html", form = form)


@app.route("/login", methods = ["POST", "GET"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@bmc.com" and form.password.data == "admin":
            flash("You have been successfully logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login unsuccessful. Please check username and password", "danger")
    return render_template("user_login.html", form = form)
        

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

        return render_template("user.html", data = None)
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

@app.route("/modal")
def modal():
    return render_template("demodal.html")

if __name__ == '__main__':
    app.run(debug = True)