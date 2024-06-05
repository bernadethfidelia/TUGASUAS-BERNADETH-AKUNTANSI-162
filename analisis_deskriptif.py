# a. Total pendapatan selama satu bulan
total_pendapatan = df['Pendapatan'].sum()

# b. Rata-rata jumlah produk yang terjual per hari
rata_rata_jumlah_per_hari = df.groupby('Tanggal')['Jumlah'].sum().mean()

# c. Produk yang paling banyak terjual selama satu bulan
produk_terbanyak = df.groupby('Produk')['Jumlah'].sum().idxmax()

# d. Hari dengan pendapatan tertinggi dan terendah
pendapatan_harian = df.groupby('Tanggal')['Pendapatan'].sum()
pendapatan_tertinggi = pendapatan_harian.idxmax()
pendapatan_terendah = pendapatan_harian.idxmin()

# Menampilkan hasil
print(f"Total Pendapatan: {total_pendapatan}")
print(f"Rata-rata Jumlah Produk Terjual per Hari: {rata_rata_jumlah_per_hari}")
print(f"Produk Terbanyak Terjual: {produk_terbanyak}")
print(f"Hari dengan Pendapatan Tertinggi: {pendapatan_tertinggi} dengan Pendapatan {pendapatan_harian[pendapatan_tertinggi]}")
print(f"Hari dengan Pendapatan Terendah: {pendapatan_terendah} dengan Pendapatan {pendapatan_harian[pendapatan_terendah]}")
