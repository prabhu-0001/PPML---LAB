import pandas as pd
df_csv=pd.read_csv("sample.csv")
print("Data frame from csv")
print(df_csv)
df_json=pd.read_json("sample.json")
print("Data frame from json")
print(df_json)
