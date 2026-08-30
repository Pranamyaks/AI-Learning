import pandas as pd

data={
    "Name":['Ram','Shyam','sita','giri','geeta','aditi','Raj','simran'],
    "Age":[23,45,23,22,19,20,24,25],
    "Salary":[50000,34000,50000,300000,230000,560000,450000,90000],
    "Performance_Rate":[90,44,33,56,78,12,34,89]


}

df=pd.DataFrame(data)
print(df)

#adding column to the data stright forward
df["Bonus"]=df["Salary"] * 0.1
print(df)

#using insert() method with precise location
#df.insert(loc,'column_name',data)
df.insert(0,"Employee_ID",[10,20,30,40,50,60,70,80])
print(df)