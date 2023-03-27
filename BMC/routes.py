from flask import redirect, url_for, render_template, flash, request
from BMC import app, db, bcrypt
from BMC.forms import RegistrationForm, LoginForm, UpdateAccountForm
from BMC.models import User
from BMC.dummydata import getDummyVenueData, getDummyShowData, getDummyBookingData
from flask_login import login_user, current_user, logout_user, login_required
import json

dummyVenues, dummyShows =   getDummyVenueData(), getDummyShowData()
dummyBookings = getDummyBookingData()

@app.route("/")
@app.route("/home")
def home(): 
    if current_user.is_authenticated: # type: ignore
        return redirect(url_for("shows"))
    return redirect(url_for("login"))

@app.route("/dashboard")
@login_required
def shows():
    return render_template("dashboard.html",user = current_user, venues = dummyVenues, shows = dummyShows , dump = json.dumps)

@app.route("/bookings")
@login_required
def bookings():
    return render_template("bookings.html",bookings = dummyBookings, dump = json.dumps)

@app.route("/profile", methods = ["POST", "GET"])
@login_required
def profile():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your Account Information Has been updated!", "success")
        return redirect(url_for("profile"))
    elif request.method == "GET":
        form.username.data = current_user.username # type: ignore
        form.email.data = current_user.email # type: ignore
    return render_template("user_profile.html", user = current_user,form = form)

@app.route("/register", methods = ["POST", "GET"])
def register():
    if current_user.is_authenticated: # type: ignore
        flash("You are already logged in!", "info")
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your Account Has been created! You can now Login", "success")
        return redirect(url_for("home"))
    return render_template("user_register.html", form = form)


@app.route("/login", methods = ["POST", "GET"])
def login():
    if current_user.is_authenticated: # type: ignore
        return redirect(url_for("user"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            next_page = request.args.get("next")
            flash("You have been logged in!", "success")
            return redirect(next_page) if next_page else  redirect(url_for("home"))
        else:
            flash("Login unsuccessful. Please check email and password", "danger")
    return render_template("user_login.html", form = form)
        
    
@app.route("/logout")
def logout():
    logout_user()
    flash("You have been logged out!", "info")
    return redirect(url_for("home"))

