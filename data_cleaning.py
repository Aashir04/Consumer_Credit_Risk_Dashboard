


import pandas as pd

# Loading German Credit dataset
df = pd.read_csv('german_credit_data.csv')

# Displaying first 5 rows and column information to confirm it loaded correctly
print(df.head())
print(df.info())
