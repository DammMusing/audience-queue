"""Defines routes for the API calls to chat-queue"""

from flask import Blueprint, render_template

www = Blueprint("www", __name__)

@www.route("/")
def homepage():
  """Renders the HTML for the landing page."""
  return render_template("homepage.html")
