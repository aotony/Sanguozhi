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

from flask import Flask, render_template, url_for
from flask.ext.script import Manager
from flask.ext.bootstrap import Bootstrap

app = Flask(__name__)

manager = Manager(app)
bootstrap = Bootstrap(app)

# @app.route("/")
# def hello():
    # return "Hello World!"

@app.route("/")
def return_index():
    return render_template("index.html")

@app.route("/user/<name>")
def user(name):
	return render_template("user.html", name=name)


@app.route("/sanguozhi/")
def return_sanguozhi_index():
	return render_template("sanguozhi_index.html")

@app.route("/sanguozhi/<file_name>")
def return_sanguozhi_content(file_name):
	if type(int(file_name)) == int :
		return render_template("sanguozhi_" + file_name + ".html")


@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"), 404

@app.errorhandler(500)
def internal_server_error(e):
	return render_template("500.html"), 500



from flask import redirect
@app.route("/163")
def route163():
	return redirect("http://www.163.com")

if __name__ == "__main__":
    manager.run()
