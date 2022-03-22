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


# filter together
def filters(wine, origin, price, food):
    wine_data = pd.read_csv('data/wine_food_data.csv', low_memory=False)
    if wine in ['red', 'white', 'rosé']:
        wine_cat = wine_data[wine_data['wine_categories'].str.contains(wine)]
    elif wine == 0: 
        wine_cat = wine_data
        
    if origin == 'europe':
        wine_o = wine_cat[(wine_cat['country'] == 'Spain') 
                         | (wine_cat['country'] == 'Portugal') 
                         | (wine_cat['country'] == 'France') 
                         | (wine_cat['country'] == 'Germany') 
                         | (wine_cat['country'] == 'Italy') 
                         | (wine_cat['country'] == 'Romania') 
                         | (wine_cat['country'] == 'Austria')
                         | (wine_cat['country'] == 'Slovenia')
                         | (wine_cat['country'] == 'Croatia')
                         | (wine_cat['country'] == 'England')
                         | (wine_cat['country'] == 'Czech Republic')
                         | (wine_cat['country'] == 'Bulgaria')
                         | (wine_cat['country'] == 'Greece')
                         | (wine_cat['country'] == 'Turkey')
                         | (wine_cat['country'] == 'Moldova')
                         | (wine_cat['country'] == 'Hungary')
                         | (wine_cat['country'] == 'Switzerland')
                         | (wine_cat['country'] == 'Ukraine')
                         | (wine_cat['country'] == 'Slovakia')
                         | (wine_cat['country'] == 'Serbia')
                         | (wine_cat['country'] == 'Luxembourg')
                         | (wine_cat['country'] == 'Macedonia')]
    elif origin == 'national':
        wine_o = wine_cat[wine_cat['country'] == 'Germany']
    elif origin == 'international':
        wine_o =  wine_cat[(wine_cat['country'] == 'Mexico') 
                         | (wine_cat['country'] == 'China') 
                         | (wine_cat['country'] == 'US') 
                         | (wine_cat['country'] == 'Argentina') 
                         | (wine_cat['country'] == 'Chile') 
                         | (wine_cat['country'] == 'Australia') 
                         | (wine_cat['country'] == 'South Africa') 
                         | (wine_cat['country'] == 'New Zealand') 
                         | (wine_cat['country'] == 'Israel')
                         | (wine_cat['country'] == 'Canada')
                         | (wine_cat['country'] == 'Lebanon')
                         | (wine_cat['country'] == 'Brazil')
                         | (wine_cat['country'] == 'Morocco')
                         | (wine_cat['country'] == 'Uruguay')
                         | (wine_cat['country'] == 'Peru')
                         | (wine_cat['country'] == 'India')
                         | (wine_cat['country'] == 'Georgia')
                         | (wine_cat['country'] == 'Armenia')]
    elif origin == 0:
        wine_o = wine_cat
        
    if price in [1, 2, 3]:
        wine_p = wine_o[wine_o['price_cat'] == price]
    elif price == 0:
        wine_p = wine_o
    
    if food == 1:
        wine_f = wine_p
    elif food == 0:
        wine_f = wine_p.drop('food', axis = 1)
    return wine_f