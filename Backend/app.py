from flask import Flask, render_template, request, url_for, redirect
from flask_cors import CORS
from filter import f_country, filters, price_cat, wine_cat, origin
import pandas as pd


 
app = Flask(__name__)
CORS(app)

@app.route('/alldata')
def get_data():
    wine_data = pd.read_csv('data/wine_food_data.csv', low_memory=False)
    result = wine_data.transpose().to_dict()
    return result

"""
@app.route('/data')
def get_dict():
    return {
        "wine_cat":"red", 
        "country":"Germany",
        "price_cat":"1", 
        "rating":"2"
        }


 
@app.route('/')
def home():
    return "hello"

@app.route('/wine') 
def wine():
    return render_template('./Frontend/src/Components/Navbar Components/Wine.js')

@app.route('/food')
def food():
    return render_template('Frontend/src/Components/Navbar Components/Food.js')

@app.route('/information')
def information():
    return render_template('Frontend/src/Components/Navbar Components/Information.js')

@app.route("/button", methods=["POST", "GET"])
def button():
    if request.method == "POST":
        get_country = request.form["nm"]
        return redirect(url_for("get_country", country=get_country))
    else:
	    return render_template('button.html')

@app.route('/country/<country>')
def get_country(country):
    return f_country(country)

@app.route("/filter", methods=["POST", "GET"])
def filter():
    if request.method == "POST":
        get_filter = request.form["wine"]
        get_filter = request.form["origin"]
        return redirect(url_for("get_filter", wine = get_filter, origin = get_filter))
    else:
	    return render_template("winefilter.html")

@app.route('/tro/<wine>/<origin>')
def get_filter(wine, origin):
    return filters(wine, origin)

@app.route("/category", methods=["POST", "GET"])
def category():
    if request.method == "POST":
        get_winecat = request.form["nm"]
        return redirect(url_for("get_winecat", wine=get_winecat))
    else:
	    return render_template('wine_cat.html')

@app.route("/where", methods=["POST", "GET"])
def where():
    if request.method == "POST":
        get_origin = request.form["nm"]
        return redirect(url_for("get_origin", name=get_origin))
    else:
	    return render_template('wine_cat.html')

@app.route("/price", methods=["POST", "GET"])
def price():
    if request.method == "POST":
        get_pricecat = request.form["nm"]
        return redirect(url_for("get_pricecat", price=get_pricecat))
    else:
	    return render_template('price_cat.html')

@app.route('/pricecat/<price>')
def get_pricecat(price):
    return price_cat(price)

@app.route('/origin/<name>')
def get_origin(name):
    return origin(name)

@app.route('/winecat/<wine>')
def get_winecat(wine):
    return wine_cat(wine)


if __name__ == '__main__':
    app.run(debug=True)
    
"""