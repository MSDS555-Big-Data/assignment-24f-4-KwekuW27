import dask.dataframe as dd
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('../BigData/NYC-pop1.csv', skiprows=5)

data.set_index('Year', inplace=True)

for column in data.columns:
    plt.plot(data.index, data[column], label=column)

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population of NYC Boroughs Over Time')
plt.legend()

plt.show()

