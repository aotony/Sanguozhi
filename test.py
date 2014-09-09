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

from flask import Flask, render_template
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/index")
def return_index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
	return render_template("user.html", name=name)





from flask import redirect
@app.route("/163")
def route163():
	return redirect("http://www.163.com")

if __name__ == "__main__":
    manager.run()
