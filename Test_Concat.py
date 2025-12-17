import pandas as pd
df1 = pd.DataFrame({'A': [1,2,3]})
df2 = pd.DataFrame({'A': [4,5,6]})
print(pd.concat([df1,df2]))
print(pd.concat([df1,df2],axis = 1))