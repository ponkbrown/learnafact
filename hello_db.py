import os
from flask_script import Manager
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
manager = Manager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

db = SQLAlchemy(app)

class Fact(db.Model):
    __tablename__ = 'facts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    fact = db.Column(db.String(254))
    fact_img = db.Column(db.String(256))
    url = db.Column(db.String(256))
    reddit_id = db.Column(db.String(64))
    img_id = db.Column(db.String(64))
    date = db.Column(db.DateTime)
    published = db.Column(db.Boolean)
    

    def __repr__(self):
        return '<Fact %r>' % self.name

    
if __name__ == '__main__':
    manager.run()
