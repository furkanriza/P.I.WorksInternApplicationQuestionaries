import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('outputFromFourthQuestion.csv')

# Calculate the minimum daily vaccinations for each country
min_daily_vaccinations = df.groupby('country')['daily_vaccinations'].min()

# Update empty daily vaccinations with minimum value for each country
df['daily_vaccinations'] = df.apply(
    lambda row: min_daily_vaccinations[row['country']] if pd.isna(
        row['daily_vaccinations']) else row['daily_vaccinations'],
    axis=1)

# Write the updated DataFrame to a new CSV file
df.to_csv('outputFromFifthQuestion.csv', index=False)
