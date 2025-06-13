# Grocery Inventory and Sales Analysis for Stock Monitoring


## Repository Outline
1. P2M3_Farras_Annisa_conceptual.txt - Berisi jawaban tentang pertanyaan Conceptual Problems
2. P2M3_Farras_Annisa_DAG.py - Script yang berisi kode untuk ETL
3. P2M3_Farras_Annisa_data_clean.csv - Berisi csv dengan data yang sudah dibersihkan (tidak ada missing value, penyesuaian tipe data, dan lain - lainnya)
4. P2M3_Farras_Annisa_data_raw.csv - Berisi csv dengan data mentah
5. P2M3_Farras_Annisa_GX.ipynb - Berisi notebook untuk Great Expectations (Data Validasi)
6. ddl.txt - Berisi query SQL

## Problem Background
Stok barang sangat penting bagi operasi sebuah toko untuk menjaga loyalitas pelanggan dan keberlangsungan bisnis. Kehabisan stok, atau stockout, dapat menyebabkan penurunan penjualan serta loyalitas pelanggan. Seringkali, masalah kehabisan stok disebabkan oleh sistem pengelolaan stok yang tidak efektif dan keterlambatan dalam proses restocking. Oleh karena itu, diperlukan sistem yang mampu mengantisipasi kehabisan stok dengan lebih baik, seperti memonitor stok secara real-time dan perencanaan restocking berdasarkan data historis.

## Project Output
Dashboard Stock Monitoring

## Data

Dataset terdiri dari 16 Kolom yaitu: 
- Product_ID: ID setiap produk.
- Product_Name : Nama produk.
- Catagory: Kategori produk (misalnya, Biji-bijian & Kacang-kacangan, Minuman, Buah & Sayur).
- Supplier_ID: ID untuk pemasok produk.
- Supplier_Name: Nama pemasok.
- Stock_Quantity: Jumlah stok produk saat ini di gudang.
- Reorder_Level: Tingkat stok di mana produk harus dipesan ulang.
- Reorder_Quantity: Jumlah produk yang dipesan.
- Unit_Price: Harga per unit produk.
- Date_Received: Tanggal produk diterima di gudang.
- Last_Order_Date: Tanggal terakhir produk dipesan.
- Expiration_Date: Tanggal kedaluwarsa produk, jika berlaku.
- Warehouse_Location: Alamat gudang.
- Sales_Volume: Total jumlah unit yang terjual.
- Inventory_Turnover_Rate: Tingkat perputaran stok, menunjukkan seberapa cepat produk terjual dan digantikan.
- Status: Status terkini produk (misalnya, Aktif, Dihentikan, Dalam Pemesanan Ulang).


## Method
Untuk proses ETL menggunakan Airflow yang datanya diambil dari PostgreSQL dan visualisasi menggunakan Kibana


## Stacks
Program dibuat menggunakan VS Code, PG Admin dengan bahasa pemrograman SQL dan python dengan library Pandas, timedelta, sqlalchemy, airflow, elasticsearch.

## Reference
Dataset: https://www.kaggle.com/datasets/salahuddinahmedshuvo/grocery-inventory-and-sales-dataset

---

**Referensi tambahan:**
- https://retalon.com/blog/what-is-safety-stock#elementor-toc__heading-anchor-6
- https://kmsoft.co.uk/healthcare/what-is-stock-management-and-why-is-it-important/
