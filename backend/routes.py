from main import app
from flask import render_template


# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getshort')
def shortener():
    return render_template('getShort.html')
