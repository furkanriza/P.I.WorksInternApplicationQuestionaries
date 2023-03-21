import pandas as pd

# read the csv file into a pandas dataframe
df = pd.read_csv('outputFromFifthQuestion.csv')

# convert the 'date' column to a datetime format
df['date'] = pd.to_datetime(df['date'], format='%m/%d/%Y')

# filter the dataframe to include only rows with the date '1/6/2021'
filtered = df[df['date'] == '2021-01-06']

# calculate the total number of vaccinations on that date
total_vaccinations = filtered['daily_vaccinations'].sum()

print(total_vaccinations,
      "\nis the is the number of total vaccinations done on 1/6/2021.")
