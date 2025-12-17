import pandas as pd 
df = pd.DataFrame({
    'Name':['A','B','C'],
    'Marks':['88','75','92']
})
print(df.sort_values('Marks'))
print(df.sort_values('Marks', ascending=False))