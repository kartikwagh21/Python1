import pandas as pd
data = {
    'Name': ['Tom', 'Jerry', 'Spike'],
    'Marks': [85,75,90]
}
df = pd.DataFrame(data)
print(df)
print(df['Marks'])