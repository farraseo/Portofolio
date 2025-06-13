# import libraries
import streamlit as st
import pandas as pd
import eda
import prediction

# Sidebar navigation
page = st.sidebar.selectbox(
    label='Select Page',
    options=['Introduction', 'Exploratory Data Analysis', 'Model Prediction']
)

if page == 'Introduction':
    # Introduction Page
    st.title('Milestone 2')
    st.write('**Name:** Farras Annisa')
    st.write('**Batch:** HCK-027')


    # Background
    with st.expander('Latar Belakang'):
        st.caption(
            "Sebagai lembaga yang bergerak dalam bidang kesehatan, khususnya kesehatan mental yang sudah berdiri selama 70 tahun,"
            "baru-baru ini NAC mengalami kesulitan dalam menentukan mental health state orang-orang yang datang ke lembaga tersebut."
            "Hal ini dikarenakan faktor-faktor yang memengaruhinya bertambah dengan adanya penggunaan teknologi."
            "Akibatnya NAC sering salah dalam memberikan metode terapi sehingga orang-orang yang datang untuk terapi tidak kunjung membaik."
            "To optimize loan approval decisions, we apply machine learning to identify low-risk customers. "
            "Agar dapat menentukan metode terapi yang tepat kita dapat membuat sebuah 5 model yang nantinya akan diuji untuk menentukan model mana yang dapat memprediksi mental health status yang paling baik."
        )


   # Dataset Description
    with st.expander('Deskripsi Dataset'):
        st.caption(
            "Dataset ini berisi informasi tentang pemakaian teknologi dan gaya hidup. "
            "Terdiri dari kolom: User_ID, Age, Gender, Technology_Usage_Hours, Social_Media_Usage_Hours, Gaming_Hours, Screen_Time_Hours, "
            "Mental_Health_Status, Stress_Level, Sleep_Hours, Physical_Activity_Hours, Support_Systems_Access,"
            "Work_Environment_Impact, Online_Support_Usage"
        )

     # Objective
    with st.expander('Objective'):
        st.caption(
            "Membantu lembaga NAC yang bergerak dalam bidang kesehatan mental untuk mendiagnosa mental health status."
            "Memberikan guide untuk pengkategorian mental health status."
        )

     # Conclusion
    with st.expander('Kesimpulan'):
        st.caption(
            "Model terbaik yang saya sudah buat overfit dengan nilai recall pada Train set = 0.35 dan Test set = 0.17."
            "Model ini berkemungkinan besar dapat menyebabkan kesalahan pada predikisi. Hal ini terjadi dapat disebabkan data yang digunakan tidak mempunyai suatu pola yang spesifik yang bisa dipelajari oleh model atau proses feature engineering yang kurang optimal."
            "Maka dari itu model yang dibuat memiliki performa yang sangat buruk dalam membantu diagnosa kesehatan mental."
        )


    
    # Recommendation
    with st.expander('Rekomendasi'):
        st.caption(
            "Pada saat melakukan Hyperparameter tuning sebaiknya menggunakan Grid Search karena metode tersebut dapat menghasilkan model yang lebih optimal dibanding Randomized Search. "
            "Grid Search dapat menghasilkan model yang lebih optimal dikarenakan mencoba semua kombinasi hyperparameter, sedangkan Randomized Search hanya mencoba kombinasi hyperparameter menggunakan sampel yang ditentukan kombinasinya."
            "Atau dapat mengelompokkan Mental Health Status menjadi 2 kategori saja seperti Poor & Fair = 1, Good & Excellent = 0"
        )

elif page == 'Exploratory Data Analysis':
    eda.run()
elif page == 'Model Prediction':
    prediction.run()