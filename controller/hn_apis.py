from flask import Blueprint


hn_apis = Blueprint("hn_apis", __name__)


@hn_apis.route("/")
def hello_jobs():
    return "Welcome to Hacker News job insights"
