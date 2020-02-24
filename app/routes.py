from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def homepage():
    return render_template("index.html")

@app.route('/web_design')
def web_design():
    return render_template("index.html", title="Home")

@app.route('/development')
def development():
    return render_template("index.html", title="Home")

@app.route('/pixel_art')
def pixel_art():
    return render_template("index.html", title="Home")


@app.route('/about')
def about():
    return render_template("index.html", title="Home")

