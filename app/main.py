## ##################################################### ##
## Website structure:                                    ##
##   homepage(index.html) / blogs (blog.html) / aboutme  ##
##                                                       ##  
## Author: Yi Zhang                                      ##  
## Email: beingzy@gmail.com                              ##
## Date: Jul/14/2014 (update date)                       ##  
## ##################################################### ##
import os
import datetime
from flask import Flask, url_for, render_template, request, g, jsonify, abort, redirect, url_for, escape, session
from flask.ext.mongoengine import MongoEngine
from mongoengine import *
# import models

app = Flask(__name__)
#app.config.from_pyfile('the-config.cfg')
app.config.update(dict(
	DEBUG=True,
	SECRET_KEY='\xe0|,Q\xbf\x9a\xd7;\x0c\x96\x84b<\xc3\x94\x00:\x0e)]C',
	USERNAME='admin',
	PASSWORD='default'
	))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# MongoDB Connection
connect('beingzy_site', host='54.88.134.182', port=27017)
# db = MongoEngine(__name__)

class Blog(Document):
	title   = StringField(max_length=256, required=True)
	created = DateTimeField(default=datetime.datetime.now,   required=True)
	updated = DateTimeField(default=datetime.datetime.now,   required=True)
	author  = StringField(max_length=128, default="beingzy", required=True)
	body    = StringField(required=True)
	tags    = ListField(StringField(), required=False)

class Resume(Document):
	first_name  = StringField(max_length=128, required=True)
	last_name   = StringField(max_length=128, required=True)
	middle_name = StringField(max_length=128, required=False)
	phone       = StringField(max_length=128, required=True)
	email       = EmailField(required=True)
	version     = FloatField(required=True)

class Moto(Document):
	created = DateTimeField(default=datetime.datetime.now,   required=True)
	body    = StringField(max_length=1000, required=True)
	tags    = ListField(StringField(), required=True) 

def get_blog_from_db():
	blogs = Blog.objects.order_by("-created")
	return blogs

def get_resume(version=None):
	if version is None:
		resumes = Resume.objects
		resume  = resumes[len(resumes) - 1]
	else:
		resume  = Resume.objects(version=version)
	return resume

## Website 
@app.route('/', methods=['GET', "POST"])
def index():
	# username = request.cookies.get('username')
	return render_template('index.html')
	# response.set_cookie('username', 'the_username')

## Blogs
@app.route('/blogs/')
def blogs():
	blogs = get_blog_from_db()
	return render_template('blogs.html', blogs=blogs)

## About Me
@app.route('/aboutme/')
def aboutme():
	#return render_template('aboutme.html', foo=42)
	resume = get_resume()
	return render_template('aboutme.html', resume=resume)

@app.errorhandler(404)
def error_page():
	return render_template('error.html'), 404


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8000)


