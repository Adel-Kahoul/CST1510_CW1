import pandas as pd

df = pd.read_csv("/Users/samiaharache/Documents/CST1510_CW1/Programming Problems-20261019/DATA/students.csv")

london = df[df["City"] == "London"]
print(london)
print("Students in London:", len(london))

low = df[df["Grade"] < 65]
print(low[["Name", "Grade"]])

print(df["City"].value_counts())