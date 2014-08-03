#from temp_config import *
# import app
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!@flaskapp.test_site"

if __name__ == "__main__":
    app.run()