import pandas as pd
df = pd.DataFrame({
    'Team':['A','A','B','B'],
    'Score':[10,20,30,40]
})
print(df.groupby('Team').sum())