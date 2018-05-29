#!/usr/bin/env python3
import datetime
from flask import render_template, Flask
from flask_sqlalchemy import SQLAlchemy
from pymongo import MongoClient
client = MongoClient('127.0.0.1',27017)
mgdb = client.shiyanlou

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

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
        self.category = c
        self.content = d
    def add_tag(self,tag_name):
        doc = mgdb.tags.find_one({'id': self.id})
        print(doc)
        if doc:
            tags = doc['tags']
            if tag_name not in tags:
                tags.append(tag_name)
                mgdb.tags.update_one({'id': self.id}, {'$set': {'tags': tags}})
        else:
            mgdb.tags.insert_one({'id': self.id, 'tags': [tag_name]})

    def remove_tag(self, tag_name):
        doc = mgdb.tags.find_onw({'id': self.id})
        if doc:
            tags = dov['tags']
            if tag_name in tags:
                tags.remove(tag_name)
        pass
    

    @property
    def tags(self):
        return mgdb.tags.find_one({'id': self.id})['tags']


@app.route('/')
def index():
    files = File.query.all()
    print(files)
    return render_template('index.html', files=files)

@app.route('/files/<file_id>')
def file(file_id):
    f = File.query.get_or_404(file_id)
    return render_template('file.html', f=f)

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
    file1.add_tag('tech')
    file1.add_tag('java')
    file1.add_tag('linux')
    file2.add_tag('tech')
    file2.add_tag('python')
