#pd.merge(df1,df2,on="Column_name", how="type of join")

import pandas as pd

#customers dataframe
df_customes=pd.DataFrame({
    'CustomerID' : [1,2,3],
    'Name' : ['Ramesh','Suresh','Kalpesh']
})

df_orders= pd.DataFrame({
    'CustomerID' : [1,2,4],
    'OrderAmount' : [250,450,350]
})

#merge
df_merged=pd.merge(df_customes,df_orders,on="CustomerID",how="cross")
print("cross join")
print(df_merged)