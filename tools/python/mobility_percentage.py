import pandas as pd
import numpy as np

# def selected_country(countries_list):
#     for country in countries_list:
#         for index, rows in df.iterrows():
#             country_rows =  df_mobilityReport.loc[df_mobilityReport[df_mobilityReport['country_region'] == country], 5:10].sum(axis=1)

    
#     print(*country_rows)
#     return country_rows

df = pd.read_csv(r'data/countries_token_mobility.txt', delimiter="\n")
df_mobilityReport = pd.read_excel (r'datasets/Global_Mobility_Report.xlsx')

#array of countries
countries = []
countries = df.values.tolist()
countries_list = sum(countries, [])


df_mobilityReport['Mean mobility %'] = df_mobilityReport.iloc[:, 5:10].sum(axis=1)
df_mobilityReport['Mean mobility %'] = df_mobilityReport['Mean mobility %'].div(5)

print(df_mobilityReport.head(3))

#for country in countries_list:
df_mobilityReport.to_csv(r'datasets/Mobility_report.txt', sep=",")

# for index, rows in df.iterrows(): 
#     # Create list for the current row 
#     my_list =[rows[5:9]] 
      
#     # append the list to the final list 
#     Row_list.append(my_list) 