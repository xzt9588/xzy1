#!/usr/bin/env python3
import json
import os

from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def user_index():
    path = '/home/shiyanlou/files'
    dirs = os.listdir(path)
    filename1 = path + '/' + dirs[0]
    filename2 = path + '/' + dirs[1]
    with open(filename1,'r') as f:
        data1 = json.load(f)
    with open(filename2,'r') as f:
        data2 = json.load(f)
    
    titles = {
        'title1': data1['title'],
        'title2': data2['title']
        }
    return render_template('index.html', titles=titles)
@app.route('/files/<filename>')
def file(filename):
    path = '/home/shiyanlou/files'
    dirs = os.listdir(path)
    filename1 = path + '/' + filename + '.json'
    i = 0
    j = 0
    while j < len(dirs):
        if dirs[j] == filename + '.json':
            i = i + 1
        j = j + 1
    if i == 0:
        data = {
                'filedata' : 'shiyanlou 404'
        }
        return render_template('index2.html',data=data)
    else:
        with open(filename1,'r') as f:
            data = json.load(f)
        data = {
                'filedata' : data
            }
        return render_template('index2.html', data=data)



