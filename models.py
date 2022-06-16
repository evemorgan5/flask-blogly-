"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = 'https://icon-library.com/images/default-profile-icon/default-profile-icon-24.jpg'

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):
    """User."""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(50),
                     nullable=False,
                     unique=False)
    last_name = db.Column(db.String(50),
                     nullable=False,
                     unique=False)

    img_url = db.Column(db.String,
                    nullable=False,
                    default=DEFAULT_IMAGE_URL)


    # need to make sure first & last name are unique when joined
    # unique(db.first_name, db.last_name)



    # def greet(self):
    #     """Greet using name."""

    #     return f"I'm {self.name} the {self.species or 'thing'}"

    # def make_edits(self, edited_first_name, edited_last_name, edited_img_url):
    #     """Nom nom nom."""
    #     self.first_name = edited_first_name
    #     self.last_name = edited_last_name
    #     self.img_url = edited_img_url
    #     user = User.query.get(user_id)




    # @classmethod
    # def get_by_species(cls, species):
    #     """Get all pets matching that species."""

    #     return cls.query.filter_by(species=species).all()



# class Post(db.Model):
#     """Post."""

#     __tablename__ = "post"

#     id = db.Column(db.Integer,
#                    primary_key=True,
#                    autoincrement=True)
#     title = db.Column(db.String(50),
#                      nullable=False,
#                      unique=False)
#     content = db.Column(db.String(50),
#                      nullable=False,
#                      unique=False)

#     created_at = db.Column(db.datetime.datetime.now())

#     user_id = db.Column(db.ForeignKey('users.id'))

