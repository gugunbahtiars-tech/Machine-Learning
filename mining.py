import pandas as pd
import os
import json
import matplotlib.pyplot as plt

folder = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(folder, 'housing.csv')
df = pd.read_csv(csv_path)

df.to_excel(os.path.join(folder, 'housing.xlsx'), index=False)
df.to_json(os.path.join(folder, 'housing.json'), orient='records', indent=2)
df.to_html(os.path.join(folder, 'housing.html'), index=False)
df.to_xml(os.path.join(folder, 'housing.xml'), index=False, parser='etree')

plt.figure()
df['median_house_value'].hist(bins=30)
plt.title('Distribusi Harga Rumah')
plt.savefig(os.path.join(folder, 'grafik_harga.png'))
plt.close()

plt.figure()
df['ocean_proximity'].value_counts().plot(kind='bar')
plt.title('Kategori Ocean Proximity')
plt.savefig(os.path.join(folder, 'grafik_kategori.png'))
plt.close()

plt.figure()
df.isnull().sum().plot(kind='bar')
plt.title('Cek Data Null')
plt.savefig(os.path.join(folder, 'grafik_null.png'))
plt.close()

print(f"Jadi! Total {len(df)} baris - SEMUA FILE BERHASIL DIBUAT!")