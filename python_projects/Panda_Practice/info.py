import pandas as pd

df=pd.read_json("sample_data.json")

#info() method give no of rows and columns
#column names
#data types
#non null counts
#memory usage of the data frame
print(df.info())