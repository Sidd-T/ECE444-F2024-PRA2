from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime, timezone

app = Flask( __name__ ) 

@app.route('/') 
def index(): 
    return render_template('index.html', current_time=datetime.now(timezone.utc))

@app.route('/user/<name>') 
def user(name): 
    return render_template('user.html', name=name)

bootstrap = Bootstrap(app)
moment = Moment(app)