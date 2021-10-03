import flask

from . import app

@app.route("/")
def homepage():
  return flask.render_template("homepage.html")