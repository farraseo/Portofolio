[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/QEz7Kk5P)
# Milestone 3

_Milestone 3 ini dibuat guna mengevaluasi pembelajaran pada Hacktiv8 Data Science Fulltime Program khususnya pada Phase 2._

_version: GAIAv2.2_

_update date: 20250418_

---

## Objectives

Milestone 3 ini dibuat dengan tujuan sebagai berikut:

- Mampu menggunakan Apache Airflow.

- Mampu melakukan validasi data dengan menggunakan Great Expectations.

- Mampu memahami konsep NoSQL secara keseluruhan.

- Mampu mempersiapkan data untuk digunakan sebelum masuk ke database NoSQL.

- Mampu mengolah dan memvisualisasikan data dengan menggunakan Kibana.

---

## Dataset

### Ketentuan Dataset

1. Pilihlah dataset yang paling nyaman digunakan dalam mengerjakan Milestone 3. Adapun ketentuan dataset yang harus digunakan adalah :
   * Setidaknya terdapat minimal 10 column.
   * Setiap column terdiri dari :
     + Capital letter dan lower letter atau semua huruf merupakan capital letter.
     + Contoh : `Age`, `fullName`, `CITY`, `Education Level`.
   * Tidak diperbolehkan memilih dataset dimana nama column terdiri dari lower letter saja.
   * Terdapat campuran column berbentuk kategorikal dan numerikal. Sebisa mungkin jumlah kolom kategorikal dan numerikal seimbang, tidak ada yang terlalu mendominasi.

2. **Konsultasikan terlebih dahulu dataset yang hendak digunakan ke buddy masing-masing student. Jika disetujui, maka silakan dikerjakan. Jika tidak disetujui, maka cari dataset yang lain dan konsultasikan lagi mengenai dataset yang baru ini.**

3. Student tidak boleh menggunakan dataset yang sudah dipakai dalam sesi pembelajaran saat dikelas bersama instruktur atau dataset pada tugas-tugas terdahulu dari Phase 0 hingga Phase 2.

4. **Student dilarang untuk melakukan scraping dataset** karena dikhawatirkan proses pembuatan scraper dan proses scraping akan memakan waktu. Gunakan public dataset yang tersedia diberbagai macam situs Internet.

5. Anda dapat membayangkan bahwa Anda saat ini bekerja sebagai seorang Data Analyst disebuah perusahaan. Carilah dataset yang sekiranya merepresentasikan domain sebuah perusahaan seperti data mengenai : 
   - Product inventory.
   - Revenue & profit.
   - Kinerja pegawai.
   - Customer profile.
   - Keluhan produk/jasa.
   - dll.

6. Pada Milestone 3 ini, Anda akan membuat sebuah report. Saat melakukan konsultasi mengenai topik yang akan dikerjakan dengan buddy sertakan :
   - URL dataset yang hendak dipakai.
   - Latar belakang.
   - Tujuan yang hendak dicapai dengan adanya report ini. Spesifikkan mengenai problem yang Anda angkat dan kegunaannya.
   - User yang akan membaca report

   Contoh bentuk konsultasi :
   - Bad
     ```
     URL Dataset : https://www.kaggle.com/datasets/datasciencerikiakbar/gramedia-vs-goodreads-indonesia

     Latar belakang :
     Gramedia merupakan salah satu toko buku terbesar di Indonesia.
     Toko buku yang berdiri sejak tahun 1970 mempunyai banyak cabang yang tersebar di berbagai daerah.
     Selain itu, toko buku ini juga melayani penjualan secara online.

     Tujuan :
     Saya merupakan seorang Data Analyst yang sedang bekerja di Gramedia.
     Diharapkan dengan adanya report ini, dapat membantu Gramedia untuk mencapai profit yang lebih maksimal.

     User : Karyawan Gramedia.
     ```
     Kekurangan contoh diatas :
     - Latar Belakang dan Tujuan terasa seperti ada celah dan keterhubungannya kurang mengena.
     - Dari segi Tujuan, kurang spesifik menjelaskan bagaimana report akan membuat profit yang lebih banyak untuk perusahaan.
     - Dari segi User, terlalu umum. Semakin umum user yang akan membaca report-nya, menandakan bahwa report yang akan terbentuk tidak bisa menggunakan istilah-istilah tertentu dikarenakan beragamnya latar pendidikan setiap user.

   - Good
     ```
     URL Dataset : https://www.kaggle.com/datasets/datasciencerikiakbar/gramedia-vs-goodreads-indonesia
      
     Latar belakang :
     Menurut https://hot.detik.com/book/d-6732117/5-toko-buku-yang-tutup-selamanya, terdapat beberapa toko buku yang menutup secara permanen semua cabangnya.
     Diantaranya yaitu Toko Buku Gunung Agung dan Toko Buku Togamas yang berdiri sudah cukup lama.
     Hal ini menandakan bahwa keberadaan toko buku akhir-akhir ini kurang menguntungkan dari segi bisnisnya.

     Tujuan :
     Saat ini, saya merupakan seorang Data Analyst yang sedang bekerja di Gramedia.
     Report ini akan berisi karakteristik-karakteristik mengenai buku yang digemari oleh pembaca baik dari segi genre-nya, penulis, hingga penerbit.
     Selain itu, tidak hanya karakteristik buku yang digemari oleh pembaca saja yang ada di-report ini, melainkan saran-saran penjualan yang sekiranya dapat menjadi bahan pertimbangan oleh tim marketing/sales agar penjualan buku tersebut lebih optimal yang diharapkan akan menuntun ke profit yang lebih besar yang akan diperoleh oleh Gramedia.

     User : Divisi pengadaan buku, divisi marketing, dan divisi sales yang berada di Gramedia.
     ```

7. Dataset yang sama dapat dibuat menjadi beberapa report berbeda jika latar belakang, tujuan, dan target audiensnya berbeda.

8. Milestone yang dibuat juga akan dipresentasikan. Oleh karena itu, pastikan bahwa Anda memahami deskripsi dataset seperti latar belakang dataset tersebut, sumber dataset, makna setiap column dan nilainya, serta satuan dari masing-masing column-nya. Pastikan bahwa Anda menguasai data yang digunakan sehingga Anda dapat mempertahankan argumen/insight yang Anda berikan dan menghindari persepsi insight tidak dapat digali lebih dalam dikarenakan terbatasnya informasi dari dataset.

### Data Sources
Student dapat memilih dataset dari salah satu repository dibawah ini. Popular open data repositories :

- [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)
- [Kaggle datasets](https://www.kaggle.com/datasets)
- [Amazon’s AWS datasets](https://registry.opendata.aws/)

Meta portals :

- [Data Portals](http://dataportals.org/)
- [OpenDataMonitor](https://opendatamonitor.eu/frontend/web/index.php?r=dashboard%2Findex)
- [Quandl](https://www.quandl.com/)
- Sumber lain yang kredibel.

---

## Problem

Buatlah report yang berisi Exploratory Data Analysis (EDA) dari sebuah dataset dengan terlebih dahulu ditentukan mengenai objective yang hendak dicapai. **Report akan berisi hasil EDA dan rekomendasi lanjutan terkait dengan objective.**
  
Dataset akan terlebih dahulu dilakukan Data Cleaning dan validasi data menggunakan Great Expectation. Semua proses dilakukan dengan pipeline yang dijalankan menggunakan Apache Airflow. Berikut ini adalah langkah-langkah yang harus dilakukan : 

1. Tentukan dataset yang hendak dipakai. Beri nama dataset ini dengan `P2M3_<nama-student>_data_raw.csv`. Contoh : `P2M3_raka_ardhi_data_raw.csv`.

2. Masukan data tersebut ke dalam PostgreSQL masing-masing student. **PostgreSQL yang dimaksud adalah PostgreSQL yang Anda jalankan via Docker.** Beri nama table untuk menyimpan data tersebut dengan `table_m3`. Masukkan data tersebut apa adanya dengan tanpa adanya perubahan apapun.

3. Setelah data berada didalam database, ambil semua data dari database dengan menggunakan Python dan lakukan beberapa Data Cleaning berikut ini dengan menggunakan Python :
   - Hapus data yang duplikat.
   - Normalisasi column dengan cara : 
     + Semua nama column menjadi lowercase. Contoh : `ID` → `id`, `EDUCATION` → `education`, `Age` → `age`.
     + Spasi yang berada ditengah-tengah nama column diubah menjadi `_` (underscore). Contoh : `First Name` → `first_name`, `HOME ADDRESS` → `home_address`, `Alternative Phone Number` → `alternative_phone_number`.
     + Menghapus spasi/tab/simbol yang dirasa tidak diperlukan pada nama column. Contoh : `  name` → `name`, `|CAR_PRICE|` → `car_price`.
   - Handling Missing Values (dibebaskan mengenai jenis penanganannya).
   - Code mengenai hapus data duplikat dan Handling Missing Values harus tetap ada sekalipun pada data yang Anda gunakan tidak terdapat data duplikat atau missing values.

4. Setelah dilakukan Data Cleaning, simpan data clean ini ke dalam CSV file dengan nama `P2M3_<nama-student>_data_clean.csv`. Contoh : `P2M3_raka_ardhi_data_clean.csv`

5. Buatlah sebuah Python Notebook (.ipynb) untuk melakukan validasi data menggunakan Great Expectations. Adapun kriteria mengenai Expectation yang dipilih adalah :
   - Lakukan minimal 7 Expectations yang didalamnya harus ada Expectation untuk:
     + to be unique
     + to be between min_value and max_value
     + to be in set
     + to be in type list
     + 3 jenis Expectation yang berbeda yang tidak diajarkan pada lecture Week 2 Day 1 AM - Data Ethics & Data Validation
   - Anda diwajibkan untuk menerapkan 4 Expectation yang telah ditentukan dan 3 Expectation lain yang tidak diajarkan pada lecture dimana semua Expectation ini berbeda satu sama lain.
   - Ketujuh Expectation yang digunakan haruslah semuanya bernilai `success: true`.
   - Untuk Expectation `to be unique`, Anda diizinkan untuk membuat sebuah column baru jika dirasa column yang ada didataset tidak ada yang unik. Column baru ini haruslah berasal dari column yang sudah ada. Anda dapat membuat gabungan antara beberapa column yang sudah ada untuk column baru ini. Buatlah skenario fiksi mengenai kegunaan dari column ini sehingga jelas peruntukannya.
   - Setiap Expectation hanya boleh berada pada 1 cell yang berbeda-beda sehingga dapat dilihat mengenai hasilnya.
   - Simpan Python Notebook yang berisi data validation ini dengan nama `P2M3_<nama-student>_GX.ipynb`. Contoh : `P2M3_raka_ardhi_GX.ipynb`.

6. Selain disimpan ke dalam file CSV seperti poin 4, data clean ini juga akan dimasukkan ke dalam Elastic Search dengan menggunakan Python.

7. Lakukan automasi dengan membuat DAG dengan kriteria :
   - DAG berisi 3 node/task dibawah ini :
     + `Fetch from Postgresql` : berisi script untuk mengambil data dari PostgreSQL.
     + `Data Cleaning` : berisi script untuk melakukan Data Cleaning dan penyimpanan ke CSV file.
     + `Post to Elasticsearch` : berisi script untuk me-load CSV yang berisi data yang sudah clean dan memasukkannya ke Elasticsearch.
   - Penjadwalan dimulai pada tanggal 01 November 2024.
   - Penjadwalan dilakukan setiap hari Sabtu jam 09:10 AM hingga 09:30 AM dan dilakukan per 10 menit. Tabel dibawah ini adalah contoh hasil penjadwalannya :
     | No | Execution Time |
     | --- | --- |
     | 1 | Saturday, 2 November 2024 09:10 AM |
     | 2 | Saturday, 2 November 2024 09:20 AM |
     | 3 | Saturday, 2 November 2024 09:30 AM |
     | 4 | Saturday, 9 November 2024 09:10 AM |
     | 5 | Saturday, 9 November 2024 09:20 AM |
     | 6 | Saturday, 9 November 2024 09:30 AM |
     | 7 | Saturday, 16 November 2024 09:10 AM |
     | 8 | Saturday, 16 November 2024 09:20 AM |
     | 9 | ... |
   - Simpan DAG dengan nama `P2M3_raka_ardhi_DAG.py`.
   - Jalankan penjadwalan yang Anda buat. Lalu, screenshot mengenai graph DAG yang telah Anda jalankan dengan nama `P2M3_raka_ardhi_DAG_graph.jpg`. *([Ilustrasi graph DAG](https://miro.medium.com/v2/resize:fit:718/1*EF5guDGjuEW5G8a0UpBu7g.png))*

9. Buatlah dashboard dengan Kibana terhadap data clean ini dengan ketentuan :
   - Jelaskan mengenai objective Exploratory Data Analysis yang hendak dilakukan. Nyatakan secara jelas mengenai tujuan report yang akan dibuat seperti :
     * Latar belakang adanya report tersebut
     * Tujuan yang hendak dicapai
     * Divisi/tim yang membutuhkan
     * dll
   - Buatlah minimal 6 visualisasi terhadap data tersebut yang mendukung tercapainya objective dari proses EDA yang dilakukan. Adapun 6 visualisasi harus menggunakan plot seperti :
     * 1 penggunaan Horizontal Bar Plot
     * 1 penggunaan Vertical Bar Plot
     * 1 penggunaan Pie Chart
     * 3 plot lainnya dibebaskan mengenai jenisnya namun tidak boleh menggunakan jenis plot yang sama dengan plot yang sudah ada. Semua plot harus berbeda jenisnya satu sama lain.
   - Setelah sebuah plot terbentuk, berikan narasi/insight yang dapat diambil dari plot tersebut. Anda bisa meletakkan insight ini dibawah plot atau disamping plot.
   - Tambahkan 1 visualisasi berupa `Markdown` yang berisi :
     + Identitas student.
     + Penjelasan objective.
   - Tambahkan 1 visualisasi berupa `Markdown` yang berisi :
     + Kesimpulan eksplorasi yang dilakukan.
     + Saran lanjutan atau insight bisnis terhadap eksplorasi yang dilakukan.
     + Kesimpulan yang dituliskan haruslah berisi rekomendasi mengenai objective yang telah ditentukan berdasarkan gabungan antara hasil eksplorasi yang dilakukan dan suatu referensi eksternal (seperti teori suatu domain, pernyataan seorang ahli, fakta kompetitor, dll) sehingga rekomendasi dapat tepat sasaran dan masuk akal untuk diberikan.
   - Total visualisasi : 6 visualisasi + 1 visualisasi Markdown mengenai indetitas + 1 visualisasi Markdown mengenai kesimpulan = 8 visualiasi.
   - Student dipersilakan membuat skenario/situasi fiksi terhadap dataset yang dipakai.
   - Student dipersilakan untuk mengaplikasikan teori mengenai Business Knowledge pada tugas ini.

10. Screenshot setiap plot dan insight.
    - Buat sebuah folder bernama `images`.
    - Masukkan semua screenshot ke dalam folder tersebut.
    - Sebuah plot dan insightnya akan dimasukkan ke dalam screenshot yang sama. 
    - Screenshot juga bagian mengenai Identitas, Objective, dan Kesimpulan.
   
---

## Conceptual Problems

*Jawab pertanyaan berikut dengan menggunakan kalimat Anda sendiri:*

1. Jelaskan apa yang dimaksud dengan NoSQL menggunakan pemahaman yang kalian ketahui !

2. Jelaskan kapan harus menggunakan NoSQL dan Relational Database Management System !

3. Sebutkan contoh 2 tools/platform NoSQL selain ElasticSearch beserta keunggulan tools/platform tersebut !

4. Jelaskan apa yang Anda ketahui dari Airflow menggunakan pemahaman dan bahasa Anda sendiri !

5. Jelaskan apa yang Anda ketahui dari Great Expectations menggunakan pemahaman dan bahasa Anda sendiri !

6. Jelaskan apa yang Anda ketahui dari Batch Processing menggunakan pemahaman dan bahasa Anda sendiri (Definisi, Contoh Kasus Penggunaan, Tools, dll) !

---

## Instructions

*Milestone 3* dikerjakan dengan beberapa **kriteria wajib** di bawah ini:

1. *Project* dinyatakan selesai dan diterima untuk dinilai jika script dapat dijalankan dengan baik di prompt maupun terminal.

2. Pada tugas Milestone 3, student akan diminta untuk membuat :
   1. `P2M3_<nama-student>_ddl.txt`
      - File ini berisi :
        + URL dataset yang dijadikan acuan.
        + Syntax DDL untuk pembuatan table.
        + Syntax DML untuk melakukan insert data ke database. Anda bisa menggunakan perintah `COPY` untuk melakukan insert data.
      - Contoh penamaan : `P2M3_raka_ardhi_ddl.txt`
   2. `P2M3_<nama-student>_data_raw.csv`
      - File ini berisi dataset original yang akan dimasukkan ke dalam database PostgreSQL.
      - Contoh penamaan : `P2M3_raka_ardhi_data_raw.csv`.
   3. `P2M3_<nama-student>_data_clean.csv`
      - File ini berisi data yang telah dilakukan Data Cleaning.
      - Contoh penamaan : `P2M3_raka_ardhi_data_clean.csv`.
   4. `P2M3_<nama-student>_DAG.py`
      - File yang berisi DAG untuk dijalankan dengan menggunakan Apache Airflow yang terdiri dari :
        + Python code untuk mengambil data dari database PostgreSQL.
        + Python code untuk melakukan proses Data Cleaning seperti yang sudah ditentukan dan menyimpannya ke sebuah CSV file.
        + Python code untuk me-load CSV yang berisi data yang sudah clean dan memasukkannya ke dalam Elasticsearch.
      - Contoh penamaan : `P2M3_raka_ardhi_DAG.py`.
   5. `P2M3_<nama-student>_DAG_graph.jpg`
      - Screenshot yang menampilkan alur graph dari DAG yang dibuat.
      - Jalankan penjadwalan yang Anda buat. Setelah selesai dilakukan, barulah screenshot graph DAG ini.
      - Alur graph DAG haruslah berwarna hijau pada semua task-nya yang menandakan tidak ada masalah pada proses penjadwalan.
   6. `P2M3_<nama-student>_conceptual.txt`.
      - File ini berisi jawaban conceptual problem.
      - Contoh penamaan : `P2M3_raka_ardhi_conceptual.txt`.
   7. `P2M3_<nama-student>_GX.ipynb`
      - File ini berisi Expectations yang digunakan untuk melakukan validasi data.
      - Contoh penamaan : `P2M3_raka_ardhi_GX.ipynb`.
   8. `/images`.
      - Folder ini berisi daftar screenshot.
      - Contoh penamaan :
        * `introduction & objective.png`.
        * `plot & insight 01.png`.
        * `plot & insight 02.png`.
        * `plot & insight 03.png`.
        * `plot & insight 04.png`.
        * `plot & insight 05.png`.
        * `plot & insight 06.png`.
        * `kesimpulan.png`.
      - Jika sebuah plot dan insight ternyata tidak cukup dimasukkan kedalam sebuah gambar, Anda diizinkan untuk membuat lebih dari 1 screenshot untuk plot & insight tersebut. Perhatikan `plot & insight 06` dibawah ini :
        * `introduction & objective.png`.
        * `plot & insight 01.png`.
        * `plot & insight 02.png`.
        * `plot & insight 03.png`.
        * `plot & insight 04.png`.
        * `plot & insight 05.png`.
        * `plot & insight 06 - part 1.png`.
        * `plot & insight 06 - part 2.png`.
        * `kesimpulan.png`.

3. Markdown File Creation Instructions
   1. Pada repository ini terdapat file [description.md](description.md).

   2. File ini akan berisi deskripsi dokumentasi repository project yang Anda buat yang berfungsi untuk :
      - Menjelaskan tujuan project, fungsi, dan kegunaannya.
      - Memudahkan orang lain memahami project yang Anda kerjakan sebelum mereka melihat/menggunakannya.
      - Memberikan instruksi tentang bagaimana cara menginstall, membuka, menjalankan, dan memahami project yang Anda buat.
      - dll.

   3. Silakan edit file tersebut. Anda dapat menambah, mengurangi, atau mengubah bagian-bagian yang ada didalam file tersebut seperti :
      - Penambahan bagian instalasi program.
      - Penambahan bagian kontak.
      - Penambahan screenshot dashboard/web yang dibuat.
      - dll.

   4. Milestone 3 yang Anda buat ini dapat Anda masukkan ke repository GitHub pribadi Anda sebagai portofolio project yang pernah Anda kerjakan. Adapun ketentuannya adalah : 
      1. **Anda hanya berhak memasukkan Milestone 3 ke repository GitHub pribadi Anda setelah Anda berada di Phase 2 Week 4.**
      2. **File `README.md` yang ada pada repository tugas dilarang untuk dimasukkan ke repository pribadi.**
      3. Anda dapat memasukkan file Python Notebook beserta dataset ke dalam repository Anda.
          - Rename semua file yang Anda buat pada tugas ini.
          - Pada file notebook, Anda tidak perlu menuliskan mengenai Batch Hacktiv8.
      4. File [description.md](description.md) :
          - Masukkan ke dalam repository GitHub pribadi Anda.
          - Rename file ini menjadi `README.md`.
          - File ini akan menjadi dokumen utama yang akan menunjukkan deskripsi project yang telah Anda bangun.

   5. Catatan penting : 
      1. Anda wajib mengedit file [description.md](description.md) dan menguploadnya ke repository tugas GitHub Classroom.
      2. File ini akan selanjutnya dinilai sebagai salah satu bagian dalam Milestone 3.
      3. Setelah Anda selesai mengerjakan Milestone 3 ini, jangan membuat repository baru di GitHub Anda.
      4. Tunggulah hingga Anda berada di Phase 2 Week 4.

4. Pada file Python, **wajib** memberikan keterangan atau pengenalan dengan menggunakan `comment` atau `docstring` yang berisikan : Judul tugas, Nama, Batch, dan penjelasan singkat tentang program yang dibuat, fitur-fitur. Contoh:
    ```py
    '''
    =================================================
    Milestone 3

    Nama  : Raka Ardhi
    Batch : FTDS-001-RMT

    Program ini dibuat untuk melakukan automatisasi transform dan load data dari PostgreSQL ke ElasticSearch. Adapun dataset yang dipakai adalah dataset mengenai penjualan mobil di Indonesia selama tahun 2020.
    =================================================
    '''
    ```

5. Anda diwajibkan menggunakan class/function untuk memisahkan bagian code agar flow dari code yang dibuat mudah diikuti. Berikan penjelasan pada setiap class/function yang dibuat dengan menggunakan docstring seperti : 
   ```py
   def get_data_from_postgresql(url, database, table):
     '''
     Fungsi ini ditujukan untuk mengambil data dari PostgreSQL untuk selanjutnya dilakukan Data Cleaning.

     Parameters:
      url: string - lokasi PostgreSQL
      database: string - nama database dimana data disimpan
      table: string - nama table dimana data disimpan

     Return
      data: list of str - daftar data yang ada di database
        
     Contoh penggunaan:
     data = get_data_from_postgresql('localhost', 'db_phase2', 'table_m3')
     '''

     return data

   ```

---

## Submission

- Push Assignment yang telah Anda buat ke akun GitHub Classroom Anda masing-masing.

- Contoh bentuk repository :
  ```
  P2-M3/raka-ardhi
  |
  ├── description.md
  ├── P2M3_raka_ardhi_ddl.txt
  ├── P2M3_raka_ardhi_data_raw.csv
  ├── P2M3_raka_ardhi_data_clean.csv
  ├── P2M3_raka_ardhi_DAG.py
  ├── P2M3_raka_ardhi_DAG_graph.jpg
  ├── P2M3_raka_ardhi_conceptual.txt
  ├── P2M3_raka_ardhi_GX.ipynb
  ├── README.md
  ├── /images
        ├── introduction & objective.png
        ├── plot & insight 01.png
        ├── plot & insight 02.png
        ├── plot & insight 03.png
        ├── plot & insight 04.png
        ├── plot & insight 05.png
        ├── plot & insight 06.png
        └── kesimpulan.png
  ```

---

## Rubrics

### Code Review

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| DAG | DAG yang digunakan dapat dijalankan tanpa error | 18 pts |
| Great Expectation | Mampu membuat 7 Expectations dengan 0 Error | 2 pts / Expectation |
| Data Visualization | Mampu membuat minimal 6 visualisasi dengan menggunakan Kibana | 4 pts / visualisasi |
| Insight | Menampilkan **insight di setiap visualisasi** yang ditampilkan pada dashboard | 4 pts / insight |
| Conclusion | Penarikan kesimpulan yang dilakukan sejalan dengan tujuan dilakukannya eksplorasi dan terdapat saran/tindakan lanjutan/rekomendasi terhadap insight yang dihasilkan | 8 pts |
| Runs Perfectly | Kode berjalan tanpa ada error. Seluruh kode berfungsi dan dibuat dengan benar. | 5 pts |

### Concepts

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| NoSQL | Mampu menjawab 6 pertanyaan dengan singkat, jelas, dan padat serta sesuai dengan konsep dan logika yang ada mengenai Conceptual Problems | 2 pts / pertanyaan |

### Readability

| Criteria | Meet Expectations | Points |
| --- | --- | --- |
| Tertata Dengan Baik | Semua baris kode terdokumentasi dengan baik dengan Markdown untuk penjelasan kode | 18 pts |

```
Kriteria tertata dengan baik diantaranya adalah: 

1. Tidak menyalin markdown dari tugas lain.
2. Import library rapih (terdapat dalam 1 cell dan tidak ada unused libs).
3. Terdapat komentar pada setiap baris kode.
4. Adanya pemisah yang jelas antar section, dll.
5. Tidak adanya typo.
```

---

```
Total Points : 123

Catatan : Penilaian Milestone 3 juga dapat dipengaruhi oleh aktivitas student selama Phase 2 berlangsung, baik sesi kelas maupun sesi mentoring dengan buddy-nya masing-masing sehingga terdapat kemungkinan adanya penambahan atau pengurangan nilai diluar rubric yang telah disebutkan diatas.
```

---

## Notes

* Deadline : 
  - Default : Phase 2 Week 3 Day 1 pukul 23:59 WIB.
  - Deadline dapat berubah jika terdapat kondisi khusus seperti hari libur atau hal lain.
  - Silakan cek kembali mengenai deadline tugas ini pada repository Anda atau silakan tanyakan ke instruktur/buddy Anda.

* Commit terakhir di GitHub yang akan dinilai. Pastikan tidak ada commit yang dibuat setelah deadline.

* Jika commit terakhir GitHub telah melewati deadline, meskipun ada commit sebelumnya yang belum melewati deadline, akan mengakibatkan tugas Milestone 3 dinyatakan terlambat dan Milestone 3 mendapat nilai 0.
