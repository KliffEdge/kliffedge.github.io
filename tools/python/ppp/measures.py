import pandas as pd
import numpy as np
import os
from datetime import datetime
d0 = datetime(2019, 12, 31,0,0)


i = 12012
# for i in range(2):
#     path = os.getcwd()
#     parent = os.path.dirname(path)
#     os.chdir(parent)
# os.chdir("datasets")
# data_dir = os.getcwd()
df = pd.read_excel (r'datasets/acaps-_covid19_government_measures_dataset.xlsx', sheet_name='Database',nrows= 11614)
data_measure_by_country = pd.DataFrame(df, columns= ['COUNTRY','MEASURE'])
countries_raw = df['COUNTRY'].tolist()


#array of countries
countries = []
for country in countries_raw:
    if country not in countries:
        countries.append(country)
countries.sort()
np.savetxt("data/countries_token.txt", countries, fmt="%s")
#array of measures
measures_type_token = ['Movement restrictions','Social distancing' ,'Lockdown']
MR_token =[]
SD_token =[]
L_token =[]
measures_token =[MR_token,SD_token,L_token]
for measure,token in zip(measures_token,measures_type_token):
    f = open("data/Measure Parameters/"+token+".txt", "r")
    Lines = f.readlines() 
    for line in Lines: 
        line = line.replace("\n", "")
        measure.append(line)
np.savetxt("data/measures_parameters.txt", measures_type_token, fmt="%s")
np.savetxt("data/measures_by_parameters.txt", measures_token, fmt="%s")
# measures by country
measure_by_country_raw = []
measure_by_country = []


dayss = []
# Iterate over each row 
for index, rows in df.iterrows(): 
    # Create list for the current row
 
    my_list =[rows.COUNTRY, rows.MEASURE.replace("\xa0", ""),rows.DATE_IMPLEMENTED] 
    
    if isinstance(rows.DATE_IMPLEMENTED,datetime):
        days = rows.DATE_IMPLEMENTED - d0
        my_list[2]=days.days
    elif isinstance(rows.DATE_IMPLEMENTED,str):
         my_list[2]=1
    elif isinstance(rows.DATE_IMPLEMENTED,float):
         my_list[2]=1
   
    # append the list to the final list 
  
    measure_by_country_raw.append(my_list) 

print(measure_by_country_raw)
def sortSecond(val): 
    return val[1]  
  
# Print the list 
for i in countries:
    measure_by_country.append([])
for country in countries:
    for i in measure_by_country_raw:
    
        if i[0] == country:
            pair =i[2],i[1]
            measure_by_country[countries.index(country)].append(pair)
measure_by_country_list =[]
for i in measure_by_country:
    
    sortedList = sorted(i)
    measure_by_country_list.append(sortedList)
np.savetxt("data/measures_by_country.txt", measure_by_country_list, fmt="%s")
       
    




   
   





