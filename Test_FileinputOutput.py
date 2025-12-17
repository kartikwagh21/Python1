import pandas as pd

# Read CSV
df = pd.read_csv('data.csv')
print(df)


# Write CSV
df.to_csv('output.csv', index=False)


# Read JSON
df3 = pd.read_json('data.json')