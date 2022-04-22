from flask import render_template, session
from flask_app import app

@app.route('/')
def home():
    if 'user_id' in session:
        session.pop('user_id')
    return render_template('home.html')