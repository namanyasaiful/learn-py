import pandas as pd

csvFile = pd.read_csv("pertemuan 14/insurance.csv")
desc = csvFile.sort_values(by=['sex'])
asc = csvFile.sort_values(by=['sex'], ascending=False)
print("hasil sorting descending", desc.head())
print("hasil sorting ascending", asc.head())