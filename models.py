from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate 
db = SQLAlchemy()
database_name = "movies"
database_path = "postgresql://{}:{}@{}/{}".format('postgres','123','localhost:5432',database_name)

def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.urandom(32)
    db.app = app
    db.init_app(app)
    db.create_all()

class Movies(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String,unique=True, nullable=False)
    type=db.Column(db.String, nullable=False)
    image_link = db.Column(db.String(500), nullable=False)
    link=db.Column(db.String(120), nullable=False)
    release_date=db.Column(db.DateTime, nullable=False)
    #define relationship one movie can has many actors
    main_actor = db.relationship("Actors", backref="movies")
    def __init__(self, title, type, image_link, release_date,link):
        self.title = title
        self.type = type
        self.image_link= image_link
        self.release_date = release_date
        self.link=link
    def format(self):
        return {
            "id": self.id,
            "title": self.title,
            "type": self.type,
            "release_date": self.release_date.strftime("%B %d, %Y"),
            "main_actor": [actor.name for actor in self.main_actor],
            "image_link":self.image_link,
            "link":self.link,
        }
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()
class Actors(db.Model):
    __tablename__ = "actors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_link = db.Column(db.String(500), nullable=False)
    gender = db.Column(db.String(10))
    movie_id = db.Column(db.Integer, db.ForeignKey("movies.id"))
    def __init__(self, name, image_link, gender,movie_id):
        self.name = name
        self.image_link= image_link
        self.gender = gender
        self.movie_id=movie_id
    def format(self):
        return {
            "id": self.id,
            "name": self.name,
            "image_link ":self.image_link ,
            "gender": self.gender,
            "movies": self.movie_id.title,
        }
