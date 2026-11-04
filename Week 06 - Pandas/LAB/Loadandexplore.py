import pandas as pd

df = pd.read_csv("/Users/samiaharache/Documents/CST1510_CW1/Programming Problems-20261019/DATA/students.csv")

print(df.head())
print(df.tail(3))
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())