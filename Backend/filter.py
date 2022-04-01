import pandas as pd
import numpy as np

wine_data = pd.read_csv('Data/wine_food_data.csv')


# filter wine categorie
def wine_cat(wine = 'red'):
    cat_result = wine_data[wine_data['wine_categories'].str.contains(wine)]
    output_dict_c = cat_result.transpose().to_dict()
    return output_dict_c

# filter origin 
def origin(name = 'national'):
    if name == 'europe':
        return wine_data[(wine_data['country'] == 'Spain') 
                         | (wine_data['country'] == 'Portugal') 
                         | (wine_data['country'] == 'France') 
                         | (wine_data['country'] == 'Germany') 
                         | (wine_data['country'] == 'Italy') 
                         | (wine_data['country'] == 'Romania') 
                         | (wine_data['country'] == 'Austria')
                         | (wine_data['country'] == 'Slovenia')
                         | (wine_data['country'] == 'Croatia')
                         | (wine_data['country'] == 'England')
                         | (wine_data['country'] == 'Czech Republic')
                         | (wine_data['country'] == 'Bulgaria')
                         | (wine_data['country'] == 'Greece')
                         | (wine_data['country'] == 'Turkey')
                         | (wine_data['country'] == 'Moldova')
                         | (wine_data['country'] == 'Hungary')
                         | (wine_data['country'] == 'Switzerland')
                         | (wine_data['country'] == 'Ukraine')
                         | (wine_data['country'] == 'Slovakia')
                         | (wine_data['country'] == 'Serbia')
                         | (wine_data['country'] == 'Luxembourg')
                         | (wine_data['country'] == 'Macedonia')].transpose().to_dict()
    elif name == 'national':
        return wine_data[wine_data['country'] == 'Germany'].transpose().to_dict()
    elif name == 'international':
        return wine_data[(wine_data['country'] == 'Mexico') 
                         | (wine_data['country'] == 'China') 
                         | (wine_data['country'] == 'US') 
                         | (wine_data['country'] == 'Argentina') 
                         | (wine_data['country'] == 'Chile') 
                         | (wine_data['country'] == 'Australia') 
                         | (wine_data['country'] == 'South Africa') 
                         | (wine_data['country'] == 'New Zealand') 
                         | (wine_data['country'] == 'Israel')
                         | (wine_data['country'] == 'Canada')
                         | (wine_data['country'] == 'Lebanon')
                         | (wine_data['country'] == 'Brazil')
                         | (wine_data['country'] == 'Morocco')
                         | (wine_data['country'] == 'Uruguay')
                         | (wine_data['country'] == 'Peru')
                         | (wine_data['country'] == 'India')
                         | (wine_data['country'] == 'Georgia')
                         | (wine_data['country'] == 'Armenia')].transpose().to_dict()


# filter price category 
def price_cat(price = 1):
    selection = wine_data[wine_data['price_cat'] == price]
    result_p = selection.sort_values('price')
    result_p = result_p.transpose().to_dict()
    return result_p

# filter together
def filters(wine = 'red', origin = 'national', price = 1, food = 1):
    wine_data = pd.read_csv('data/wine_food_data.csv')
    if wine in ['red', 'white', 'rosé']:
        wine_cat = wine_data[wine_data['wine_categories'].str.contains(wine)]
    else: 
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
    else:
        wine_o = wine_cat
    
    if price in [1, 2, 3]:
        wine_p = wine_o[wine_o['price_cat'] == price]
    else: 
        wine_p = wine_o

    if food == 1:
        wine_f = wine_p
    else: 
        wine_f = wine_p.drop('food', axis = 1)
    
    output = wine_f.transpose().to_dict()
    return output

