import pandas as pd

flights = pd.read_csv('../BigData/flights.csv')

year_mode = flights['year'].mode()[0]

flights['year'].fillna(year_mode, inplace=True)

print(flights.to_string(index=False))
