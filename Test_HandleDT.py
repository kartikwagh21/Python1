import pandas as pd
df = pd.DataFrame({
    'Date': ['2025-01-01', '2025-02-10', '2025-03-15']
})
df['Date'] = pd.to_datetime(df['Date'])
print(df['Date'].dt.month)
print(df['Date'].dt.day)
print(df[df['Date'] > '2025-02-01'])