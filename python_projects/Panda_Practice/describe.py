import pandas as pd

data = {
    "Name": ["Ram", "Shyam", "Ghanshyam", "Dhanshyam", "Aditi", "Jagdish", "Raj", "Simran"],
    "Age":  [28,34,32,29,45,22, 25, 26],
    "Salary": [50000, 60000, 45000, 52000, 49000, 70000, 48000, 58000],
    "Performance_Score": [85,90,78,92,88,95,89,81]
}
df = pd.DataFrame(data)
print(df.describe())
