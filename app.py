from flask import Flask, render_template, request, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv #<--brings env variable into python app
import os #<--brings env variable into python app

load_dotenv()
SECRET = os.getenv("SECRET")#<--Returns value of environment variable key as a string if it exists


app = Flask(__name__) #<--naming the application with variable app

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://xxxxxxxxxxx@localhost:5432/portfolio_site" #<--input the database port so it can connect
                                                                #instead of local host , you would use wherever your database url and port is living online
db = SQLAlchemy(app)#<--using db as variable to hold sqlalchemy reference to app in line 4, much quicker way to write instead of the full name

posts = [
    {
        "author": "Neka Blair",
        "title": "Blog Post 1",
        "content": "First post content",
        "date_posted": "April 21, 2023"
    }, 
    {
        "author": "John Doe",
        "title": "Blog Post 2",
        "content": "Second post content",
        "date_posted": "October 9, 2023"
    }
]

#creating a database model
class MockData(db.Model): #<--making our sql data table into a class 
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False) #<--something must be placed into this row since it is nullable=False
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(35), unique=True, nullable=False)
    ip_address = db.Column(db.String(20))
    gender = db.Column(db.String(6))

    def __repr__(self):#<--repr dunder
        return "<Name %r>" % self.name

@app.route("/")#<--creating route with app.route decorator and endpoint forward slash
@app.route("/home")#<--can have multiple endpoints pointing to the same page, handled by the same function
def home():
    return render_template("home.html", title="Home")#<--using variable name for list of dictionaries

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/projects")
def projects():#<--Kept getting an assertion error(view function mapping is overwriting an existing endpoint function: about. I debugged and found I didn't change the method name.)
    return render_template("projects.html", title="Projects")

@app.route("/blog")
def blog():
    return render_template("blog.html", posts=posts, title="Blog")

@app.route("/api/v1/mock_data/", methods=["GET"])
def all_data():
    # print("test")#<--debug purposes
    data = MockData.query.all()
    # print("test2")#<--debug purposes
    data_list = [
        {'first_name': item.first_name, 'last_name': item.last_name, 'email': item.email} for item in data]
    return jsonify(data_list)
    # dummy_data = [#<--debug purposes
    #     {'first_name': "Will", 'last_name': 'Smith'}
    # ]
    # return jsonify(dummy_data)

if __name__ == "__main__":#<--conditional using dunder, used when script runs module directly
    app.run(debug=True)#<--server in debug mode, not to be used in production
