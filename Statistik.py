import statistics

# Data nilai
data_median = [3, 4, 5, 6, 7, 8]

# Menghitung median
median_nilai = statistics.median(data_median)

print("Median =", median_nilai)


# Data nilai siswa
nilai_siswa = [12, 34, 56, 78, 89, 10, 24]

# Menghitung mean
mean_nilai = sum(nilai_siswa) / len(nilai_siswa)

print("Mean (Rata-rata) =", mean_nilai)


import statistics

# Data nilai
data_modus = [2, 2, 2, 2, 2, 2, 2, 9]

# Menghitung modus
modus_nilai = statistics.mode(data_modus)

print("Modus =", modus_nilai)
