from flask import Flask, render_template, flash, redirect
from forms import RegistrationForm, LoginForm, HomeSearch, NewPost
from Userclasses import Subject, User
import pickle
import os
app = Flask(__name__)

app.config["SECRET_KEY"] = "04217a5cba4ffa9a502cdde6f8b15b43"

#print(os.path.exists("user.pickle"))

def job_pickle(jobs_l):
    pickle_out = open("user.pickle","wb")
    pickle.dump(listings, pickle_out)
    pickle_out.close()

def people_pickle(people_l):
    people_out = open("people.pickle","wb")
    pickle.dump(Users, pickle_out)
    people_out.close()

if(os.path.exists("people.pickle")==False):
    Users = [] #create that list 
else:
    people_in = open("people.pickle","rb")
    Users = pickle.load(people_in)
    people_in.close()

if(os.path.exists("user.pickle")==False):
    listings = [] #create that list 
else:
    list_in = open("user.pickle","rb")
    listings = pickle.load(list_in)
    list_in.close()

"""
data = {
    "name": "tyler",
    "tutor_rating": "*****",
    "student_rating": "****",
    "qualifications": [
        "CSE231", "CSE232", "CSE260", "MTH132", "MTH234"
    ],
    "email": "smit2660@msu.edu",
    "location": "Charlotte"
}
"""

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
        new_user = [form.username.data, form.email.data, form.password.data, "MSU", [], "**", "*****"]
        Users.append(new_user)
        return redirect("/home/"+form.username.data)
    return render_template("register.html", form=form, username = username)

#@app.route('/login/<username>', methods = ["GET", "POST"])
@app.route('/login', methods = ["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.username.data == "admin@blog.com" and form.password.data == "password":
            return redirect("/home/"+form.username.data)
    return render_template("login.html", form=form)

@app.route('/postings/<username>')
@app.route('/postings')
def postings(username=""):


    """
    LISTING NEEDS TO BE LIST OF DICTIONARIES THAT REPRESENT JOB POSTINGS
    """

    return render_template("postings.html", listings = listings, username=username)

@app.route('/profile/<username>/<profilename>')
def profile(username="", profilename=""):

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

        """
        LISTINGS SHOULD BE
        """
        listings.append(new_listing)
        #pickle function
        job_pickle(listings)
        return redirect("/home/"+username)
    return render_template("new.html", form = form, username = username)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port='80',threaded=True)
