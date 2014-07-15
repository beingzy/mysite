## #################################################### ##
## Website structure:                                   ##
##   homepage(index.html) / blogs (blog.html) / resume  ##
##                                                      ##  
## Author: Yi Zhang                                     ##  
## Email:beingzy@gmail.com                              ##
## Date: Jul/14/2014 (update date)                       ##  
## #################################################### ##
import os
from flask import Flask, url_for, render_template, request, g, jsonify, abort, redirect, url_for, escape, session

app = Flask(__name__)
app.config.from_object(__name__)

# Load default config and overwrite config from an environment variable
app.config.update(dict(
	DEBUG=True,
	SECRET_KEY='\xe0|,Q\xbf\x9a\xd7;\x0c\x96\x84b<\xc3\x94\x00:\x0e)]C',
	USERNAME='admin',
	PASSWORD='default'
	))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)
      
## #############
## Website 
@app.route('/', methods=['GET', "POST"])
def index():
	# username = request.cookies.get('username')
	static_url = url_for('static', filename='images/favicon.ico')
	pwd_path   = os.getcwd()
	response = render_template('index.html', static_url=pwd_path)
	# response.set_cookie('username', 'the_username')
	return response

## Blogs
@app.route('/blogs/')
def blogs():
	return render_template('blogs.html', foo=42)

## Resume
@app.route('/aboutme/')
def aboutme():
	#return render_template('aboutme.html', foo=42)
	return redirect(url_for('error/'))

@app.route('/error/')
@app.errorhandler(404)
def error_page():
	resp = make_response(render_template('error.html'), 404)
	resp.headers['X-Somthing'] = "Error: 404"
	return resp

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=8000)


