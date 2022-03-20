from flask import Flask, render_template, request, url_for, redirect
from filter import f_country, f_price
import pandas as pd
 
app = Flask(__name__)
 
@app.route('/')
def home():
    return 'Hello'

@app.route('/wine')
def wine():
    return 'Here Wine'

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        country = request.form['country']
        return redirect(url_for("get_country", country=get_country))
    else:
        return render_template('index.html')

#@app.route('/country/<country>')
#def get_country(country: str):
#    return f_country(country)

@app.route('/price/<price>')
def get_price(price: int):
    return f_price(price)

@app.route("/c", methods=["POST", "GET"])
def c():
    if request.method == "POST":
        get_country = request.form["nm"]
        return redirect(url_for("get_country", country=get_country))
    else:
	    return render_template("button.html")

@app.route('/<country>')
def get_country(country):
    return f_country(country)

if __name__ == '__main__':
    app.run(debug=True)
    