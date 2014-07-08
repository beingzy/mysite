## #################################################### ##
## Website structure:                                   ##
##   homepage(index.html) / blogs (blog.html) / resume  ##
##                                                      ##  
## Author: Yi Zhang                                     ##  
## Email:beingzy@gmail.com                              ##
## Date: Jul/7/2014 (create date)                       ##  
## #################################################### ##
from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from flask import jsonify
## bootstrap
from flask.ext.bootstrap import Bootstrap
# app = Flask(__name__)
bootstrap = Bootstrap(__name__)
      
## #############
## Website 
@app.route('/')
def index():
	return render_template('index.html', foo=42)

## Blogs
@app.route('/blogs')
def blogs():
	return render_template('blogs.html', foo=42)

## Resume
@app.route('/aboutme')
def resume():
	return render_template('aboutme.html', foo=42)

if __name__ == '__main__':
	## to envure when the file is excuted directly
	app.run(debug=True)