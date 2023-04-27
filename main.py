from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import string
import random


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Urls(db.Model):
    
    id_ = db.Column("id_", db.Integer, primary_key=True)
    url = db.Column("url", db.String())
    short = db.Column("short", db.String(4))
    
    def __init__(self, url, short):
        self.url = url
        self.short = short
        
@app.before_first_request
def create_table():
    db.create_all()
    print("Table created!")
    
    
def create_short_url():
    characters = string.ascii_lowercase + string.ascii_uppercase
    while True:
      rand_chars = random.choices(characters, k=4)
      rand_chars = "".join(rand_chars)
      short_url = Urls.query.flter_by(short=rand_chars).first()
      if not short_url:
          return rand_chars

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/shorten', methods=["GET", "POST"])
def url_shorten():
    if request.method == "POST":
        url_recieved = request.form["url"]
        # checking if url already exists in database
        url_found = Urls.query.filter_by(url=url_recieved).first()
        if url_found:
            #if found, return the short url
            return f" Your short URL is <a> 127.0.0.1:5000/{url_found.short} <a>"
        else:
            #else,we crate a new short url and return it to the user
            short_url = create_short_url()
            print(short_url)
            new_url = Urls(url_recieved, short_url)
            db.session.add(new_url)
            db.session.commit()
            return f" Your short URL is <a> 127.0.0.1:5000/{short_url} <a>"
    
# After shorting the url, we redirect to the correspoding one
@app.route('/<short_url>')
def redirect_url(short_url):
    long_url = Urls.query.filter_by(short=short_url).first()
    if long_url:
        return redirect(long_url.long)
    else:
        return f"<h1>Url does not exist</h1>"
    
if __name__ == "__main__":
    app.run(debug=True)