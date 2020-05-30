import pandas as pd
import numpy as np
import os
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
measures_type_token = ['Movement restrictions','Public health measures','Governance and Socio-economic measures','Social distancing' ,'Lockdown']
MR_token =[]
PHM_token =[]
GAS_token =[]
SD_token =[]
L_token =[]
measures_token =[MR_token,PHM_token,GAS_token,SD_token,L_token]
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


 
# Iterate over each row 
for index, rows in df.iterrows(): 
    # Create list for the current row 
    my_list =[rows.COUNTRY, rows.MEASURE.replace("\xa0", "")] 

    # append the list to the final list 
    measure_by_country_raw.append(my_list) 
  
# Print the list 
for i in countries:
    measure_by_country.append([])
for country in countries:
    for i in measure_by_country_raw:
    
        if i[0] == country:
            measure_by_country[countries.index(country)].append(i[1])

np.savetxt("data/measures_by_country.txt", measure_by_country, fmt="%s")
       
    




   
   





