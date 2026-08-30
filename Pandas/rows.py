#head() tail()
#head() 5 first
#tail() 5 last
import pandas as pd


df=pd.read_json(r"C:\Users\LENOVO\OneDrive\Desktop\ML\Pandas\sample_Data.json")

print("Display of 10 rows of first")
print(df.head())

print("Display of 10 rows of Last")
print(df.tail())


#print(df)