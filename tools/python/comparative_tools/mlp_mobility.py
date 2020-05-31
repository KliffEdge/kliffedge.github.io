import numpy as np
import os
import pandas as pd
tip= "There were only 132 countries in the dataset, so we are using only the first 132 countries from the original list"
Y_train = np.loadtxt( "data/y_train.txt", delimiter=" ")
country_names =[]
f = open("data/countries_token.txt", "r")
for x in f:
  country_names.append(x.replace("\n", ""))
df = pd.read_excel (r'datasets/Global_Mobility_Report.xlsx')

countries_raw = df['country_region'].tolist()


#array of countries
countries = []
for country in countries_raw:
    if country not in countries:
        countries.append(country)
np.savetxt("data/countries_token_mobility.txt", countries, fmt="%s")
country_not_in_new = list(set(country_names)-set(countries))

Y_train_final= []
Y_train_token =[]
for i in zip(country_names,Y_train):
  if i not in country_not_in_new:
    Y_train_final.append(Y_train)
  else:
    print(country_names)
 
print(len(Y_train_token))
    

