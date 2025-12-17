import pandas as pd

df = pd.DataFrame({
    'A':[1,2,3],
    'B':[4,5,6],
    'C':[7,8,9]
})
#Add New Column
df['D'] = df['A']+df['B']
print(df)
print("----------------")

df['E'] = df['B']+df['C']
print(df)
print("---------------")

#Update a value 
df.loc[1,'A'] = 100
print(df)
print("---------------")

#Drop a column
df = df.drop('C', axis=1)
df = df.drop('D', axis=1)
df = df.drop('E', axis=1)
print(df)
print("---------------")

#Rename column
df = df.rename(columns={'A':'Alpha'})
print(df)
print("---------------")
