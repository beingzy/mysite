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
from mongoengine import *
import config
from models import *

app = Flask(__name__)
app.config.from_object('config.ProdConfig')

connect(app.config['MONGODB_SETTINGS']['DB'], 
	host=app.config['MONGODB_SETTINGS']['HOST'], 
	port=app.config['MONGODB_SETTINGS']['PORT'])

def get_blog_from_db():
	# Read blogs and sort by date from the most recent one
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
	return render_template('index.html')

## Blogs
@app.route('/blogs/')
def blogs():
	blogs = get_blog_from_db()
	return render_template('blogs.html', blogs=blogs)

## About Me
@app.route('/aboutme/')
def aboutme():
	resume = get_resume()
	return render_template('aboutme.html', resume=resume)

@app.errorhandler(404)
def error_page():
	return render_template('error.html'), 404

@app.route('/user/<username>')
def user(username):
	return "username is %s" % username


if __name__ == '__main__':
	#app.run(debug=True, host='0.0.0.0', port=8000)
	app.run(debug=app.config['DEBUG'], host=app.config['HOST'], port=app.config['PORT'])


