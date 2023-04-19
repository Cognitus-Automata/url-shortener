from flask import Flask, render_template, request,  redirect
from funcs import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/shorten', methods=['GET', 'POST'])
def shorten():
    if request.method == 'POST':
        url = request.form['url']
    
    return f"Your short URL is <a> 127.0.0.1:5000/{createShort(url)} </a>"

# TODO Split the url
# Get the short URL from the URL and redirect to the corresponding URL
@app.route('/<string:short>')
def redirectToURL(short):
    # Get the URL and split after the last /
    shortCode = request.url.split('/')[-1]
    return redirect("https://" + getURL(shortCode))



if __name__ == "__main__":
    createTable()

    app.run(debug=True)
