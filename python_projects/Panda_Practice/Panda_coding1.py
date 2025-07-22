import pandas as pd

#Read data from csv file in to a data frame
#encoding is to convert text to format that computer understand, read and store
#utf and latin
# df = pd.read_json("sample_data.json")
# print(df)
xls = pd.ExcelFile('SampleSuperStore.xlsx')
print(xls.sheet_names)
df = pd.read_excel("SampleSuperstore.xlsx")
# print(df)

order_ids = df["Order ID"].tolist()
# print(order_ids)
quantity = df["Quantity"].tolist()
# print(quantity)

dict_order_quantity = dict(zip(order_ids, quantity))
sorted_dict_order_quantity = sorted(dict_order_quantity.items(), key = lambda x : x[1])
print(sorted_dict_order_quantity)
