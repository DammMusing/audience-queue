import flask

from . import app

@app.route("/")
def homepage():
  return flask.render_template("homepage.html")

@app.route("/list")
def listing():
  return flask.render_template("queue_listing")

@app.route("/info")
def queue_info():
  return flask.render_template("queue_info")

@app.route("/join")
def join_queue():
  return flask.render_template("joined")

@app.route("/leave")
def leave_queue():
  return flask.render_template("leaving")

@app.route("/position/user/<string:username>")
def position_user(username):
  return flask.render_template("position_user")

@app.route("/position/at/<int:at>")
def position_at(at):
  return flask.render_template("position_at")

@app.route("/position/next/<int:count>")
def position_head(count):
  return flask.render_template("position_head")