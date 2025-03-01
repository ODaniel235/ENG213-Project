import pandas as pd
excel_file = 'Exporters-of-Crude-Petroleum-2001-Click-to-Select-a-Country.xlsx'
#Loading dataset using pandas
data = pd.read_excel(excel_file)
#Filtering North America data
north_america_data = data[data['Continent ID'] == 'na']
#Getting the trade values
trade_values= north_america_data['Trade Value']
#Extracting Statistical Data
mean_value=trade_values.mean()
min_value = trade_values.min()
max_value=trade_values.max()
std = trade_values.std()
data_range = max_value - min_value
#Printing Extracted Data
print(f"Mean Trade Value : {mean_value}" )
print(f"Standard Deviation : {std}" )
print(f"Minimum Trade Value : {min_value}" )
print(f"Maximum Trade Value : {max_value}" )
print(f"Data Range : {data_range}" )
#Solving a range problem
#Problem is identifying the country top three countries with both the highest and lowest trade values and range between them
sorted_data = north_america_data.sort_values(by='Trade Value', ascending=True)
top_three_countries = sorted_data.head(3).reset_index(drop=False)
bottom_three_countries = sorted_data.tail(3).reset_index(drop=False)
top_three_countries["Rank"] = ['1st', '2nd', '3rd']
bottom_three_countries["Rank"] = ['1st', '2nd', '3rd']
range_value = top_three_countries['Trade Value'].max() - bottom_three_countries['Trade Value'].min()

#Printing the results
print(f"Top 3 countries by trade value:")
print(top_three_countries[["Rank","Country", "Trade Value"]])
print("\nBottom 3 countries by trade value:")
print(bottom_three_countries[["Rank","Country", "Trade Value"]])
print(f"Range between highest and lowest trades: {range_value}")