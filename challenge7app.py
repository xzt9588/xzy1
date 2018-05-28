#!/usr/bin/env python3
import datetime
from flask import render_template, Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
engine = create_engine('mysql://root@localhost/test')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/test'
db = SQLAlchemy(app)
Session = sessionmaker(bind=engine)
session = Session()
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    def __init__(self, a):
        self.name = a


class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    created_time = db.Column(db.DateTime)
    catagory_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category', backref='file')
    content = db.Column(db.Text)
    def __init__(self, a, b, c, d):
        self.title = a
        self.created_time = b
        self.catagory = c
        self.content = d


if __name__ == '__main__':
    db.create_all()
    java = Category('Java')
    python = Category('Python')
    file1 = File('Hello Java', datetime.datetime.utcnow(), java, 'File Content - Java is cool!')
    file2 = File('Hello Python', datetime.datetime.utcnow(), python, 'File Content - Python is cool!')
    db.session.add(java)
    db.session.add(python)
    db.session.add(file1)
    db.session.add(file2)
    db.session.commit()
    print(file1.title)
#@app.route('/files/<file_id>')
#def file(file_id):
#    pass
@app.route('/')
def index():
    file1 = (session.query(File).filter(File.id==1).one())
    file2 = (session.query(File).filter(File.id==2).one())
    titles = {
            'title1' : file1.title,
            'title2' : file2.title
            }
    return render_template('index.html',title = titles)
@app.route('/files/<file_id>')
def file(file_id):
    file1 = (session.query(File).filter(File.id==file_id).one())
    content = {
            'content' : file1.content
            }
    return render_template('index2.html',content = content)

