import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash 
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/pubs")
def pubs():
    pubs = mongo.db.pubs.find()
    return render_template("pubs.html", pubs=pubs)


@app.route("/pints")
def pints():
    pints = mongo.db.pints.find()
    return render_template("pints.html", pints=pints)


@app.route("/add_review")
def add_review():
    return render_template("add_review.html")


@app.route("/register")
def register():
    return render_template("register.html", methods=["GET", "POST"])


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/contact_us")
def contact_us():
    return render_template("contact_us.html")


@app.route("/logout")
def logout():
    return render_template("logout.html")


@app.route("/my_reviews")
def my_reviews():
    return render_template("my_reviews.html")


# Make sure to change the debug true statement below
# to debug false before project is submitted
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
