import pandas as pd

data={
    "Name":['Ram','Shyam','sita','giri','geeta','aditi','Raj','simran'],
    "Age":[23,45,23,22,19,20,24,25],
    "Salary":[50000,34000,50000,300000,230000,560000,450000,90000],
    "Performance_Rate":[90,44,33,56,78,12,34,89]


}

df=pd.DataFrame(data)
print(df)

#deleting
#df.drop(columns=['column_name'], inplace=True)
print("After Removing Performance_Rate")
df.drop(columns=['Performance_Rate','Age'] , inplace=True)
print(df)