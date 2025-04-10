import pandas as pd

file_path = "data/feedback.csv" 

df = pd.read_csv(file_path) 

df_columns = df.columns

print(df_columns)