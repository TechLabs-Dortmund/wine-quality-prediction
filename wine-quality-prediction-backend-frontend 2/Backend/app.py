from flask import Flask, render_template, request, url_for, redirect
from filter import wine_cat, origin
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

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
    data = pd.read_csv('Data/wine_food_data.csv')
    data = data.iloc[0:3]
    return data.transpose().to_dict()

@app.route('/alldata')
def get_alldata():
    wine_data = pd.read_csv('Data/wine_food_data.csv')
    result = wine_data.transpose().to_dict()
    return result

"""

@app.route('/winecat/<wine>')
def get_winecat(wine):
    return wine_cat(wine)

"""

@app.route('/origin/<name>')
def get_origin(name):
    return origin(name)

if __name__ == '__main__':
    app.run(debug=True)
    
