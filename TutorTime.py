from flask import Flask, render_template, flash, redirect
from forms import RegistrationForm, LoginForm, HomeSearch
from Userclasses import Subject, User
app = Flask(__name__)

app.config["SECRET_KEY"] = "04217a5cba4ffa9a502cdde6f8b15b43"

listings = [
    {
        "student": "Tyler",
        "rating": "***",
        "subject": "CSE231",
        "pay": "$15/hr",
        "location": "library"
    },
    {
        "student": "Jake ",
        "rating": "***",
        "subject": "CSE260",
        "pay": "$20/hr",
        "location": "Shaw"
    },
    {
        "student": "Mo   ",
        "rating": "***",
        "subject": "CSE320",
        "pay": "$20/hr",
        "location": "Akers"
    },
    {
        "student": "Billy",
        "rating": "***",
        "subject": "CSE335",
        "pay": "$35/hr",
        "location": "Anywhere"
    },
]

@app.route('/')
@app.route("/home/<username>")
@app.route('/home', methods = ["GET", "POST"])
def home(username=""):
    form = HomeSearch()
    if form.validate_on_submit():
        return redirect("/results")
    return render_template('home.html', form = form, username = username)

num_users = 57

@app.route("/about/<username>")
@app.route('/about/')
def about(username=""):
    return render_template('about.html', username = username, users = num_users)

@app.route('/register/<username>', methods = ["GET", "POST"])
@app.route('/register', methods = ["GET", "POST"])
def register(username=""):
    form = RegistrationForm()
    # new_user = User(form.username.data, form.email.data, form.password.data)
    # username_data = form.username.data
    if form.validate_on_submit():
        return redirect("/home/"+form.username.data)
        # form.password.data
    
    return render_template("register.html", form=form, username = username)

@app.route('/login/<username>', methods = ["GET", "POST"])
@app.route('/login', methods = ["GET", "POST"])
def login(username=""):
    form = LoginForm()
    # if form.validate_on_submit():
    #     if form.email.data == "admin@blog.com" and form.password.data == "password":
    #         pass
    return render_template("login.html", form=form, username=username)

@app.route('/postings')
def postings():
    return render_template("postings.html", listings = listings)


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='80',threaded=True)

