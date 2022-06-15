"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, Users

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


# line of code below given to us in file
# db.create_all()




@app.get("/")
def list_users():
    """List pets and show add form."""

    users = Users.query.all()
    return render_template("userinterface.html", users=users)


@app.post("/")
def add_user():
    """Add user and redirect to list."""

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    img_url = request.form['img_url']

    # need something similar for img_url if they dont submit url
    # hunger = int(hunger) if hunger else None

    user = Users(first_name=first_name, last_name=last_name, img_url=img_url)
    db.session.add(user)
    db.session.commit()

    return redirect(f"/{user.id}")


@app.get("/<int:user_id>")
def show_user(user_id):
    """Show info on a single user."""

    user = Users.query.get_or_404(user_id)
    return render_template("detail.html", user=user)
