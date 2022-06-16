"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


connect_db(app)

# debug tool bar
from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
debug = DebugToolbarExtension(app)
# look into line below - Eve
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


#db.create_all()

@app.get("/")
def return_users_page():
    """Redirect to users page."""
    return redirect("/users")


@app.get("/users")
def list_users():
    """List users."""
    users = User.query.all()
    return render_template("home.html", users=users)


@app.get("/users/new")
def show_user_form():
    """Show new user form."""
    return render_template("create_user.html")


@app.post("/users/new")
def add_user():
    """Add new user and redirect to new user page (/users/user_id)."""
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    img_url = request.form['img_url']

    # need something similar for img_url if they dont submit url
    # hunger = int(hunger) if hunger else None

    user = User(first_name=first_name, last_name=last_name, img_url=img_url)
    db.session.add(user)
    db.session.commit()

    return redirect(f"/users/{user.id}")


@app.get("/users/<int:user_id>")
def show_user(user_id):
    """Show info on a single user."""
    user = User.query.get_or_404(user_id)
    return render_template("detail.html", user=user)

@app.get("/users/<int:user_id>/edit")
def show_edit_form_with_old_values(user_id):
    """shows user form"""
    user = User.query.get(user_id)
    return render_template("edit.html", user=user)


@app.post("/users/<int:user_id>/edit")
def edit_user(user_id):
    """Add user and redirect to users page."""
    edited_first_name = request.form['edited_first_name']
    edited_last_name = request.form['edited_last_name']
    edited_img_url = request.form['edited_img_url']

    user = User.query.get(user_id)
    user.first_name = edited_first_name
    user.last_name = edited_last_name
    user.img_url = edited_img_url
    db.session.commit()

    return redirect("/users")


@app.post("/users/<int:user_id>/delete")
def delete_user(user_id):
    """Delete user and redirect to users page."""

    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()

    return redirect("/users")