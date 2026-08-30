import pandas as pd

data={
    "Name":['Ram','Shyam','sita','giri','geeta','aditi','Raj','simran'],
    "Age":[23,45,23,22,19,20,24,25],
    "Salary":[50000,34000,50000,300000,230000,560000,450000,90000],
    "Performance_Rate":[90,44,33,56,78,12,34,89]


}

df=pd.DataFrame(data)

#Display the data frame
print("Sample Dataframe")
print(df)
print("Names (single column return series)")
name=df['Name']
print(name)

#selecting multiple columns
subset=df[["Name","Salary"]]
print("\nsubset with Name and salary")
print(subset)