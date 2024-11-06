import pandas as pd

flights = pd.read_csv('../BigData/flights.csv')

unique_flights = flights.drop_duplicates()

print(unique_flights.to_string(index=False))