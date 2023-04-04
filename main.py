from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/rnd')
def rnd():
    return f"{random.randint(1, 100)}"

if __name__ == '__main__':
    app.run(debug=True)