import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Name': ['A', 'B', 'C', 'D'],
    'Age': [25, np.nan, 30, np.nan]
})

# Check missing values
print(df.isnull())

# Drop rows with missing values
print(df.dropna())

#Fill Missing values
print(df.fillna(0))
