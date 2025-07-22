import pandas as pd
#head() and tail() - to fetch rows from top and from bottom of data set

df=pd.read_json("sample_data.json")
#default head and tail will give 5 rows and print it
print(df.head(10))
print(df.tail(10))

#info() method give no of rows and columns
#column names
#data types
#non null counts
#memory usage of the data frame
print(df.info())