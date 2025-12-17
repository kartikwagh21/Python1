import pandas as pd
df = pd.DataFrame({
    'A': [1,2,3],
    'B': [4,5,6],
    'C': [7,8,9]
    })

#Select Column
print(df['A'])

#Select rows by index label
print(df.loc[1])

#Select rows by integer position
print(df.iloc[0:2])  #first 2 rows

#Conditional position
print(df[df['B']> 4])