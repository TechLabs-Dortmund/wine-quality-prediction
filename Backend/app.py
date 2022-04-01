from flask import Flask, render_template, request, url_for, redirect
from filter import wine_cat, origin
import pandas as pd
 
app = Flask(__name__)

@app.route("/data")
def get_testdata():
    return {
            'country': 'US',
            'price': 13.0,
            'province': 'Michigan',
            'region_1': 'Lake Michigan Shore',
            'title': 'St. Julian 2013 Reserve Late Harvest Riesling (Lake Michigan Shore)',
            'variety': 'Riesling',
            'winery': 'St. Julian',
            'rating': 2,
            'wine_categories': 'sweet white wine',
            'price_cat': 1,
            'food': 'soft cheese, hard cheese, cured meat, sweets'
    }

@app.route('/testdata')
def get_data():
    data = pd.read_csv('data/wine_food_data.csv')
    data = data.iloc[0]
    return data.transpose().to_dict()

@app.route('/alldata')
def get_alldata():
    wine_data = pd.read_csv('data/wine_food_data.csv')
    result = wine_data.transpose().to_dict()
    return result

"""
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

@app.route('/origin/<name>')
def get_origin(name):
    return origin(name)

@app.route('/winecat/<wine>')
def get_winecat(wine):
    return wine_cat(wine)

"""
if __name__ == '__main__':
    app.run(debug=True)
    
