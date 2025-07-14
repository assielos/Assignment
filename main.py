import pandas as pd 
df = pd.read_csv('messi.csv')
pd.set_option('display.max_columns',12)
print(df.hist)
print(df.info())
print(df.head())