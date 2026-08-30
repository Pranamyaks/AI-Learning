#fillna()
#fillna(value,inplace=True)

import pandas as pd

data={
    "Name":['Ram',None,'sita','giri','geeta','aditi','Raj','simran'],
    "Age":[23,None,23,22,19,20,24,25],
    "Salary":[50000,None,50000,300000,230000,560000,450000,90000],
    "Performance_Rate":[90,None,33,56,78,12,34,89]


}

df=pd.DataFrame(data)
print(df)

#filling missing values
'''df.fillna(0,inplace=True)
print(df)'''

#filling missing values by using mean method
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)
print(df)