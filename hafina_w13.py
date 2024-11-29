import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as plx

# Title of the app
st.title('✨Prediksi Kebiasaan Belanja Pelajar✨')

# Sidebar Info
st.sidebar.info("""
    **🛍️ Prediksi Kebiasaan Belanja Pelajar**  
    Nama: **Hafina Meilawati**  
    NPM : **223307042**  
""")

# Choose Menu
menu = st.sidebar.selectbox(
    "🌟 Pilih Menu",
    ["📖 Deskripsi Data", "📂 Dataset", "📊 Grafik", "🔮 Prediksi Kebiasaan Belanja Pelajar"]
)

# Path to dataset
csv_url = 'student_spending (1).csv'  # Gantilah dengan path file yang sesuai

if menu == "📖 Deskripsi Data":
    st.header('📖 Deskripsi Dataset')
    st.write("""
        Dataset ini berisi informasi tentang kebiasaan belanja pelajar, dengan beberapa atribut utama:
        - 🧑‍🎓 **age**: Usia pelajar (dalam tahun).  
        - 👤 **gender**: Jenis kelamin pelajar (Laki-laki/Perempuan).  
        - 🏫 **year_in_school**: Tingkat pendidikan pelajar (Tahun Pertama hingga Lulus).  
        - 💰 **monthly_income**: Penghasilan bulanan pelajar (dalam Rupiah).  
        
        Tujuan dataset ini adalah untuk menganalisis pola belanja berdasarkan atribut tersebut, 
        serta memprediksi kebiasaan belanja berdasarkan data masukan.
    """)

    # Example structure of dataset
    try:
        df = pd.read_csv(csv_url)
        st.subheader("📋 Struktur Data:")
        st.write(df.head())  # Show first 5 rows
        st.write("Jumlah Baris dan Kolom:", df.shape)
        st.write("📂 Nama Kolom:", list(df.columns))
    except Exception as e:
        st.error(f"❌ Terjadi kesalahan saat memuat dataset: {e}")

elif menu == "📂 Dataset":
    st.header('📂 Data Kebiasaan Belanja Pelajar')

    try:
        # Read the CSV file directly
        df = pd.read_csv(csv_url)
        st.write(df.head())  # Show first 5 rows

        # Display dataset information and description
        st.subheader('📄 Informasi Data')
        st.write(df.info())
        st.write(df.describe())

    except Exception as e:
        st.error(f"❌ Terjadi kesalahan saat memuat dataset: {e}")

elif menu == "📊 Grafik":
    st.header('📊 Visualisasi Data Kebiasaan Belanja Pelajar')

    try:
        # Load dataset
        df = pd.read_csv(csv_url)

        # Visualize Age Distribution (Histogram)
        if 'age' in df.columns:
            st.subheader('🎂 Distribusi Umur')
            sns.histplot(df['age'], color='teal')
            st.pyplot()

        # Kernel Density Estimation for 'age'
        if 'age' in df.columns:
            st.subheader('🎨 Distribusi Umur (KDE)')
            sns.kdeplot(df['age'], shade=True)
            st.pyplot()

        # Visualize Gender Distribution (Pie Chart)
        if 'gender' in df.columns:
            st.subheader('👩‍🦰👨‍🦱 Distribusi Gender')
            plt.figure(figsize=(8, 8))
            plt.pie(df['gender'].value_counts(), labels=df['gender'].value_counts().index, autopct='%1.1f%%')
            plt.title('Gender Distribution')
            st.pyplot()

        # Visualize Year in School Distribution (Countplot)
        if 'year_in_school' in df.columns:
            st.subheader('📚 Distribusi Tahun Sekolah')
            sns.countplot(data=df, x='year_in_school', palette='coolwarm', order=df['year_in_school'].value_counts().index)
            st.pyplot()

        # Visualize Monthly Income Distribution (Plotly Histogram)
        if 'monthly_income' in df.columns:
            st.subheader('💵 Distribusi Penghasilan Bulanan')
            fig = plx.histogram(df, x="monthly_income")
            st.plotly_chart(fig)

        # Correlation Heatmap for Numeric Features
        st.subheader('🔥 Heatmap Korelasi')
        numeric_df = df.select_dtypes(include=['number'])  # Only numeric columns
        if not numeric_df.empty:
            sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm')
            st.pyplot()

    except Exception as e:
        st.error(f"❌ Terjadi kesalahan saat memproses data: {e}")

elif menu == "🔮 Prediksi Kebiasaan Belanja Pelajar":
    st.write("""
         Masukkan informasi berikut untuk memprediksi kebiasaan belanja pelajar berdasarkan data yang tersedia.
    """)

    # Input form for prediction
    age = st.slider("🎂 Usia", min_value=17, max_value=30, step=1, help="Pilih usia pelajar.")
    gender = st.selectbox("👩‍🦰👨‍🦱 Jenis Kelamin", ["Laki-laki", "Perempuan"], help="Pilih jenis kelamin pelajar.")
    year_in_school = st.selectbox(
        "📚 Tahun Sekolah",
        ["Tahun Pertama", "Tahun Kedua", "Tahun Ketiga", "Tahun Keempat", "Lulus"],
        help="Pilih tingkat pendidikan pelajar."
    )
    monthly_income = st.slider(
        "💰 Penghasilan Bulanan (Rp)", min_value=500000, max_value=10000000, step=50000,
        help="Masukkan penghasilan bulanan pelajar."
    )

    # Tombol prediksi
    if st.button("🔍 Prediksi"):
        # Contoh logika prediksi sederhana
        if monthly_income < 2000000:
            prediction = "🛍️ Cenderung hemat dan lebih memilih diskon."
        elif gender == "Perempuan" and year_in_school in ["Tahun Ketiga", "Tahun Keempat"]:
            prediction = "💄 Cenderung belanja fashion atau kosmetik."
        else:
            prediction = "💻 Cenderung belanja barang elektronik atau keperluan akademik."

        # Display prediction result
        st.subheader("🌟 Hasil Prediksi:")
        st.success(prediction)
