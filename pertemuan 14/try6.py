import pandas as pd

csvFile = pd.read_csv("pertemuan 14/insurance.csv")
addColumn = csvFile['diskon'] = csvFile['charges']*0.05
print("hasil filter \n", csvFile.head())