"""Models for adopt."""
from flask_alchemy import SQLAlchemy

GENERIC_IMAGE = "https://mylostpetalert.com/wp-content/themes/mlpa-child/images/nophoto.gif"

db = SQLAlchemy()

class Pet(db.Model):
    '''model for pet information'''
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = False)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable = False, default = True)
    image_url = db.Column(db.Text, nullable = False, default = True)

    def image_url(self):
        """Return image for pet -- given or generic."""

        return self.image_url or GENERIC_IMAGE
    
def connect_db(app):

    db.app = app
    db.init_app(app)