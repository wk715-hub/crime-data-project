import pandas as pd


# Load the dataset
df = pd.read_csv('state_crime.csv')


# First look at the data
print("Shape:" , df.shape)
print("\nFirst 5 rows:")
print(df.head())

# Find out what columns exist
print("\nColumn Names:")
print(df.columns.tolist())

# Find out data types for each column
print("\nData Types:")
print(df.dtypes)

# Summary statistics for numerical columns
print("\nSummary Statistics:")
print(df.describe())


# Store data for 1960 and 2019 separately
df_1960 = df[df['Year'] == 1960]
df_2019 = df[df['Year'] == 2019]


# Find top 5 states with highest violent crime rates in 1960 and 2019 by using .nlargest
top_violent_1960 = df_1960.nlargest(5, 'Data.Rates.Violent.All')
top_violent_2019 = df_2019.nlargest(5, 'Data.Rates.Violent.All')


# Print the results using the State and Data.Rates.Violent.All columns
print(top_violent_1960[['State', 'Data.Rates.Violent.All']])
print(top_violent_2019[['State', 'Data.Rates.Violent.All']])



# Now the same for property crime rates
top_property_1960 = df_1960.nlargest(5, 'Data.Rates.Property.All')
top_property_2019 = df_2019.nlargest(5, 'Data.Rates.Property.All')

print(top_property_1960[['State', 'Data.Rates.Property.All']])
print(top_property_2019[['State', 'Data.Rates.Property.All']])



