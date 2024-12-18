import pandas as pd
import numpy as np

np.random.seed(0)
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='D').to_list()
products = ['Produk A', 'Produk B', 'Produk C']
categories = ['Kategori 1', 'Kategori 2', 'Kategori 3']

data = {
    'Tanggal': np.random.choice(dates, 50),
    'Produk': np.random.choice(products, 50),
    'Kategori': np.random.choice(categories, 50),
    'Harga': np.random.randint(10000, 100000, 50),
    'Jumlah': np.random.randint(1, 10, 50)
}

df = pd.DataFrame(data)

df['Total'] = df['Harga'] * df['Jumlah']
df['Tanggal'] = pd.to_datetime(df['Tanggal'])

monthly_revenue = df.resample('M', on='Tanggal')['Total'].sum()
average_revenue = df['Total'].mean()

min_revenue = df['Total'].min()
max_revenue = df['Total'].max()
best_selling_product = df.groupby('Produk')['Jumlah'].sum().idxmax()

print("Total Pendapatan Setiap Bulan:")
print(monthly_revenue)
print("\nRata-rata Pendapatan 2023:", average_revenue)
print("Pendapatan Paling Sedikit:", min_revenue)
print("Pendapatan Paling Banyak:", max_revenue)
print("Produk Terlaris:", best_selling_product)