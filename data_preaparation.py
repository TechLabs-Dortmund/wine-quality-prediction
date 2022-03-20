import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

wine_data = pd.read_csv('Data/winemag-data-130k-v2.csv.zip', compression='zip', low_memory=False)

print(wine_data.head())

# delete unnecessary columns
wine_data = wine_data.drop(['Unnamed: 0', 'taster_name', 'taster_twitter_handle', 'region_2'], axis = 1)

# data overview 
def resumetable(df):
    print(f"Dataset Shape: {df.shape}")
    summary = pd.DataFrame(df.dtypes,columns=['dtypes'])
    summary = summary.reset_index()
    summary['Name'] = summary['index']
    summary = summary[['Name','dtypes']]
    summary['counts'] = df.count().values
    summary['Missing'] = df.isnull().sum().values
    summary['missing_ration'] = (df.isnull().sum().values / df.shape[0]) * 100
    summary['Uniques'] = df.nunique().values
    return summary

print(resumetable(wine_data))

# drop missing values in certain columns
wine_data = wine_data.dropna(subset=['price', 'country', 'variety'])
wine_data = wine_data.drop(['designation'], axis = 1)

# drop double entries based on description and title 
wine_data = wine_data.drop_duplicates(['description','title'])

wine_data = wine_data.reset_index(drop = True)

print(wine_data.describe())

# transform point system 
def cat_points(points):
    if points in list(range(80,83)):
        return 0
    elif points in list(range(83,87)):
        return 1
    elif points in list(range(87,90)):
        return 2
    elif points in list(range(90,94)):
        return 3
    elif points in list(range(94,98)):
        return 4
    else:
        return 5

wine_data["rating"] = wine_data["points"].apply(cat_points)

wine_data = wine_data.drop(['points'], axis = 1)

wine_data = wine_data.dropna(subset=['region_1'])
wine_data = wine_data.reset_index(drop = True)

# assign different varieties to categories of wine
conditions_wine = [
    (wine_data['variety'].str.contains('Sauvignon Blanc')) | (wine_data['variety'].str.contains('Pinot Grigio')) | (wine_data['variety'].str.contains('Albariño')) | (wine_data['variety'].str.contains('Pino Gris')),
    (wine_data['variety'].str.contains('Gewürztraminer'))  | (wine_data['variety'].str.contains('Malvasia')) | (wine_data['variety'].str.contains('Moscato')) | (wine_data['variety'].str.contains('Riesling')),
    (wine_data['variety'].str.contains('Chardonnay')) | (wine_data['variety'].str.contains('Viognier')) | (wine_data['variety'].str.contains('Roussanne')) | (wine_data['variety'].str.contains('Marsanne')),
    (wine_data['variety'].str.contains('Champagne')) | (wine_data['variety'].str.contains('Prosecco')) | (wine_data['variety'].str.contains('Sparkling')) | (wine_data['variety'].str.contains('Cava')),
    (wine_data['variety'].str.contains('St. Laurent')) | (wine_data['variety'].str.contains('Gamay')) | (wine_data['variety'].str.contains('Pinot Noir')) | (wine_data['variety'].str.contains('Zweigelt')),
    (wine_data['variety'].str.contains('Red Table Wine')) | (wine_data['variety'].str.contains('Zinfandel')) | (wine_data['variety'].str.contains('Merlot')),
    (wine_data['variety'].str.contains('Cabernet Sauvignon')) | (wine_data['variety'].str.contains('Malbec')) | (wine_data['variety'].str.contains('Anglianico')) | (wine_data['variety'].str.contains('Syrah')) | (wine_data['variety'].str.contains('Sangiovese')) | (wine_data['variety'].str.contains('Carbanet Franc')),
    (wine_data['variety'].str.contains('Late Harvest')) | (wine_data['variety'] == 'Port') | (wine_data['variety'].str.contains('Ice Wine')) | (wine_data['variety'].str.contains('Sherry')),
    (wine_data['variety'].str.contains('Rosé'))]

# categories of wine
values_wine = ['dry white wine', 'sweet white wine', 'rich white wine', 'sparkling wine', 'light red wine', 'medium red wine', 'bold red wine', 'dessert wine', 'rosé']

wine_data['wine_categories'] = np.select(conditions_wine, values_wine)

# not all data can be assigned to categorie 
# variety with largest amount of different sorts of wine in this dataset are assigned manually 
variety_u_null = wine_data[wine_data['wine_categories'] == '0']
variety_u_null_g = variety_u_null.groupby('variety')['variety'].count()
v_sort = variety_u_null_g.sort_values(ascending = False)

# price categories 
price = wine_data.price
price = price.sort_values(ascending = False)
summe = price.sum()
price = pd.DataFrame(price)
price['perci'] = price/summe
price['perci_c'] = price['perci'].cumsum()
FFFF = price[price['perci_c'] <= 0.15]
FFF = price[(price['perci_c'] > 0.15) & (price['perci_c'] <= 0.48)]
FF = price[(price['perci_c'] > 0.48) & (price['perci_c'] <= 0.87)]
F = price[price['perci_c'] > 0.87]

conditions_price = [
    (wine_data['price'] >= 101),
    (wine_data['price'] < 101) & (wine_data['price'] >= 51),
    (wine_data['price'] < 51) & (wine_data['price'] >= 21),
    (wine_data['price'] < 21)
    ]

# price categories: 4 is most expensive 
values_price = [4, 3, 2, 1]

wine_data['price_cat'] = np.select(conditions_price, values_price)

# food link
conditions_food = [
    (wine_data['wine_categories'] == 'dry white wine'),
    (wine_data['wine_categories'] == 'sweet white wine'),
    (wine_data['wine_categories'] == 'rich white wine'),
    (wine_data['wine_categories'] == 'sparkling wine'),
    (wine_data['wine_categories'] == 'light red wine'),
    (wine_data['wine_categories'] == 'medium red wine'),
    (wine_data['wine_categories'] == 'bold red wine'),
    (wine_data['wine_categories'] == 'desert wine'),
    (wine_data['wine_categories'] == 'rosé')]

values_food = ['vegetables, roasted vegetables, starches, fish', 
          'soft cheese, hard cheese, cured meat, sweets',
          'soft cheese, starches, fish, rich fish, white meat',
          'vegetables, soft cheese, hard cheese, starches, fish',
          'roasted vegetables, starches, rich fish, white meat, cured meat',
          'roasted vegetables, hard cheese, starches, white meat, red meat, cured meat',
          'hard cheese, starches, red meat, cured meat', 
          'soft cheese, starches, cured meat, sweets',
          'everything']

wine_data['food'] = np.select(conditions_food, values_food)

wine_data_food = wine_data[wine_data['food'] != '0']
wine_data_food = wine_data_food.reset_index(drop = True)

wine_data_food_f = wine_data_food.drop(['description'], axis = 1)