import pandas as pd
import numpy as np

wine_data = pd.read_csv('Data/wine_food_data_f.csv', low_memory=False)

def f_country(country: str):
    wine_data = pd.read_csv('data/wine_food_data_f.csv', low_memory=False)
    selection_c = wine_data[wine_data['country'] == country]
    result_c = selection_c[['country', 'title', 'price', 'rating']]
    result_c_p = result_c.to_dict()
    return result_c_p

def f_price(price: int):
    wine_data = pd.read_csv('data/wine_food_data_f.csv', low_memory=False)
    selection_p = wine_data[wine_data['price'] == price]
    result = selection_p[['title', 'price', 'rating']]
    result_p_p = result.to_dict()
    return result_p_p

def g_rating2(rating = 3):
    wine_data = pd.read_csv('data/wine_food_data_f.csv', low_memory=False)
    selection_r = wine_data[wine_data['rating'] == rating]
    result_r = selection_r[['title', 'price', 'rating']]
    result_r = result_r.sort_values('price')
    result_r = result_r.iloc[0:10, :]
    result_r = result_r.to_dict()
    return result_r

def g_price(price=10):
    wine_data = pd.read_csv('data/wine_food_data_f.csv', low_memory=False)
    best_wine = pd.DataFrame(wine_data.groupby('price')['rating'].max())
    return wine_data.loc[(wine_data.rating == float(best_wine.loc[price])) & (wine_data.price == price),['title', 'price', 'rating']]

def g_rating(rating=3):
    wine_data = pd.read_csv('data/wine_food_data_f.csv', low_memory=False)
    cheapest_wine = pd.DataFrame(wine_data.groupby('rating')['price'].min())
    return wine_data.loc[(wine_data.price == float(cheapest_wine.loc[rating])) & (wine_data.rating == rating),['title', 'price', 'rating']]
