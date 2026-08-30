import pandas as pd

#read data from csv file into a dataframe
#df=pd.read_csv(r"C:\Users\LENOVO\OneDrive\Desktop\ML\Pandas\sales_data_sample.csv",encoding="latin1")

#read data from excel file
#df=pd.read_excel(r"C:\Users\LENOVO\OneDrive\Desktop\ML\Pandas\data.xlsx",engine="openpyxl")

#read data from json
df=pd.read_json(r"C:\Users\LENOVO\OneDrive\Desktop\ML\Pandas\sample_Data.json")


print(df)
