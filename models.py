"""Models for adopt."""
from flask_alchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):
    '''model for pet information'''
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    species = db.Column(db.Text, nullable = True)
    age = db.Column(db.Integer, nullable = True)
    notes = db.Column(db.Text, nullable = True)
    available = notes
    image_url = db.Column(db.Text, nullable = False)

    
def connect_db(app):

    db.app = app
    db.init_app(app)