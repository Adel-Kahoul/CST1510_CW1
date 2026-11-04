import pandas as pd
df = pd.read_csv("/Users/samiaharache/Documents/CST1510_CW1/Programming Problems-20261019/DATA/students.csv")
print(df.dtypes)

print(df.describe())

print("Average grade:", df["Grade"].mean())
print("Maximum attendance:", df["Attendance"].max())
print("Youngest student's age:", df["Age"].min())