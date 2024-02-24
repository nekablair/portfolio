from flask import Flask, render_template, request
# from sqlalchemy import SQLAlchemy

app = Flask(__name__) #<--naming the application with variable app

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

@app.route("/")#<--creating route with app.route decorator and endpoint forward slash
@app.route("/home")#<--can have multiple endpoints pointing to the same page, handled by the same function
def home():
    return render_template("home.html", posts=posts, title="Home")#<--using variable name for list of dictionaries

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/projects")
def projects():#<--Kept getting an assertion error(view function mapping is overwriting an existing endpoint function: about. I debugged and found I didn't change the method name.)
    return render_template("projects.html", title="Projects")

@app.route("/blog")
def blog():
    return render_template("blog.html", title="Blog")


if __name__ == "__main__":#<--conditional using dunder, used when script runs module directly
    app.run(debug=True)#<--server in debug mode, not to be used in production
