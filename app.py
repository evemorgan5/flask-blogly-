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
def list_users():
    """List pets and show add form."""

    users = User.query.all()
    return render_template("home.html", users=users)


@app.get("/create_user")
def show_user_form():
    """shows user form"""
    return render_template("create_user.html")


@app.post("/create_user")
def add_user():
    """Add user and redirect to list."""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    img_url = request.form['img_url']

    # need something similar for img_url if they dont submit url
    # hunger = int(hunger) if hunger else None

    user = User(first_name=first_name, last_name=last_name, img_url=img_url)
    db.session.add(user)
    db.session.commit()

    return redirect(f"/{user.id}")

@app.get("/<int:user_id>/edit_user")
def show_edit_form():
    """shows user form"""
    return render_template("edit.html")


@app.post("/<int:user_id>/edit_user")
def edit_user(user_id):
    """Add user and redirect to list."""
    edited_first_name = request.form['edited_first_name']
   # edited_last_name = request.form['edited_last_name']
    #edited_img_url = request.form['edited_img_url']

    user = User.query.get(user_id)
    user.first_name = edited_first_name

    print(user)
    db.session.commit()

    return redirect("/")


@app.get("/<int:user_id>")
def show_user(user_id):
    """Show info on a single user."""

    user = User.query.get_or_404(user_id)
    return render_template("detail.html", user=user)
