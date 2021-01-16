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


@app.route("/add_review")
def add_review():
    return render_template("add_review.html")


@app.route("/contact_us")
def contact_us():
    return render_template("contact_us.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/logout")
def logout():
    return render_template("logout.html")


@app.route("/my_reviews")
def my_reviews():
    return render_template("my_reviews.html")


@app.route("/pints")
def pints():
    pints = mongo.db.pints.find()
    return render_template("pints.html", pints=pints)


@app.route("/pubs")
def pubs():
    pubs = mongo.db.pubs.find()
    return render_template("pubs.html", pubs=pubs)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # username validate
        is_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        
        if is_user:
            flash("Username taken!")
            return redirect(url_for('register'))

        reg_user = {
            "username": request.form.get("username").lower(),
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        mongo.db.users.insert_one(reg_user)

        session["active_user"] = request.form.get("username").lower()
        flash("You are now a pintbaby!")

    return render_template("register.html")


# Make sure to change the debug true statement below
# to debug false before project is submitted
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
