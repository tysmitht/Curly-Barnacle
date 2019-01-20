from flask import Flask, render_template, flash, redirect
from forms import RegistrationForm, LoginForm, HomeSearch, NewPost
from Userclasses import Subject, User
app = Flask(__name__)

old_data = open("data.txt", "w")

app.config["SECRET_KEY"] = "04217a5cba4ffa9a502cdde6f8b15b43"

listings = [
    {
        "student": "Tyler",
        "rating": "***",
        "subject": "CSE231",
        "pay": "$15/hr",
        "location": "library",
        "date": "4/14/1998"
    },
    {
        "student": "Jake ",
        "rating": "***",
        "subject": "CSE260",
        "pay": "$20/hr",
        "location": "Shaw",
        "date": "4/14/1998"
    },
    {
        "student": "Mo   ",
        "rating": "***",
        "subject": "CSE320",
        "pay": "$20/hr",
        "location": "Akers",
        "date": "4/14/1998"
    },
    {
        "student": "Billy",
        "rating": "***",
        "subject": "CSE335",
        "pay": "$35/hr",
        "location": "Anywhere",
        "date": "4/14/1998"
    },
]

users = [
    "Tyler",
    "Billy",
    "Mo",
    "Jake",
    "Nathan",
    "John"
]

@app.route('/')
@app.route("/home/<username>", methods = ["GET", "POST"])
@app.route('/home', methods = ["GET", "POST"])
def home(username=""):
    form = HomeSearch()
    print("we have reached this particular point")
    if form.validate_on_submit():
        print("This particular form was validated")
        return redirect("/results/"+username+"/"+form.search.data)
    return render_template('home.html', form = form, username = username)

@app.route("/results/<username>/<search>", methods = ["GET", "POST"])
@app.route('/results', methods = ["GET", "POST"])
def results(username="",search=""):
    found_users = [user for user in users if search in user]
    print("Hey guess what. it runs")
    for user in found_users:
        print(user)

    return render_template('results.html', username = username, searched_users = found_users)

num_users = 57

@app.route("/about/<username>")
@app.route('/about/')
def about(username=""):
    return render_template('about.html', username = username, users = num_users)

@app.route('/register/<username>', methods = ["GET", "POST"])
@app.route('/register', methods = ["GET", "POST"])
def register(username=""):
    form = RegistrationForm()
    if form.validate_on_submit():
        return redirect("/home/"+form.username.data)
    return render_template("register.html", form=form, username = username)

#@app.route('/login/<username>', methods = ["GET", "POST"])
@app.route('/login', methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            return redirect("/home/"+username)
    return render_template("login.html", form=form, username=username)

@app.route('/postings/<username>')
@app.route('/postings')
def postings(username=""):
    return render_template("postings.html", listings = listings, username=username)

@app.route('/profile/<username>')
def profile(username=""):
    return render_template("profile.html", username = username, data = data)

@app.route('/new/<username>', methods = ["GET", "POST"])
def new(username=""):
    form = NewPost()
    
    if form.validate_on_submit():
        new_listing = {
            "student": username,
            "rating": "***",
            "subject": form.subject.data,
            "pay": form.price.data,
            "location": form.location.data,
            "date": form.date.data,
            "additional comments": form.comments.data
        }
        listings.append(new_listing)
        return redirect("/home/"+username)
    return render_template("new.html", form = form, username = username)



if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='80',threaded=True)

old_data.close()