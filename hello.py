from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError
import re

app = Flask( __name__ ) 
app.config['SECRET_KEY'] = 'hard to guess string'

def validate_uoft_email(form, field):
    if not re.search('utoronto', field.data):
        raise ValidationError("Please Use a UofT Email")

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your UofT email?',  
            validators=[DataRequired(), 
                        Email(message="Please enter a valid email", check_deliverability=True),
                        validate_uoft_email])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST']) 
def index():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash("Looks like you have changed your name!")

        old_email = session.get('email')
        if old_email is not None and old_email != form.email.data:
            flash("Looks like you have changed your email!")
            
        session['name'] = form.name.data
        session['email'] = form.email.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'), email=session.get('email'))

@app.route('/user/<name>') 
def user(name): 
    return render_template('user.html', name=name)

bootstrap = Bootstrap(app)