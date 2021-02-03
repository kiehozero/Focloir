import os
from flask import (
    Flask, flash, render_template, redirect, request, session, url_for)
from flask_pymongo import PyMongo
from werkzeug.security import (
    generate_password_hash, check_password_hash)
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


@app.route("/add_pub", methods=["GET", "POST"])
def add_pub():
    countries = mongo.db.countries.find().sort("name")
    if request.method == "POST":
        new_pub = {
            "pname": request.form.get("pname"),
            "loc": request.form.get("loc"),
            "city": request.form.get("city"),
            "state": request.form.get("state"),
            "country": request.form.get("country")
        }

        mongo.db.pubs.insert_one(new_pub)
        flash("{} successfully added".format(request.form.get("pname")))
        # need a modal to display above
        # automatically sends user to review page
        return redirect(url_for('add_review'))

    # this is the else statement for the request method, so the GET request
    return render_template("add_pub.html", countries=countries)


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    pubs = mongo.db.pubs.find().sort("pname")
    pints = mongo.db.pints.find().sort("dname")
    if request.method == "POST":
        new_review = {
            "pub": request.form.get("pub"),
            "pint": request.form.get("pint"),
            "visit": request.form.get("visit"),
            "prating": request.form.get("prating"),
            "drating": request.form.get("drating"),
            "arating": request.form.get("arating"),
            "price": request.form.get("price"),
            "review": request.form.get("review"),
            "author": session["user"]
        }

        mongo.db.reviews.insert_one(new_review)
        flash("Review added, add another?")
        # needs modal to display flash above, plus
        # buttons saying "Add another review" and
        # a second option that takes you to the
        # my_reviews area

    return render_template("add_review.html", pubs=pubs, pints=pints)


@app.route("/contact_us")
def contact_us():
    return render_template("contact_us.html")


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    # needs a confirm message here, if yes then
    # below, if no redirect to my_reviews
    mongo.db.reviews.remove(
        {"_id": ObjectId(review_id)}
    )
    flash("Review deleted")
    return redirect(url_for(
        'my_reviews', username=session["user"]))


@app.route("/edit_profile/<username>", methods=["GET", "POST"])
def edit_profile(username):
    if request.method == "POST":
        # need to work out how to change password"
        user_id = mongo.db.users.find_one({"username": session["user"]})["_id"]
        edited_profile = {
            "username": request.form.get("username"),
            "first_name": request.form.get("first_name"),
            "last_name": request.form.get("last_name"),
            "email": request.form.get("email")
            # requires a way of working out how
            # to change password or ignore field
        }
        mongo.db.users.update(
            {"_id": user_id}, edited_profile)

        flash("Profile updated")
        return redirect(url_for(
            'my_reviews', username=session["user"]))

    # probably a better way of doing both, rather
    # than duplicating requests
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    user_id = mongo.db.users.find_one(
        {"username": session["user"]})["_id"]
    return render_template(
        "edit_profile.html", username=username, user=user, user_id=user_id)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        edited_review = {
            "pub": request.form.get("pub"),
            "pint": request.form.get("pint"),
            "visit": request.form.get("visit"),
            "prating": request.form.get("prating"),
            "drating": request.form.get("drating"),
            "arating": request.form.get("arating"),
            "price": request.form.get("price"),
            "review": request.form.get("review"),
            "author": session["user"]
        }
        mongo.db.reviews.update(
            {"_id": ObjectId(review_id)}, edited_review)
        # needs to be able to display flash
        flash("Review amended")
        return redirect(url_for(
            'my_reviews', username=session["user"]))

    # else method (GET)
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    pints = mongo.db.pints.find().sort("dname")
    pubs = mongo.db.pubs.find().sort("pname")
    return render_template(
        "edit_review.html", review=review, pints=pints, pubs=pubs)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        is_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if is_user:
            if check_password_hash(
                is_user["password"], request.form.get(
                    "password")):
                    session["user"] = request.form.get(
                        "username").lower()
                    flash("Welcome, {}".format(request.form.get("username")))
                    # need a modal or heading to display
                    return redirect(url_for(
                        'my_reviews', username=session["user"]))

            else:
                flash("Username and password combination is incorrect")
                # need a modal to display
                return redirect(url_for('login'))

        else:
            flash("Username and password combination is incorrect")
            # need a modal to display
            return redirect(url_for('login'))

    # this is the else statement for the request method, so the GET request
    return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    # needs a modal to display this on the page
    return redirect(url_for('login'))


@app.route("/my_reviews/<username>", methods=["GET", "POST"])
def my_reviews(username):
    # only returns username from MongoDB users collection
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    # returns reviews by active user, ordered by most recent visit first
    reviews = mongo.db.reviews.find(
        {"author": session["user"]}).sort("visit", -1)

    # if statement ensures that you can't add any username to the
    # profile url string to access their profile page
    if session["user"]:
        return render_template(
            "my_reviews.html", username=username, reviews=reviews)
    # need an else statement here to catch any requests where
    # someone who isn't logged in can't type a profile address
    # access it. At the moment this just loads of a Jinja error

    return redirect(url_for('login'))


@app.route("/pints")
def pints():
    pints = mongo.db.pints.find()
    return render_template("pints.html", pints=pints)


@app.route("/pubs")
def pubs():
    pubs = mongo.db.pubs.find().sort("pname")
    return render_template("pubs.html", pubs=pubs)


@app.route("/view_pub/<pub_id>")
def view_pub(pub_id):
    pub_id = mongo.db.pubs.find_one(
        {"_id": ObjectId(pub_id)}
    )
    # minus one sorts reviews by most recent first
    reviews = mongo.db.reviews.find().sort("visit", -1)
    return render_template(
        "view_pub.html", pub_id=pub_id, reviews=reviews)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # username validate
        is_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if is_user:
            flash("Username taken!")
            # add a div to display this flash
            return redirect(url_for('register'))

        reg_user = {
            # do these all need to be converted to lower case?
            "username": request.form.get("username").lower(),
            "first_name": request.form.get("first_name").lower(),
            "last_name": request.form.get("last_name").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }

        mongo.db.users.insert_one(reg_user)

        session["user"] = request.form.get("username").lower()
        # successful log-in re-directs to their new blank profile page
        return redirect(url_for('my_reviews', username=session["user"]))

    # change re-direct destination
    return render_template("register.html")


@app.route("/search_pubs", methods=["GET", "POST"])
def search_pubs():
    query = request.form.get("search")
    pubs = list(mongo.db.pubs.find({"$text": {"$search": query}}).sort("pname"))
    return render_template("pubs.html", pubs=pubs)


# Make sure to change the debug true statement below
# to debug false before project is submitted
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
