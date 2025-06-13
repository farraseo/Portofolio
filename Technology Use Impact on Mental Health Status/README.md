# Prediksi Mental Health State

## Repository Outline
1. P1M2_Farras_Annisa.ipynb - Berisi notebook preprocessing, model training, and model evaluation.
2. P1M2_Farras_Annisa_inf.ipynb - Berisi notebook untuk melakukan model inference.
3. P1M2_Farras_Annisa_conceptual.txt - Txt yang berisi jawaban dari pertanyaa conceptual problems.
4. P1M2_Farras_Annisa.csv - Dataset yang digunakan dalam format CSV.
5. deployment - Folder yang berisi file yang dibutuhkan untuk deployment.

## Problem Background
Sebagai lembaga yang bergerak dalam bidang kesehatan, khususnya kesehatan mental yang sudah berdiri selama 70 tahun, baru-baru ini NAC mengalami kesulitan dalam menentukan mental health state orang-orang yang datang ke lembaga tersebut. Hal ini dikarenakan faktor-faktor yang memengaruhinya bertambah dengan adanya penggunaan teknologi. Akibatnya NAC sering salah dalam memberikan metode terapi sehingga orang-orang yang datang untuk terapi tidak kunjung membaik. Agar dapat menentukan metode terapi yang tepat kita dapat membuat sebuah 5 model yang nantinya akan diuji untuk menentukan model mana yang dapat memprediksi mental health state yang paling baik.

## Project Output
- Membantu lembaga NAC yang bergerak dalam bidang kesehatan mental untuk mendiagnosa mental health state.
- Memberikan guide untuk pengkategorian mental health status.

## Data
- **User_ID** : ID unik dari setiap responden  
- **Age** : Umur dari setiap responden.
- **Gender** : Jenis kelamin setiap responden yang dibagi menjadi 3 (Male, Female, Others) dimana Others adalah responden yang tidak mau menyebutkan (Prefer Not To Say).              
- **Technology_Usage_Hours** : Waktu yang digunakan per hari (dalam jam) untuk menggunakan perangkat elektronik (komputer, smartphone, atau tablet) dari setiap responden, per hari (dalam jam).
- **Social_Media_Usage_Hours** : Waktu yang digunakan untuk mengakses platform media sosial (Instagram, Twitter, dan lain-lainnya) dari setiap responden, per hari (dalam jam).
- **Gaming_Hours** : Waktu yang digunakan untuk bermain game, baik di perangkat mobile, konsol, maupun komputer dari setiap responden, per hari (dalam jam).             
- **Screen_Time_Hours** : Waktu yang digunakan untuk menatap layar perangkat elektronik dari setiap responden, per hari (dalam jam).
- **Mental_Health_Status** : Status kesehatan mental dari setiap responden dalam kategori: Poor, Fair, Good, dan Excellent.    
- **Stress_Level** : Tingkat stress responden dalam kategori: Low, Medium, atau High.           
- **Sleep_Hours** : Jam tidur per hari dari setiap responden.
- **Physical_Activity_Hours** : Waktu yang digunakan untuk aktivitas fisik, seperti olahraga, berjalan kaki, atau kegiatan fisik lainnya per hari (dalam jam).   
- **Support_Systems_Access** : Menunjukkan apakah responden memiliki akses ke sistem dukungan sosial atau profesional, seperti keluarga, teman, terapis, atau layanan kesehatan mental (Yes/No).   
- **Work_Environment_Impact** : Persepsi responden terhadap dampak lingkungan kerja mereka terhadap kesehatan mental, dengan kategori: Positive, Neutral, atau Negative.
- **Online_Support_Usage** : Menunjukkan apakah responden menggunakan layanan dukungan kesehatan mental berbasis daring, seperti forum online, aplikasi konseling, atau care group (Yes/No). 

## Method
Project ini dibuat dengan menggunakan model supervised learning yaitu K-Nearest Neighbors (KNN), Support Vector Machine (SVM), Decision Tree, Random Forest Classifier, XGBoost dengan Decision Tree sebagai base model.

## Stacks
Project ini menggunakan bahasa pemrograman python, Visual Studio Code, Hugging Face, dan library Pandas, Numpy, Scikit-Learn, Scipy, Matplotlib.

## Reference
- [XGBoost Documentation](https://xgboost.readthedocs.io/en/release_3.0.0/)
- [XGBoost](https://www.geeksforgeeks.org/xgboost/)
- [Performance Metrics: Confusion matrix, Precision, Recall, and F1 Score](https://towardsdatascience.com/performance-metrics-confusion-matrix-precision-recall-and-f1-score-a8fe076a2262/)
- [Bagging dalam Machine Learning: Konsep dan Penerapannya](https://www.cloudcomputing.id/pengetahuan-dasar/bagging-machine-learning)
- [KNeighborsClassifier](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)
---

**Referensi tambahan:**
- [Technology use and interest in digital apps for mental health promotion and lifestyle intervention among young adults with serious mental illness](https://pmc.ncbi.nlm.nih.gov/articles/PMC11870643/)
- [How modern life affects our physical and mental health](https://www.medicalnewstoday.com/articles/318230#Digital-connectivity-and-well-being)
- [Exploring the Link Between Technology and Mental Health](https://counseling.online.wfu.edu/blog/exploring-link-technology-mental-health/)