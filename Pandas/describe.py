#step-1 sample data frame

import pandas as pd

data={
    "Name":['Ram','Shyam','sita','giri','geeta','aditi','Raj','simran'],
    "Age":[23,45,23,22,19,20,24,25],
    "Salary":[50000,34000,50000,300000,230000,560000,450000,90000]

}

df=pd.DataFrame(data)
print("Sample Dataframe")
print(df)
print("Descriptive Statistics")
print(df.describe())