from geopy.geocoders import Nominatim
import geopy as gp
import pandas as pd

df = pd.read_csv('../datasets/CSA_20200322.csv')


lat = df['# Latitude'].values.tolist()
lon = df[' Longitude'].values.tolist()

count = 0
locator = Nominatim(user_agent="myGeocoder")

for i in df.index:
    coordinates = str(lat[count]) + "," + str(lon[count])
    location = locator.reverse(coordinates)
    print(location.raw['address']['country'])

        
