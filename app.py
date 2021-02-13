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
    if session.user:
        if request.method == "POST":
            new_pub = {
                "pname": request.form.get("pname"),
                "loc": request.form.get("loc"),
                "city": request.form.get("city"),
                "state": request.form.get("state"),
                "country": request.form.get("country"),
                "photo": request.form.get("photo")
            }

            mongo.db.pubs.insert_one(new_pub)
            flash("{} successfully added".format(request.form.get("pname")))
            # need a modal to display above
            # automatically sends user to review page
            # needs to redirect to review page pre-filled with that pub
            return redirect(url_for('add_review'))

        # GET method
        return render_template("add_pub.html", countries=countries)

    # below not currently functioning
    else:
        return redirect(url_for('register'))


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
        flash("Review added")
        # redirect to specific pub page

    # GET method
    return render_template("add_review.html", pubs=pubs, pints=pints)


@app.route("/add_review_of/<pub_id>", methods=["GET", "POST"])
def add_review_of(pub_id):
    pub_id = mongo.db.pubs.find_one(
        {"_id": ObjectId(pub_id)})
    if request.method == "POST":
        new_review = {
            "pub": request.form.get("pub"),
            "visit": request.form.get("visit"),
            "prating": request.form.get("prating"),
            "drating": request.form.get("drating"),
            "arating": request.form.get("arating"),
            "price": request.form.get("price"),
            "review": request.form.get("review"),
            "author": session["user"]
        }

        mongo.db.reviews.insert_one(new_review)
        flash("Review added")
        return redirect(url_for('pubs'))
        # needs a redirect back to specific pub page

    # GET method
    return render_template(
        "add_review_of.html", pub_id=pub_id)


@app.route("/contact_us")
def contact_us():
    return render_template("contact_us.html")


@app.route("/delete_pub_admin/<pub_id>")
def delete_pub_admin(pub_id):
    # admin only
    # needs a confirm message here, if yes then
    # below, if no redirect to my_reviews
    mongo.db.pubs.remove(
        {"_id": ObjectId(pub_id)}
    )
    flash("Pub deleted")
    return redirect(url_for('pubs'))


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


@app.route("/delete_review_admin/<review_id>")
def delete_review_admin(review_id):
    # needs a confirm message here, if yes then
    # below, if no redirect to my_reviews
    # same functionality as above, just re-directs to
    # the pub index rather than the user profile
    mongo.db.reviews.remove(
        {"_id": ObjectId(review_id)}
    )
    flash("Review deleted")
    return redirect(url_for('pubs'))


@app.route("/delete_user/<user_id>")
def delete_user(user_id):
    flash("Are you sure you want to remove {{ user.username }}'s account?")
    mongo.db.users.remove(
        {"_id": ObjectId(user_id)}
    )
    # need to display flash messages
    flash("User Deleted")
    return redirect(url_for('users'))


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

    # GET method
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    user = mongo.db.users.find_one(
        {"username": session["user"]})
    user_id = mongo.db.users.find_one(
        {"username": session["user"]})["_id"]
    return render_template(
        "edit_profile.html", username=username, user=user, user_id=user_id)


@app.route("/edit_pub/<pub_id>", methods=["GET", "POST"])
def edit_pub(pub_id):
    if request.method == "POST":
        edited_pub = {
            "pname": request.form.get("pname"),
            "loc": request.form.get("loc"),
            "city": request.form.get("city"),
            "state": request.form.get("state"),
            "country": request.form.get("country"),
            "photo": request.form.get("photo")
        }
        mongo.db.pubs.update(
            {"_id": ObjectId(pub_id)}, edited_pub)
        # needs to be able to display flash
        flash("Review amended")
        return redirect(url_for('view_pub', pub_id=pub_id))

    # GET method
    pub = mongo.db.pubs.find_one({"_id": ObjectId(pub_id)})
    countries = mongo.db.countries.find().sort("name")
    return render_template(
        "edit_pub.html", pub=pub, countries=countries)


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

    # GET method
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    pints = mongo.db.pints.find().sort("dname")
    pubs = mongo.db.pubs.find().sort("pname")
    return render_template(
        "edit_review.html", review=review, pints=pints, pubs=pubs)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #username validation
        is_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if is_user:
            # password match
            if check_password_hash(
                is_user["password"], request.form.get(
                    "password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                    'my_reviews', username=session["user"]))

            else:
                flash("Username and password combination is incorrect")
                return redirect(url_for('login'))

        else:
            flash("Username and password combination is incorrect")
            return redirect(url_for('login'))

    # GET method
    return render_template("login.html")


@app.route("/logout")
def logout():
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for('login'))


@app.route("/moderate_review/<review_id>", methods=["GET", "POST"])
def moderate_review(review_id):
    # admin only function to moderate content, e.g. offensive or legally
    # questionable statements
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
            "author": request.form.get("author")
        }
        mongo.db.reviews.update(
            {"_id": ObjectId(review_id)}, edited_review)
        # needs to be able to display flash
        flash("Review amended")
        return redirect(url_for('pubs'))

    # GET method
    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    pints = mongo.db.pints.find().sort("dname")
    pubs = mongo.db.pubs.find().sort("pname")
    return render_template(
        "moderate_review.html", review=review, pints=pints, pubs=pubs)


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


@app.route("/pubs")
def pubs():
    # Converting below to a list allows the if loop in the template
    # page to work properly when a user searches for somewhere
    pubs = list(mongo.db.pubs.find().sort("pname"))
    return render_template("pubs.html", pubs=pubs)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # username validation
        is_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})
        if is_user:
            flash("Username taken!")
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

    # GET method
    return render_template("register.html")


@app.route("/search_pubs", methods=["GET", "POST"])
def search_pubs():
    query = request.form.get("search")
    pubs = list(
        mongo.db.pubs.find({"$text": {"$search": query}}).sort("pname"))
    return render_template("pubs.html", pubs=pubs)


@app.route("/users")
# admin only
def users():
    users = list(mongo.db.users.find().sort("username"))
    return render_template("users.html", users=users)


@app.route("/view_pub/<pub_id>")
def view_pub(pub_id):
    pub_id = mongo.db.pubs.find_one(
        {"_id": ObjectId(pub_id)}
    )
    # sorts reviews by most recent first
    reviews = mongo.db.reviews.find().sort("visit", -1)
    return render_template(
        "view_pub.html", pub_id=pub_id, reviews=reviews)


# Make sure to change the debug true statement below
# to debug false before project is submitted
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
