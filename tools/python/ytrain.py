import pandas as pd
import numpy as np
import csv




   
    
df = pd.read_excel (r'datasets/total_cases_per_million.xlsx')

countries = list(df.columns) 

countries.remove('date')
countries.remove('World')
countries_check=[]
with open('data/countries_token.txt') as f:
   for line in f:
        line = line.replace("\n", "")
        countries_check.append(line)




a =set(countries) ^ set(countries_check)
print(len(a))
countries_not_in_orginal =list(set(countries_check).difference(countries))
print(len(countries_not_in_orginal))
print(countries_not_in_orginal)
countries_not_in_new = list(set(countries).difference(countries_check))
print(len(countries_not_in_new))
print(countries_not_in_new)





 