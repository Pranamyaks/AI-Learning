import pandas as pd


df=pd.read_json(r"C:\Users\LENOVO\OneDrive\Desktop\ML\Pandas\sample_Data.json")

print("Displaying the  info of data set")
print(df.info())