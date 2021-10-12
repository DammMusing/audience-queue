"""Defines routes for the API calls to chat-queue"""

from flask import Blueprint, g, render_template

from . import database as db


api = Blueprint("api", __name__, url_prefix="/<channel_id>")

@api.url_value_preprocessor
def extract_queue_id(unused_endpoint, values):
  """Preprocessor for the routes that extracts the channel_id from URL.

  Args:
    unused_endpoint: route, not needed
    values: (dict) vars extracted from the route's URL.
  """
  g.queue_id = values.pop("channel_id", None)
  # Validate existence of queue_id.
  if not db.queue_exists(g.queue_id):
    g.queue_id = None


@api.route("/")
def queue_listing():
  """Returns a plaintext list of the players next up in the queue.

  The entire list is given if it can fit in a Twitch message, or the list is
  truncated if too long.
  """
  return render_template("queue_listing")

@api.route("/info")
def queue_info():
  """Returns an informative phrase for the queue, as a custom description."""
  return render_template("queue_info")

@api.route("/join", methods=["GET", "POST"])
def join_queue():
  """Add a user to the queue."""
  # To avoid proxies from caching, get joined user from URL params not path.
  return render_template("joined")

@api.route("/leave", method=["GET", "POST"])
def leave_queue():
  """Remove a user from the queue."""
  return render_template("leaving_success")

@api.route("/position/user/<string:username>")
def position_user(username):
  """Returns the position of the indicated user."""
  return render_template(
      "position_user",
      username=username)

@api.route("/position/at/<int:at>")
def position_at(at_pos):
  """Returns the user at the requested position."""
  username = db.get_user_at_position(g.queue_id, at_pos)
  return render_template(
      "position_at",
      at_pos=at_pos,
      username=username)

@api.route("/position/next/<int:count>")
def position_head(count):
  """Returns the next `count` users in the queue, up to what fits in chat."""
  users = db.ViewerQueues.get_next_n(g.queue_id, count)
  return render_template("position_head", users=users)
