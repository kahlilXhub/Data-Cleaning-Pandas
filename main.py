import numpy as np
import pandas as pd
df = pd.read_csv('raw_data.csv')

print("--- Data Mentah ---")
print(df)
print("\n")

df = df.dropna(how='all')
df['Harga'] = df['Harga'].astype(str).str.replace(r'[Rp\s\.]', '', regex=True)
df['Harga'] = pd.to_numeric(df['Harga'], errors='coerce')
df['Jumlah'] = pd.to_numeric(df['Jumlah'], errors='coerce')
df = df.dropna(subset=['Harga', 'Jumlah'])
df['Tanggal'] = pd.to_datetime(df['Tanggal'], errors='coerce')
df['Total_Omzet'] = df['Harga'] * df['Jumlah']
laporan_akhir = df.groupby('Produk')['Total_Omzet'].sum().reset_index()

print("--- Laporan Bersih ---")
print(laporan_akhir)