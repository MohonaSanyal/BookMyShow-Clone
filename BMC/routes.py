from flask import redirect, url_for, render_template, flash, request
from BMC import app, db, bcrypt
from BMC.forms import RegistrationForm, LoginForm, UpdateAccountForm, AdminRegistrationForm, AdminLoginForm, VenueForm, EditVenueForm, ShowForm, EditShowForm
from BMC.models import User, Admin, Venue, Show, Ticket
from flask_login import login_user, current_user, logout_user, login_required
from json import dumps

@app.route("/")
@app.route("/home")
def home(): 
    if app.config.get("ADMIN") == True:
        flash("Admin cannot access as an user", "warning")
        return redirect(url_for("admin"))
    if current_user.is_authenticated: # type: ignore
        return redirect(url_for("dashboard"))
    return redirect(url_for("login"))

@app.route("/profile/", methods = ["POST", "GET"])
@login_required
def profile():
    if app.config.get("ADMIN") == True:
        flash("Admin cannot access as an user", "warning")
        return redirect(url_for("admin"))
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash("Your Account Information Has been updated!", "success")
        return redirect(url_for("profile"))
    elif request.method == "GET":
        form.fullname.data = current_user.fullname # type: ignore
        form.username.data = current_user.username # type: ignore
        form.email.data = current_user.email # type: ignore
    return render_template("user_profile.html", user = current_user,form = form)

@app.route("/register/", methods = ["POST", "GET"])
def register():
    if app.config.get("ADMIN") == True:
        flash("Admin cannot access as an user", "warning")
        return redirect(url_for("admin"))
    if current_user.is_authenticated: # type: ignore
        flash("You are already logged in!", "info")
        return redirect(url_for("home"))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(fullname = form.fullname.data, username = form.username.data, email = form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash("Your Account Has been created! You can now Login", "success")
        return redirect(url_for("home"))
    return render_template("user_register.html", form = form)

@app.route("/login/", methods = ["POST", "GET"])
def login():
    if app.config.get("ADMIN") == True:
        flash("Admin cannot access as an user", "warning")
        return redirect(url_for("admin"))
    if current_user.is_authenticated: # type: ignore
        return redirect(url_for("home"))
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

@app.route("/logout/")
@login_required
def logout():
    if app.config.get("ADMIN") == True:
        flash("Admin cannot access as an user", "warning")
        return redirect(url_for("admin"))
    logout_user()
    flash("You have been logged out!", "info")
    return redirect(url_for("home"))

@app.route("/dashboard/")
@login_required
def dashboard():
    if app.config.get("ADMIN") == True:
        flash("Admin cannot access as an user", "warning")
        return redirect(url_for("admin"))
    return render_template("user_dashboard.html",user = current_user, venues = Venue.query.all(), shows = Show.query.all(), dumps = dumps)

@app.route("/book", methods = ["POST"])
@login_required
def book():
    if app.config.get("ADMIN") == True:
        flash("Admin cannot access as an user", "warning")
        return redirect(url_for("admin"))
    if request.method == "POST":
        user_id = request.form.get("form_user_id")
        venue_id = request.form.get("form_venue_id")
        show_id = request.form.get("form_show_id")
        num_tickets = request.form.get("form_tktQuantity")
        total_price =  request.form.get("form_tktTotal")
        ticket = Ticket(show_id = show_id, user_id = user_id, venue_id = venue_id, num_tickets = num_tickets, total_price = total_price)
        show = Show.query.filter_by(id = show_id).first()
        show.tickets-=int(num_tickets) # type: ignore
        db.session.add(ticket)
        db.session.commit()
        flash("Tickets Booked successfully!", "success")
        return redirect(url_for("bookings"))
    return redirect(url_for("dashboard"))

@app.route("/bookings/")
@login_required
def bookings():
    if app.config.get("ADMIN") == True:
        flash("Admin cannot access as an user", "warning")
        return redirect(url_for("admin"))
    return render_template("user_bookings.html",bookings = Ticket.query.filter_by(user_id=current_user.id), venues = Venue.query.all(), shows = Show.query.all(), dumps = dumps) # type: ignore

@app.route("/admin/")
@app.route("/admin/home/")
def admin():
    return redirect(url_for("admin_login"))

@app.route("/admin/register/", methods = ["POST", "GET"])
def admin_register():
    if current_user.is_authenticated and app.config.get('ADMIN'): # type: ignore
        return redirect(url_for("admin_dashboard"))
    if current_user.is_authenticated and not app.config.get('ADMIN'): # type: ignore
        flash("You are not an admin!", "danger")
        return redirect(url_for("home"))
    form = AdminRegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        admin = Admin(email = form.email.data, password = hashed_password)
        db.session.add(admin)
        db.session.commit()
        flash("Your Account Has been created! You can now Login", "success")
        return redirect(url_for("admin_login"))
    return render_template("admin_register.html", form = form)

@app.route("/admin/login/", methods = ["POST", "GET"])
def admin_login():
    if current_user.is_authenticated and app.config.get('ADMIN'): # type: ignore
        return redirect(url_for("admin_dashboard"))
    if current_user.is_authenticated and not app.config.get('ADMIN'): # type: ignore
        flash("You are not an admin!", "danger")
        return redirect(url_for("home"))
    form = AdminLoginForm()
    if form.validate_on_submit():
        admin = Admin.query.filter_by(email = form.email.data).first()
        if admin and bcrypt.check_password_hash(admin.password, form.password.data):
            login_user(admin)
            next_page = request.args.get("next")
            app.config['ADMIN'] = True
            flash("You have been logged in!", "success")
            return redirect(next_page) if next_page else  redirect(url_for("admin_dashboard"))
        else:
            flash("Login unsuccessful. Please check email and password", "danger")
    return render_template("admin_login.html", form = form)

@app.route("/admin/logout/")
def admin_logout():
    if not app.config.get('ADMIN'): # type: ignore
        flash("You are not an admin!", "danger")
        return redirect(url_for("logout"))
    logout_user()
    app.config['ADMIN'] = False
    flash("You have been logged out!", "info")
    return redirect(url_for("admin_login"))



@app.route("/admin/dashboard/")
def admin_dashboard():
    if not app.config.get('ADMIN'): # type: ignore
        flash("You are not an admin!", "danger")
        return redirect(url_for("home"))
    return render_template("admin_dashboard.html", venues = Venue.query.all(), shows = Show.query.all())

@app.route("/admin/summary/")
def admin_summary():
    if not app.config.get('ADMIN'): # type: ignore
        flash("You are not an admin!", "danger")
        return redirect(url_for("home"))
    return render_template("admin_summary.html")

@app.route("/admin/venue-new/", methods = ["POST", "GET"])
def admin_venue_new():
    if not app.config.get('ADMIN'): # type: ignore
        flash("You are not an admin!", "danger")
        return redirect(url_for("home"))
    form = VenueForm()
    if form.validate_on_submit():
        venue = Venue(name = form.name.data, place = form.place.data, location = form.location.data, capacity = form.capacity.data)
        db.session.add(venue)
        db.session.commit()
        flash("Venue has been added!", "success")
        return redirect(url_for("admin_dashboard"))
    return render_template("admin_venue_new.html", form = form)

@app.route("/admin/venue-edit/<int:venue_id>", methods = ["POST", "GET"])
def admin_venue_edit(venue_id):
    if not app.config.get('ADMIN'): # type: ignore
        flash("You are not an admin!", "danger")
        return redirect(url_for("home"))
    form = EditVenueForm()
    venue = Venue.query.get_or_404(venue_id)
    if form.validate_on_submit():
        venue.name = form.name.data
        venue.place = form.place.data
        venue.location = form.location.data
        venue.capacity = form.capacity.data
        db.session.commit()
        flash("Venue has been updated!", "success")
        return redirect(url_for("admin_dashboard"))
    elif request.method == "GET":
        form.name.data = venue.name
        form.place.data = venue.place
        form.location.data = venue.location
        form.capacity.data = venue.capacity
    return render_template("admin_venue_edit.html", form = form, venue = venue)

@app.route("/admin/venue-delete/<int:venue_id>", methods = ["POST", "GET"])
def admin_venue_delete(venue_id):
    if not app.config.get('ADMIN'): # type: ignore
        flash("You are not an admin!", "danger")
        return redirect(url_for("home"))
    venue = Venue.query.filter_by(id = venue_id).first()
    shows = Show.query.filter_by(venue_id = venue_id).all()
    for show in shows:
        db.session.delete(show)
    db.session.delete(venue)
    db.session.commit()
    flash("Venue has been deleted!", "success")
    return redirect(url_for("admin_dashboard"))

@app.route("/admin/<int:venue_id>/show-new", methods = ["POST", "GET"])
def admin_show_new(venue_id):
    if not app.config.get('ADMIN'): # type: ignore
        flash("You are not an admin!", "danger")
        return redirect(url_for("home"))
    form = ShowForm()
    if form.validate_on_submit():
        form.venue_id.data = venue_id
        show = Show(venue_id = form.venue_id.data, title = form.title.data, rating = form.rating.data, time = form.time.data, tags = form.tags.data, price = form.price.data, tickets = form.tickets.data)
        db.session.add(show)
        db.session.commit()
        flash("Show has been added!", "success")
        return redirect(url_for("admin_dashboard"))
    if request.method == "GET":
        venue_capacity = Venue.query.filter_by(id = venue_id).first().capacity
        form.venue_id.data = venue_id
        form.tickets.data = venue_capacity
        
    return render_template("admin_show_new.html", form = form)

@app.route("/admin/show-edit/<int:show_id>", methods = ["POST", "GET"])
def admin_show_edit(show_id):
    if not app.config.get('ADMIN'): # type: ignore
        flash("You are not an admin!", "danger")
        return redirect(url_for("home"))
    form = EditShowForm()
    show = Show.query.filter_by(id = show_id).first()
    if form.validate_on_submit():
        show.venue_id = form.venue_id.data
        show.title = form.title.data
        show.rating = form.rating.data
        show.time = form.time.data
        show.tags = form.tags.data
        show.price = form.price.data
        show.tickets = form.tickets.data
        db.session.commit()
        flash("Show has been updated!", "success")
        return redirect(url_for("admin_dashboard"))
    elif request.method == "GET":
        form.venue_id.data = show.venue_id
        form.title.data = show.title
        form.rating.data = show.rating
        form.time.data = show.time
        form.tags.data = show.tags
        form.price.data = show.price
        form.tickets.data = show.tickets
    return render_template("admin_show_edit.html", form = form, show_id = show_id)

@app.route("/admin/show-delete/<int:show_id>", methods = ["POST", "GET"])
def admin_show_delete(show_id):
    if not app.config.get('ADMIN'): # type: ignore
        flash("You are not an admin!", "danger")
        return redirect(url_for("home"))
    show = Show.query.filter_by(id = show_id).first()
    db.session.delete(show)
    db.session.commit()
    flash("Show has been deleted!", "success")
    return redirect(url_for("admin_dashboard"))




