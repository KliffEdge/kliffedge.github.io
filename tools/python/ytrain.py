import pandas as pd
import numpy as np

df = pd.read_excel (r'datasets/COVID-19-geographic-disbtribution-worldwide.xlsx', sheet_name='COVID-19-geographic-disbtributi',nrows= 20293)
data_measure_by_country = pd.DataFrame(df, columns= ['country'])


countries_raw = df['country'].tolist()
countries_check=[]
with open('data/countries_token.txt') as f:
   for line in f:
        line = line.replace("\n", "")
        countries_check.append(line)
print(len(countries_check))
#array of countries
countries = []
for country in countries_raw:
    if country not in countries:
        
        countries.append(country.replace("_", " "))


a =set(countries) ^ set(countries_check)

countries_not_in_orginal = set(countries_check).difference(countries)

countries_not_in_new = set(countries).difference(countries_check)




case_by_country_raw = []
case_by_country = []


 
# Iterate over each row 
for index, rows in df.iterrows(): 
    # Create list for the current row 
    my_list =[rows.country, rows.cases] 

    # append the list to the final list 
    case_by_country_raw.append(my_list) 
  
# Print the list 
for i in countries:
    case_by_country.append([])
for country in countries:
    for i in case_by_country_raw:
    
        if i[0] == country:
           case_by_country[countries.index(country)].append(i[1])
print(case_by_country)