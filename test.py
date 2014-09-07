#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      AOTONY
#
# Created:     03/09/2014
# Copyright:   (c) AOTONY 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from flask import Flask
from flask.ext.script import Manager

app = Flask(__name__)

manager = Manager(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/user/<name>")
def user(name):
	return "<h1>Hello %s!</h1>" % name

from flask import redirect
@app.route("/163")
def route163():
	return redirect("http://www.163.com")

if __name__ == "__main__":
    manager.run()
