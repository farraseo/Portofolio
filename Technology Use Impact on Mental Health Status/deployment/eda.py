# import libraries
import streamlit as st
import pandas as pd
from PIL import Image

def run():
    # title section
    st.title('Exploratory Data Analysis')

    # eda 3
    st.subheader("Apakah ada perbedaan signifikan antara rata-rata 'Technology_Usage_Hours' pada 'Stress_Level' tiap levelnya?")
    image_3 = Image.open('src/EDA3.png')
    st.image(image_3)
    with st.expander("Penjelasan"):
        st.caption("""Dari visualisasi di atas, rata-rata 'Technology_Usage_Hours" tidak ada perbedaan yang signifikan pada tiap 'Stress_Level" nya. Hal ini menunjukkan bahwa rata-rata penggunaan teknologi seperti perangkat elektronik tiap stress level tidak jauh berbeda, tetapi stress level (Low) memiliki rata-rata jam tertinggi.""")


    # eda 4
    st.subheader("Apakah ada perbedaan signifikan antara rata-rata 'Social_Media_Usage_Hours' pada 'Stress_Level' tiap levelnya?")
    image_4= Image.open('src/EDA4.png')
    st.image(image_4)
    with st.expander("Penjelasan"):
        st.caption("""Dari visualisasi di atas, rata-rata 'Social_Media_Usage_Hours" tidak ada perbedaan yang signifikan pada tiap 'Stress_Level" nya. Hal ini menunjukkan bahwa rata-rata penggunaan sosial media tiap stress level tidak jauh berbeda, tetapi stress level (high) memiliki rata-rata jam tertinggi.""")

    # eda 5
    st.subheader("Apakah ada perbedaan signifikan antara rata-rata 'Gaming_Hours' pada 'Stress_Level' tiap levelnya?")
    image_5 = Image.open('src/EDA5.png')
    st.image(image_5)
    with st.expander("Penjelasan"):
        st.caption("""Dari visualisasi di atas, rata-rata 'Gaming_Hours" tidak ada perbedaan yang signifikan pada tiap 'Stress_Level" nya. Hal ini menunjukkan bahwa rata-rata bermain game tiap stress level tidak jauh berbeda, tetapi stress level (Low) memiliki rata-rata jam tertinggi.""")

    # eda 6
    st.subheader("Apakah ada perbedaan signifikan antara rata-rata 'Screen_Time_Hours' pada 'Stress_Level' tiap levelnya?")
    image_6 = Image.open('src/EDA6.png')
    st.image(image_6)
    with st.expander("Explanation"):
        st.caption("""Dari visualisasi di atas, rata-rata 'Screen_Time" tidak ada perbedaan yang signifikan pada tiap 'Stress_Level" nya, tetapi stress level (Low) memiliki rata-rata jam tertinggi.""")
        
    # eda 7
    st.subheader("Apakah ada perbedaan signifikan antara rata-rata 'Sleep_Hours' pada 'Stress_Level' tiap levelnya?")
    image_7 = Image.open('src/EDA7.png')
    st.image(image_7)
    with st.expander("Penjelasan"):
        st.caption("""Dari visualisasi di atas, rata-rata 'Sleep_Hours" tidak ada perbedaan yang signifikan pada tiap 'Stress_Level" nya, tetapi stress level (High) memiliki rata-rata jam tertinggi.""")
    
    # eda 8
    st.subheader("Apakah ada perbedaan signifikan antara rata-rata 'Physical_Activity_Hours' pada 'Stress_Level' tiap levelnya?")
    image_8 = Image.open('src/EDA8.png')
    st.image(image_8)
    with st.expander("Penjelasan"):
        st.caption("""Dari visualisasi di atas, rata-rata 'Physical_Activity_Hours" tidak ada perbedaan yang signifikan pada tiap 'Stress_Level" nya, tetapi stress level (High) memiliki rata-rata jam tertinggi.""")
    
    # eda 9
    st.subheader("Apakah ada perbedaan signifikan antara rata-rata 'Sleep_Hours' pada 'Work_Environment_Impact' tiap pengaruhnya?")
    image_9 = Image.open('src/EDA9.png')
    st.image(image_9)
    with st.expander("Penjelasan"):
        st.caption("""Dari visualisasi di atas, rata-rata 'Sleep_Hours" tidak ada perbedaan yang signifikan pada tiap 'Work_Environment_Impact" nya, tetapi Work Environment Impact (Negative) memiliki rata-rata jam tertinggi.""")
    
    # eda 10
    st.subheader("Apakah ada perbedaan signifikan antara rata-rata 'Technology_Usage_Hours' pada 'Support_Systems_Access' tiap kategorinya?")
    image_10 = Image.open('src/EDA10.png')
    st.image(image_10,)
    with st.expander("Penjelasan"):
        st.caption("""Dari visualisasi di atas, rata-rata 'Technology_Usage_Hours" tidak ada perbedaan yang signifikan pada tiap 'Support_Systems_Access" nya, tetapi orang yang memiliki Support Systems Access (Yes) memiliki rata-rata jam tertinggi.""")
        

    # eda 11
    st.subheader("Apakah ada perbedaan signifikan antara rata-rata 'Technology_Usage_Hours' pada 'Online_Support_Usage' tiap kategorinya?")
    image_11 = Image.open('src/EDA11.png')
    st.image(image_11)
    with st.expander("Penjelasan"):
        st.caption("""Dari visualisasi di atas, rata-rata 'Technology_Usage_Hours" tidak ada perbedaan yang signifikan pada tiap 'Online_Support_Usage" nya, tetapi orang yang tidak memiliki Online Support (No) memiliki rata-rata jam tertinggi.""")


    # eda 12
    st.subheader("Apakah ada perbedaan signifikan antara rata-rata 'Sleep_Hours' pada 'Mental_Health_Status' tiap kategorinya?")
    image_12 = Image.open('src/EDA12.png')
    st.image(image_12)
    with st.expander("Penjelasan"):
        st.caption("""Dari visualisasi di atas, rata-rata 'Sleep_Hours" tidak ada perbedaan yang signifikan pada tiap 'Mental_Health_Status" nya, tetapi orang dengan status kesehatan mental 'Poor' memiliki rata-rata jam tertinggi.""")


    # eda 13
    st.subheader("Bagaimana distribusi 'Stress_Level' pada tiap kategori usia 10's - 60's?")
    image_13 = Image.open('src/EDA13.png')
    st.image(image_13)
    with st.expander("Penjelasan"):
        st.caption("""Dari visualisasi di atas, rata-rata 'Sleep_Hours" tidak ada perbedaan yang signifikan pada tiap 'Mental_Health_Status" nya, tetapi orang dengan status kesehatan mental 'Poor' memiliki rata-rata jam tertinggi.""")


     # eda 14
    st.subheader("Bagaimana distribusi 'Mental_Health_Status' pada tiap kategori usia 10's - 60's?")
    image_14 = Image.open('src/EDA14.png')
    st.image(image_14)
    with st.expander("Penjelasan"):
        st.caption("""Dari visualisasi di atas, berdasarkan persentase 'Mental_Health_Status' **Poor** terbanyak dimiliki oleh kategori usia 20's, **Fair** terbanyak dimiliki oleh kategori usia 60's, **Good** terbanyak dimiliki oleh kategori usia 10's, dan **Excellent** terbanyak dimiliki oleh kategori usia 30's.""")

if __name__=='__main__':
    run()