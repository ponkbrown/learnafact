import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class Fact(db.Model):
    __tablename__ = 'facts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    date = db.Column(db.DateTime)
    url = db.Column(db.String(256))
    image = db.Column(db.String(256))
    img_id = db.Column(db.String(64))
    reddit_id = db.Column(db.String(64))
    published = db.Column(db.Boolean)
    

    def __repr__(self):
        return '<Fact %r>' % self.name

    
