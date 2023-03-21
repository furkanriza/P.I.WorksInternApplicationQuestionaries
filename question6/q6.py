import pandas as pd

# read the csv file into a pandas dataframe
df = pd.read_csv('outputFromFifthQuestion.csv')

# group the dataframe by country and calculate the median of daily vaccinations for each country
grouped = df.groupby(['country'])['daily_vaccinations'].median()

# sort the groups by the median daily vaccinations in descending order and select the top 3
top3 = grouped.sort_values(ascending=False).head(3)

# loop through the top 3 countries and print their names and median daily vaccinations
for country, vaccinations in top3.items():
    print(country, vaccinations)
