from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def homepage():
    return render_template("index.html")

@app.route('/web_development')
def web_development():
    return render_template("web_development.html", title="Web Development")

@app.route('/development')
def development():
    return render_template("development.html", title="Development")

@app.route('/pixel_art')
def pixel_art():
    return render_template("pixel_art.html", title="Pixel Art")


@app.route('/about')
def about():
    return render_template("index.html", title="Home")

