from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["SECRET_KEY"] = "d8ac68546863a23e2bd783d9a4d7ac14"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["POSTS_PER_PAGE"] = 10
db = SQLAlchemy(app)
ma = Marshmallow(app)

from myapp2 import routes