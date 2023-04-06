from flask import Flask, render_template
from funcs import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/rnd')
def rnd():
    return f"Your short URL is {createShort('https://www.google.com')}"

if __name__ == "__main__":
    createTable()

    app.run(debug=True)
