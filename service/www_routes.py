"""Defines routes for the API calls to chat-queue"""

from flask import Blueprint, g, render_template

www = Blueprint("www", __name__)

@www.route("/")
def queue_listing():
  return render_template("homepage.html")