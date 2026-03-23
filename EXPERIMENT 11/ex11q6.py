import pandas as pd
data={'Name':['Alice',"Bob",'Charlie'],
      'Age':[25,30,35],
      'City':['New york','San fransisco','Los angles']}
df=pd.DataFrame(data);
print("Data Frame : \n",df)
print("Age column : ",df['Age'])
print("Row at index 1 : ",df.iloc[1])