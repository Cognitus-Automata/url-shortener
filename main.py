from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from backend.manager import create_schema
from flask import render_template

# initialize the app with the extension
# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

db = SQLAlchemy()

if __name__ == '__main__':

    db.init_app(app)
    # Routes
    create_schema(app, db)
    import backend.models as models
    Entry = models.Entry

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/getshort',methods=['POST'])
    def shortener():
        return render_template('getShort.html')
    
    app.run(debug=True)