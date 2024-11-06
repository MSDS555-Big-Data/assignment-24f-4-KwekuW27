import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('../BigData/NYC-pop2.csv', index_col='Borough')

df1 = df.T

df1.plot()
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Population of NYC Boroughs Over Time')
plt.legend(title='Boroughs')
plt.show()
