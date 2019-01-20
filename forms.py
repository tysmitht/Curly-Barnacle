from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField("Username",
        validators=[DataRequired(), Length(min=2, max=20)])

    email = StringField("Email", 
        validators=[DataRequired(), Email()])

    password = PasswordField('Password',
        validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password',
        validators = [DataRequired(), EqualTo("password")])

    submit = SubmitField("Sign Up")

class LoginForm(FlaskForm):
    email = StringField("Email", 
        validators=[DataRequired(), Email()])

    password = PasswordField('Password',
        validators = [DataRequired()])

    remember = BooleanField("Remember Me")

    submit = SubmitField("Login")

class HomeSearch(FlaskForm):
    search = StringField("Search", 
        validators=[DataRequired()])
    submit = SubmitField("Search")

class NewPost(FlaskForm):
    subject = StringField("subject",
        validators=[DataRequired()])

    price = StringField("price",
        validators=[DataRequired()])

    location = StringField("location",
        validators=[DataRequired()])
        
    date = DateField("date",
        validators=[DataRequired()])

    comments = StringField("comments")

    submit = SubmitField("Create Post")

class JobSelection(FlaskForm):
    choice = StringFiezld("choice",
        validators=[DataRequired()])

