import pandas as pd

csvFile = pd.read_csv("pertemuan 14/insurance.csv")

group = csvFile.groupby('sex').agg(rata_rata = ('age', 'mean'),
median = ('charges', 'median'))

print("hasil filter", group.head())