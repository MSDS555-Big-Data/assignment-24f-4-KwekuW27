import pandas as pd

flights = pd.read_csv('../BigData/flights.csv')

cleaned_flights = flights.dropna()

print(cleaned_flights.to_string(index=False))