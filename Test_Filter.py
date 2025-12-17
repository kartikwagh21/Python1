import pandas as pd
df = pd.DataFrame({
    'Name':['A','B','C','D'],
    'Age':[25,30,35,40]
})

#Filter age > 30
print(df[df['Age']>30])

#Multiple Conditions
print(df[(df['Age']>25) & (df['Age']<40)])