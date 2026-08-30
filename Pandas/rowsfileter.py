import pandas as pd

data={
    "Name":['Ram','Shyam','sita','giri','geeta','aditi','Raj','simran'],
    "Age":[23,45,23,22,19,20,24,25],
    "Salary":[50000,34000,50000,300000,230000,560000,450000,90000],
    "Performance_Rate":[90,44,33,56,78,12,34,89]


}

df=pd.DataFrame(data)

high_salary=df[df['Salary'] > 50000]
print("Employess with salary>50000")
print(high_salary)

#filtering rows salary > 50k and age >30
filtered=df[(df['Salary'] > 50000) & (df['Age'] > 20)]
print("Employee List Age > 30 + Salary > 50000")
print(filtered)

#using or condition
filtered_or=df[(df['Age'] > 25) | (df['Performance_Rate'] > 90)]
print("Employee older than 25 and performance rate is greater than 90 ")
print(filtered_or)