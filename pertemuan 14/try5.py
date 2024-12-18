import pandas as pd
csvFile = pd.read_csv("pertemuan 14/insurance.csv")
dfFilter = csvFile.filter(items=['sex', 'region'])

print("hasil filter", dfFilter.head())