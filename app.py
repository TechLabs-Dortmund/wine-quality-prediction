from flask import Flask, render_template, request, url_for, redirect
from filter import f_country, f_price, filters
import pandas as pd
 
app = Flask(__name__)
 
@app.route('/')
def home():
    return render_template('home.js')

@app.route('/wine')
def wine():
    return render_template('wine.js')

@app.route('/food')
def food():
    return render_template('Food.js')

@app.route('/information')
def information():
    return render_template('information.js')

@app.route("/button", methods=["POST", "GET"])
def button():
    if request.method == "POST":
        get_country = request.form["nm"]
        return redirect(url_for("get_country", country=get_country))
    else:
	    return render_template('button.html')

@app.route('country/<country>')
def get_country(country):
    return f_country(country)

@app.route("/filter", methods=["POST", "GET"])
def filter():
    if request.method == "POST":
        get_filter = request.form["wine"]
        get_filter = request.form["origin"]
        get_filter = request.form["price"]
        get_filter = request.form["food"]
        return redirect(url_for("get_filter", wine = get_filter, origin = get_filter, price = get_filter, food = get_filter))
    else:
	    return render_template("winefilter.html")

@app.route('/results/<wine>/<origin>/<price>/<food>')
def get_filter(wine, origin, price, food):
    return filters(wine, origin, price, food)

if __name__ == '__main__':
    app.run(debug=True)
    