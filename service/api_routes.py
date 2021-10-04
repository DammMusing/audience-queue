"""Defines routes for the API calls to chat-queue"""

from flask import Blueprint, g, render_template

api = Blueprint("api", __name__, url_prefix="/<channel_id>")

@api.url_value_preprocessor
def extract_queue_id(unused_endpoint, values):
  g.queue_id = values.pop("channel_id", None)
  # TODO validate existence of queue_id
  # g.queue = db.get_channel_queue(g.queue_id)


@api.route("/")
def queue_listing():
  return render_template("queue_listing")


@api.route("/info")
def queue_info():
  return render_template("queue_info")


@api.route("/join")
def join_queue():
  return render_template("joined")


@api.route("/leave")
def leave_queue():
  return render_template("leaving")


@api.route("/position/user/<string:username>")
def position_user(username):
  return render_template("position_user")


@api.route("/position/at/<int:at>")
def position_at(at_pos):
  # TODO lookup position entry for g.queue_id
  return render_template(
    "position_at",
    at_pos=at_pos,
    name="stubname")  # ViewerQueues.get_at(g.queue_id, at_pos)


@api.route("/position/next/<int:count>")
def position_head(count):
  return render_template("position_head")
