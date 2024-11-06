import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('../BigData/NYC-pop1.csv', skiprows=5)

plt.plot(data.index, data['Queens'], label='Queens', color='black')

plt.xlabel('Year')
plt.ylabel('Population (Queens)')
plt.title('Population of Queens Over Time')
plt.legend()

plt.show()