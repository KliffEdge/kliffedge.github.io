import numpy as np
import os
import pandas as pd
from datetime import datetime

tip= "There were only 132 countries in the dataset, so we are using only the first 132 countries from the original list"
#base date is 15th February 2020

#to get raw data
# df = pd.read_excel (r'datasets/Global_Mobility_Report.xlsx')

# countries_raw = df['country_region'].tolist()


# #array of countries
# #list of countries in this list
# countries = []
# for country in countries_raw:
#     if country not in countries:
#         countries.append(country)
# np.savetxt("data/countries_token_mobility.txt", countries, fmt="%s")
# #list of countries that need to be removed from the other list
# # country_not_in_new = list(set(country_names)-set(countries))
# baseline = 100
# d0 = datetime(2020, 2, 15,0,0)
# #creating the raw data
# raw_data_mobility =[]
# import csv

# with open('tools/python/comparative_tools/data/raw_data_moblity.csv', mode='w') as file:
#     writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     for index, rows in df.iterrows(): 
#         # Create list for the current row
    
#         my_list =[rows.country_region, 
#         rows.date - d0,
#         baseline + rows.retail_and_recreation_percent_change_from_baseline ,
#         baseline +rows.grocery_and_pharmacy_percent_change_from_baseline ,
#         baseline +rows.parks_percent_change_from_baseline,
#         baseline +rows.transit_stations_percent_change_from_baseline ,
#         baseline +rows.workplaces_percent_change_from_baseline ,
#         baseline +rows.residential_percent_change_from_baseline ]
        
#         my_list[1] = my_list[1].days
        
      
        
#         # append the list to the final list 

#         writer.writerow(my_list)
      



# Y_train = np.loadtxt( "tools/python/comparative_tools/data/y_train.txt", delimiter=" ") #spread
# Y_train_token =[]
# f = open("data/countries_token.txt", "r")
# for x in f:
#   Y_train_token.append(x.replace("\n", ""))
import csv

X_train_token =[]
with open("data/countries_token_mobility.txt") as csvfile:
  readCSV = csv.reader(csvfile, delimiter=',')

  for x in readCSV:
    x = x[0]
    X_train_token.append(x)




repeat_counter = np.ones(127)
mobility_by_country_raw =[[]]
for i in range(102):
  mobility_by_country_raw[0].append(0)

countries =[]


# Print the list 
raw = pd.read_excel("tools/python/comparative_tools/data/raw_data_moblity.xlsx", nrows=451260)
print(raw)

i= 0
i_day = 0

for index, rows in raw.iterrows(): 
    # Create list for the current row
 
    mean_for_day =np.mean([rows.one,rows.two,rows.thre,rows.fore,rows.fiv,rows.six] )
    country = rows.Country
  
    if i_day <102:

      mobility_by_country_raw[i][i_day] += mean_for_day
      i_day += 1
    
   
    if i_day == 102:
       if (country not in countries):
        countries.append(country)
        i+=1
        print(i,country)
        mobility_by_country_raw.append([])
        for whatthef in range(102):
          mobility_by_country_raw[i].append(0)
        i_day = 0
        mobility_by_country_raw[i][i_day] += mean_for_day
       
        
       else:
         index = X_train_token.index(country)
         repeat_counter[index] += 1
      

with open('tools/python/comparative_tools/data/data_moblity_train.csv', mode='w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)     
    for list,divider in zip(mobility_by_country_raw,repeat_counter):
        if divider > 1:
          list = [x / divider for x in list]
        writer.writerow(list)
print(mobility_by_country_raw)


# Print the list 
# for country in X_train_token:
#   mobility_by_country.append([])
#   for i in raw:
#         if i[0] == country:
#             mean = np.mean([i[2],i[3],i[4],i[5],i[6],i[7]])
#             pair =[i[2],mean]
#             mobility_by_country[X_train_token.index(country)].append(pair)
# print(mobility_by_country)
# moblity_by_country_list =[]
# for i in measure_by_country:
    
#     sortedList = sorted(i)
#     measure_by_country_list.append(sortedList)
# np.savetxt("data/measures_by_country.txt", mobility_by_country_list, fmt="%s")

    

