import pandas as pd

data={
    "Name":['Ram','Shyam','sita','giri','geeta','aditi','Raj','simran'],
    "Age":[23,None,23,22,19,20,24,25],
    "Salary":[50000,None,50000,300000,230000,560000,450000,90000],
    "Performance_Rate":[90,None,33,56,78,12,34,89]


}

df=pd.DataFrame(data)
print(df)

#linear,ploynomial,time

df.interpolate(method="linear",axis=0,inplace=True)
print(df)
