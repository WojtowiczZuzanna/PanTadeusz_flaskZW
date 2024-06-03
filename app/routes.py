from app import app
import requests
from flask import render_template, redirect

@app.route("/")
def index():
    return render_template("index.html.jinja")

@app.route("/księgi", endpoint="księgi")
def księgi():
    return render_template("ksiegi.html.jinja")


@app.route("/księgi/k1", endpoint="księgi1")
def księgi1():
    return render_template("k1.html.jinja")

@app.route("/księgi/k2", endpoint="księgi2")
def księgi2():
    return render_template("k2.html.jinja")

@app.route("/księgi/k3", endpoint="księgi3")
def księgi3():
    return render_template("k3.html.jinja")

@app.route("/księgi/k4", endpoint="księgi4")
def księgi4():
    return render_template("k4.html.jinja")

@app.route("/księgi/k5", endpoint="księgi5")
def księgi5():
    return render_template("k5.html.jinja")

@app.route("/księgi/k6", endpoint="księgi6")
def księgi6():
    return render_template("k6.html.jinja")

@app.route("/księgi/k7", endpoint="księgi7")
def księgi7():
    return render_template("k7.html.jinja")

@app.route("/księgi/k8", endpoint="księgi8")
def księgi8():
    return render_template("k8.html.jinja")

@app.route("/księgi/k9", endpoint="księgi9")
def księgi9():
    return render_template("k9.html.jinja")

@app.route("/księgi/k10", endpoint="księgi10")
def księgi10():
    return render_template("k10.html.jinja")

@app.route("/księgi/k11", endpoint="księgi11")
def księgi11():
    return render_template("k11.html.jinja")

@app.route("/księgi/k12", endpoint="księgi12")
def księgi12():
    return render_template("k12.html.jinja")

