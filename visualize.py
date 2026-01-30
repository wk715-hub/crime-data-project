# Plot violent crime rate over time for one state (e.g., Washington)
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('state_crime.csv')

df_wa = df[df['State'] == 'Washington']

plt.plot(df_wa['Year'], df_wa['Data.Rates.Violent.All'], marker='.')
plt.title('Violent Crime Rate in Washington Over Time')
plt.xlabel('Year')
plt.ylabel('Violent Crime Rate (per 100,000 inhabitants)')
plt.grid()
plt.show()