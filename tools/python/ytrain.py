import pandas as pd
import numpy as np
import csv




   
    
df = pd.read_excel (r'datasets/total_cases_per_million.xlsx')

countries = list(df.columns) 

countries.remove('date')
countries.remove('World')
# Iterate over each row 
y_train =[]
for country_select in countries:
    country_spread =[]
    for index, rows in df.iterrows(): 
        # Create list for the current row 
        my_list =rows[country_select]

        # append the list to the final list 
        country_spread.append(my_list)
    y_train.append(country_spread)


np.savetxt("data/y_train.txt", y_train, fmt="%s")

import matplotlib.pyplot as plt
print(y_train[174])
plt.plot(y_train[174])

plt.show()





 