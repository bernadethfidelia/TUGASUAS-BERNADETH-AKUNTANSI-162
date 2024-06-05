import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Menggabungkan data dari beberapa tabel menjadi satu DataFrame
data_minggu1 = {
    'Tanggal': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06'],
    'Produk': ['Produk A', 'Produk B', 'Produk A', 'Produk C', 'Produk B', 'Produk A', 'Produk D', 'Produk B'],
    'Jumlah': [10, 5, 8, 7, 6, 9, 10, 7],
    'Pendapatan': [500000, 300000, 400000, 350000, 360000, 450000, 600000, 420000]
}

data_minggu2 = {
    'Tanggal': ['2024-01-07', '2024-01-08', '2024-01-09', '2024-01-10', '2024-01-11', '2024-01-12', '2024-01-13', '2024-01-14'],
    'Produk': ['Produk A', 'Produk C', 'Produk B', 'Produk A', 'Produk D', 'Produk C', 'Produk A', 'Produk B'],
    'Jumlah': [5, 6, 4, 10, 8, 9, 7, 8],
    'Pendapatan': [250000, 300000, 240000, 500000, 480000, 450000, 350000, 480000]
}

data_minggu3 = {
    'Tanggal': ['2024-01-15', '2024-01-16', '2024-01-17', '2024-01-18', '2024-01-19', '2024-01-20', '2024-01-21', '2024-01-22'],
    'Produk': ['Produk D', 'Produk A', 'Produk B', 'Produk C', 'Produk A', 'Produk D', 'Produk B', 'Produk C'],
    'Jumlah': [6, 10, 7, 5, 8, 9, 6, 7],
    'Pendapatan': [360000, 500000, 420000, 250000, 400000, 540000, 360000, 350000]
}

data_minggu4 = {
    'Tanggal': ['2024-01-23', '2024-01-24', '2024-01-25', '2024-01-26', '2024-01-27', '2024-01-28', '2024-01-29', '2024-01-30', '2024-01-31'],
    'Produk': ['Produk A', 'Produk B', 'Produk D', 'Produk C', 'Produk A', 'Produk B', 'Produk D', 'Produk C', 'Produk A'],
    'Jumlah': [5, 8, 10, 6, 7, 9, 8, 7, 10],
    'Pendapatan': [250000, 480000, 600000, 300000, 350000, 540000, 480000, 350000, 500000]
}

df_minggu1 = pd.DataFrame(data_minggu1)
df_minggu2 = pd.DataFrame(data_minggu2)
df_minggu3 = pd.DataFrame(data_minggu3)
df_minggu4 = pd.DataFrame(data_minggu4)

df = pd.concat([df_minggu1, df_minggu2, df_minggu3, df_minggu4], ignore_index=True)

# 1. Histogram untuk distribusi jumlah produk yang terjual
plt.figure(figsize=(10, 5))
sns.histplot(df['Jumlah'], bins=10, kde=True)
plt.title('Distribusi Jumlah Produk Terjual')
plt.xlabel('Jumlah Produk Terjual')
plt.ylabel('Frekuensi')
plt.grid(True)
plt.show()

# 2. Scatter Plot untuk hubungan antara jumlah produk yang terjual dan pendapatan
plt.figure(figsize=(10, 5))
sns.scatterplot(data=df, x='Jumlah', y='Pendapatan', hue='Produk', palette='viridis', s=100)
plt.title('Hubungan antara Jumlah Produk Terjual dan Pendapatan')
plt.xlabel('Jumlah Produk Terjual')
plt.ylabel('Pendapatan')
plt.grid(True)
plt.show()

# 3. Grafik Batang untuk jumlah total penjualan tiap produk
plt.figure(figsize=(10, 5))
df.groupby('Produk')['Jumlah'].sum().plot(kind='bar', color='skyblue')
plt.title('Jumlah Total Penjualan Tiap Produk')
plt.xlabel('Produk')
plt.ylabel('Jumlah Terjual')
plt.grid(axis='y')
plt.show()

# 4. Grafik Garis untuk tren pendapatan harian
plt.figure(figsize=(10, 5))
df.groupby('Tanggal')['Pendapatan'].sum().plot(kind='line', marker='o', linestyle='-', color='b')
plt.title('Tren Pendapatan Harian')
plt.xlabel('Tanggal')
plt.ylabel('Pendapatan')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()
